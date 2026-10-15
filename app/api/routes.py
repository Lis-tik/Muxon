from fastapi import APIRouter, HTTPException

from app.core.template_repository import load_templates
from app.services.job_service import process_job
from app.services.system_info_service import service_system_info

router = APIRouter()


@router.get("/templates")
def list_templates():
    return {"templates": load_templates()}


@router.get("/templates/{template_name}")
def get_template(template_name: str):
    from app.core.template_repository import get_template_by_name

    template = get_template_by_name(template_name)
    if template is None:
        raise HTTPException(status_code=404, detail="Template not found")
    return template


@router.post("/jobs/render")
def enqueue_render(job: dict):
    template_name = job.get("template_name")
    input_path = job.get("input_path")
    output_path = job.get("output_path")

    if not template_name or not input_path or not output_path:
        raise HTTPException(status_code=400, detail="template_name, input_path, and output_path are required")

    return process_job(template_name, input_path, output_path)


@router.get("/services/system_info")
def get_system_info():
    return service_system_info()