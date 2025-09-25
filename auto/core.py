# core.py
import urllib.request
import shutil
import psutil

def hello():
    return "AutoFix is ready!"

# Internet connectivity check
def check_internet():
    try:
        urllib.request.urlopen('http://google.com')
        return "Internet is working!"
    except:
        return "No internet detected."

# Disk space check
def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    free_gb = free // (2**30)
    if free_gb < 5:
        return f"Low disk space: {free_gb}GB available"
    return f"Disk space OK: {free_gb}GB available"

# Program installed check
def check_program(program_name):
    if shutil.which(program_name):
        return f"{program_name} is installed."
    return f"{program_name} is NOT installed."

# cli.py
from core import hello, check_internet, check_disk_space, check_cpu_usage, check_ram, check_program

def main():
    print(hello())
    print("---------------------------")
    print(check_internet())
    print(check_disk_space())
    print(check_cpu_usage())
    print(check_ram())
    print(check_program("python"))
    print(check_program("git"))

if __name__ == "__main__":
    main()


