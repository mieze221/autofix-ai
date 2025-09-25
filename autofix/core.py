# core.py
import urllib.request
import shutil
import psutil
import subprocess
import platform
import os
import tempfile
from autofix.config import LOW_DISK_THRESHOLD_GB, HIGH_CPU_THRESHOLD_PERCENT, HIGH_RAM_USAGE_PERCENT

# ------------------------------
# Basic greeting
# ------------------------------
def hello():
    return "AutoFix is ready!"

# ------------------------------
# System diagnostics
# ------------------------------
def check_internet():
    try:
        urllib.request.urlopen('http://google.com', timeout=5)
        return "Internet is working!"
    except:
        return "No internet detected."

def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    free_gb = free // (2**30)
    if free_gb < LOW_DISK_THRESHOLD_GB:
        return f"Low disk space: {free_gb}GB available"
    return f"Disk space OK: {free_gb}GB available"

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > HIGH_CPU_THRESHOLD_PERCENT:
        return f"High CPU usage: {cpu_percent}%"
    return f"CPU usage is normal: {cpu_percent}%"

def check_ram():
    mem = psutil.virtual_memory()
    used_gb = mem.used / (1024 ** 3)
    total_gb = mem.total / (1024 ** 3)
    usage_percent = (used_gb / total_gb) * 100
    if usage_percent > HIGH_RAM_USAGE_PERCENT:
        return f"High RAM usage: {used_gb:.2f}GB used ({usage_percent:.1f}%)"
    return f"RAM usage is normal: {used_gb:.2f}GB used ({usage_percent:.1f}%)"

def check_program(program_name):
    if shutil.which(program_name):
        return f"{program_name} is installed."
    return f"{program_name} is NOT installed."

# ------------------------------
# New diagnostics
# ------------------------------
def check_ping(host="8.8.8.8"):
    """Ping a host to check network latency."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        output = subprocess.run(["ping", param, "1", host], capture_output=True)
        if output.returncode == 0:
            return f"Ping to {host} successful."
        else:
            return f"Ping to {host} failed."
    except Exception as e:
        return f"Ping test error: {e}"

def check_os():
    """Return OS name and version."""
    os_name = platform.system()
    os_version = platform.version()
    return f"Operating System: {os_name} {os_version}"

def check_temp_files():
    """Check number of files in temp directory."""
    temp_dir = tempfile.gettempdir()
    try:
        num_files = len(os.listdir(temp_dir))
        return f"Temporary files in {temp_dir}: {num_files}"
    except Exception as e:
        return f"Error checking temp files: {e}"

