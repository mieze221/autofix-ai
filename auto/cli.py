# cli.py
from core import check_internet, hello

def main():
    print(hello())
    if check_internet():
        print("Internet is working!")
    else:
        print("No internet detected.")

if __name__ == "__main__":
    main()

