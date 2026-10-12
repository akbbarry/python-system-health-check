
import platform
import shutil
from datetime import datetime

print("=== DevOps System Health Check ===")
print(f"Time: {datetime.now()}")
print(f"Operating system: {platform.system()}")
print(f"Python version: {platform.python_version()}")

disk = shutil.disk_usage("/")
total_gb = disk.total / (1024**3)
free_gb = disk.free / (1024**3)
used_percent = (disk.used / disk.total) * 100

print(f"Disk total: {total_gb:.2f} GB")
print(f"Disk free: {free_gb:.2f} GB")
print(f"Disk used: {used_percent:.1f}%")

if free_gb < 2:
    print("WARNING: Low disk space!")
else:
    print("Disk space: OK")

