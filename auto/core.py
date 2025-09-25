# core.py
import urllib.request
import shutil
import psutil

def hello():
    return "AutoFix is ready!"

def check_internet():
    try:
        urllib.request.urlopen('http://google.com')
        return "Internet is working!"
    except:
        return "No internet detected."

def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    free_gb = free // (2**30)
    if free_gb < 5:
        return f"Low disk space: {free_gb}GB available"
    return f"Disk space OK: {free_gb}GB available"

def check_program(program_name):
    if shutil.which(program_name):
        return f"{program_name} is installed."
    return f"{program_name} is NOT installed."

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > 80:
        return f"High CPU usage: {cpu_percent}%"
    return f"CPU usage is normal: {cpu_percent}%"

def check_ram():
    mem = psutil.virtual_memory()
    used_gb = mem.used / (1024 ** 3)
    total_gb = mem.total / (1024 ** 3)
    if used_gb / total_gb > 0.8:
        return f"High RAM usage: {used_gb:.2f}GB used"
    return f"RAM usage is normal: {used_gb:.2f}GB used"
