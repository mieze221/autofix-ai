from flask import Flask, render_template, request
from autofix.core import check_internet, check_disk_space, check_cpu_usage, check_ram, check_program

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        # List of checks: name + function
        checks = [
            ("Internet", check_internet),
            ("Disk Space", check_disk_space),
            ("CPU Usage", check_cpu_usage),
            ("RAM Usage", check_ram),
            # Hardcode program check (e.g., python3)
            ("Python Program", lambda: check_program("python3"))
        ]

        # Run each check and collect results
        for name, func in checks:
            status = func()  # should return "OK", "Warning", or "Fail"
            results.append({"name": name, "status": status})

    return render_template("index.html", results=results)


if __name__ == "__main__":
    # Run on port 5000
    app.run(debug=True, port=5000)
