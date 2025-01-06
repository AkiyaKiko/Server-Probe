# Read Sys_Stat
import psutil
import time

WTIME = 0.5  # Constant Wait Time 

def GetSysStat():
    # Initialize result dictionary
    _res = {}
    
    # Get CPU Stats: Number of cores and maximum frequency
    cpu_count = psutil.cpu_count(logical=True)  # Total number of logical CPUs
    cpu_freq = psutil.cpu_freq()
    _res['cpu_cores'] = cpu_count
    _res['cpu_max_freq'] = cpu_freq.max  # Maximum frequency in MHz

    # Collect CPU times for each core
    cpu_times_before = psutil.cpu_times(percpu=True)

    # Wait to measure CPU usage over WTIME
    time.sleep(WTIME)

    cpu_times_after = psutil.cpu_times(percpu=True)

    # Calculate the CPU usage for each core based on the difference in times
    cpu_usages = []
    for before, after in zip(cpu_times_before, cpu_times_after):
        total_time_before = sum(before)
        total_time_after = sum(after)
        idle_time_before = before.idle
        idle_time_after = after.idle

        total_time_diff = total_time_after - total_time_before
        idle_time_diff = idle_time_after - idle_time_before

        # Calculate CPU usage as (1 - idle_time / total_time) * 100
        if total_time_diff > 0:
            cpu_usage_percentage = (1 - (idle_time_diff / total_time_diff)) * 100
        else:
            cpu_usage_percentage = 0

        cpu_usages.append(cpu_usage_percentage)

    _res['cpu_usages'] = round(sum(cpu_usages)/len(cpu_usages),2)  # List of Average CPU usage

    # Get Memory Stats: Total memory and used memory
    memory_info = psutil.virtual_memory()
    _res['memory_total'] = memory_info.total  # Total memory in bytes
    _res['memory_used'] = memory_info.used  # Used memory in bytes

    # Get Swap Stats: Total swap and used swap
    swap_info = psutil.swap_memory()
    _res['swap_total'] = swap_info.total  # Total swap in bytes
    _res['swap_used'] = swap_info.used  # Used swap in bytes

    # Get Disk Stats: Total disk space and used space
    disk_info = psutil.disk_usage('/')
    _res['disk_total'] = disk_info.total  # Total disk space in bytes
    _res['disk_used'] = disk_info.used  # Used disk space in bytes

    # Get IO Usage: Read and write bytes for disk and network before and after a delay
    disk_io_counter_bef = psutil.disk_io_counters()
    net_io_counter_bef = psutil.net_io_counters()
    
    time.sleep(WTIME)
    
    disk_io_counter_aft = psutil.disk_io_counters()
    net_io_counter_aft = psutil.net_io_counters()

    _res['disk_read_bytes'] = disk_io_counter_aft.read_bytes - disk_io_counter_bef.read_bytes  # Bytes read
    _res['disk_write_bytes'] = disk_io_counter_aft.write_bytes - disk_io_counter_bef.write_bytes  # Bytes written
    _res['net_receive_bytes'] = net_io_counter_aft.bytes_recv - net_io_counter_bef.bytes_recv  # Bytes received
    _res['net_send_bytes'] = net_io_counter_aft.bytes_sent - net_io_counter_bef.bytes_sent  # Bytes sent

    return _res