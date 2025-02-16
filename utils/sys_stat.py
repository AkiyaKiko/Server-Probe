import asyncio
import psutil

async def get_system_info():
    """异步获取系统信息"""

    # CPU 核心数
    physical_cores = psutil.cpu_count(logical=False) # 物理核心
    logical_cores = psutil.cpu_count() # 逻辑核心


    # CPU 占用百分比
    cpu_percent = psutil.cpu_percent(interval=1)  # 每隔 1 秒采样一次

    # 内存占用
    memory = psutil.virtual_memory()
    memory_used = memory.used  # 已用内存
    memory_total = memory.total  # 总内存

    # SWAP 占用
    swap = psutil.swap_memory()
    swap_used = swap.used  # 已用 SWAP
    swap_total = swap.total  # 总 SWAP

    # 磁盘占用 (这里以根目录为例)
    disk = psutil.disk_usage("/")
    disk_used = disk.used  # 已用磁盘空间
    disk_total = disk.total  # 总磁盘空间

    return {
        "physical_cores": physical_cores,
        "logical_cores": logical_cores,
        "cpu_percent": cpu_percent,
        "memory_used": memory_used,
        "memory_total": memory_total,
        "swap_used": swap_used,
        "swap_total": swap_total,
        "disk_used": disk_used,
        "disk_total": disk_total,
    }

async def main():
    system_info = await get_system_info()
    print(system_info)

if __name__ == "__main__":
    asyncio.run(main())