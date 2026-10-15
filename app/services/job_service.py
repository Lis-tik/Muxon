from pathlib import Path

from app.core.ffmpeg_service import FFmpegService
from app.core.template_repository import get_template_by_name


def process_job(template_name: str, input_path: str, output_path: str) -> dict:
    template = get_template_by_name(template_name)
    if template is None:
        return {
            "success": False,
            "error": f"Template '{template_name}' not found",
        }

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    ffmpeg = FFmpegService()
    result = ffmpeg.render(input_path, str(output_file), template)
    return result
