import psutil
import time


def utilization():
    cpu_usage = psutil.cpu_percent(interval=1)
    per_core = enumerate(psutil.cpu_percent(percpu=True, interval=1)) # calculate per-core usage
    
    for i, percentage in per_core:
        if percentage > 50: # condition for high CPU usage
            print(f"Core {i}: {percentage}%")
            print("Warning: High CPU usage detected!")
        else:
            print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {cpu_usage:.2f}%")

while True:
    utilization()
    time.sleep(1) # wait for 1 second before next check