import json
from pathlib import Path

from app.config import settings


def load_templates() -> list[dict]:
    template_dir = Path(settings.template_dir)
    if not template_dir.exists():
        return []

    templates: list[dict] = []
    for file_path in sorted(template_dir.glob("*.json")):
        with file_path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
            templates.append(data)
    return templates


def get_template_by_name(name: str) -> dict | None:
    for template in load_templates():
        if template.get("name") == name:
            return template
    return None
