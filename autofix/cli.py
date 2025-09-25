# cli.py
from .core import (
    hello,
    check_internet,
    check_disk_space,
    check_cpu_usage,
    check_ram,
    check_program,
    check_ping,
    check_os,
    check_temp_files
)
from .logger import log
import os


# Color codes
class Colors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def run_diagnostic(name, func, *args):
    """Run a diagnostic, print with color, and log the result."""
    result = func(*args) if args else func()

    # Color logic
    if "OK" in result or "working" in result or "installed" in result or "successful" in result:
        color = Colors.OKGREEN
    elif "High" in result or "Low" in result or "NOT" in result or "failed" in result:
        color = Colors.FAIL
    else:
        color = Colors.WARNING

    print(f"{Colors.BOLD}[{name}]{Colors.ENDC} {color}{result}{Colors.ENDC}")
    log(f"[{name}] {result}")


def main():
    while True:
        clear_screen()
        print(f"{Colors.BOLD}===== AutoFix CLI ====={Colors.ENDC}")
        print(hello())

        menu = {
            "1": ("Check Internet", check_internet),
            "2": ("Check Disk Space", check_disk_space),
            "3": ("Check CPU Usage", check_cpu_usage),
            "4": ("Check RAM Usage", check_ram),
            "5": ("Check Python Installation", check_program, "python"),
            "6": ("Check Git Installation", check_program, "git"),
            "7": ("Check Ping", check_ping),
            "8": ("Check OS Info", check_os),
            "9": ("Check Temp Files", check_temp_files),
            "10": ("Run All Diagnostics", None)
        }

        print("\nSelect an option:")
        for key, value in menu.items():
            print(f"{key}. {value[0]}")
        print("0. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "0":
            print("Exiting AutoFix. Goodbye!")
            break
        elif choice in menu:
            if choice == "10":
                for k, v in menu.items():
                    if k != "10":
                        run_diagnostic(*v)
            else:
                run_diagnostic(*menu[choice])
        else:
            print(f"{Colors.FAIL}Invalid choice. Please try again.{Colors.ENDC}")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()



