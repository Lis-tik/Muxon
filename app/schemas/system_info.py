from pydantic import BaseModel

class SystemInfo(BaseModel):
    os_name: str | None
    cpu_model: CPUInfo | None
    gpu_models: list[str] | None
    memory_total_bytes: float | None
    memory_available_bytes: float | None
    

class CPUInfo(BaseModel):
    model: str | None
    arch: str | None
    threads: int | None
    frequency: str | None