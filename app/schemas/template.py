from pydantic import BaseModel, Field


class TemplatePreset(BaseModel):
    codec: str = Field(default="libx264")
    preset: str = Field(default="medium")
    crf: int = Field(default=23)
    fps: int = Field(default=30)
    width: int | None = None
    height: int | None = None
    bitrate: str | None = None
    audio_bitrate: str = Field(default="192k")


class VideoTemplate(BaseModel):
    name: str
    description: str = ""
    preset: TemplatePreset = Field(default_factory=TemplatePreset)
    output_extension: str = Field(default="mp4")
