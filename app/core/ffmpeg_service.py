import subprocess
from pathlib import Path


class FFmpegService:
    def __init__(self, ffmpeg_bin: str = "ffmpeg"):
        self.ffmpeg_bin = ffmpeg_bin

    def build_command(self, input_path: str, output_path: str, template: dict) -> list[str]:
        preset = template.get("preset", {})
        codec = preset.get("codec", "libx264")
        fps = preset.get("fps", 30)
        crf = preset.get("crf", 23)
        width = preset.get("width")
        height = preset.get("height")
        bitrate = preset.get("bitrate")
        audio_bitrate = preset.get("audio_bitrate", "192k")
        scale_filter = ""

        if width and height:
            scale_filter = f" -vf scale={width}:{height}"

        bitrate_filter = f" -b:v {bitrate}" if bitrate else ""
        command = [
            self.ffmpeg_bin,
            "-y",
            "-i",
            input_path,
            "-c:v",
            codec,
            "-preset",
            preset.get("preset", "medium"),
            "-crf",
            str(crf),
            "-r",
            str(fps),
            *([] if not scale_filter else ["-vf", f"scale={width}:{height}"]),
            "-c:a",
            "aac",
            "-b:a",
            audio_bitrate,
            *([] if not bitrate else ["-b:v", bitrate]),
            output_path,
        ]
        return command

    def render(self, input_path: str, output_path: str, template: dict) -> dict:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        command = self.build_command(input_path, str(output), template)
        result = subprocess.run(command, capture_output=True, text=True)

        return {
            "command": " ".join(command),
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "output_path": str(output),
        }
