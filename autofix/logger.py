# logger.py
import datetime

def log(message):
    with open("autofix.log", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")
