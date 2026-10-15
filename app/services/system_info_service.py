import platform
import psutil
import cpuinfo

from app.schemas.system_info import SystemInfo, CPUInfo

def service_system_info() -> SystemInfo:
    os_name = platform.platform()
    cpu_model = cpuinfo.get_cpu_info().get('brand_raw')
    cpu_arch = cpuinfo.get_cpu_info().get('arch')

    cpu_threads = cpuinfo.get_cpu_info().get('count')
    cpu_frequency = None
    if 'hz_advertised_friendly' in cpuinfo.get_cpu_info():
        cpu_frequency = cpuinfo.get_cpu_info().get('hz_advertised_friendly')
        
    gpu_models = []  # Placeholder for GPU models, as this requires additional libraries
    memory_total_bytes = psutil.virtual_memory().total
    memory_available_bytes = psutil.virtual_memory().available

    return SystemInfo(
        os_name=os_name,
        
        cpu_model=CPUInfo(
            model=cpu_model,
            arch=cpu_arch,
            threads=cpu_threads,
            frequency=cpu_frequency
        ) if cpu_model else None,
        
        gpu_models=gpu_models,
        memory_total_bytes=memory_total_bytes,
        memory_available_bytes=memory_available_bytes
    )
