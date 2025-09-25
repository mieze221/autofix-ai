![AutoFix Logo](autofix/background.png)


# AutoFix – AI-Powered System Diagnostics

**Tagline:** Quickly identify system issues and get real-time diagnostics through a CLI or web interface.

---

## Project Overview

AutoFix is a Python-based system diagnostics tool that helps users monitor and troubleshoot their computer’s performance. It supports:

* **Internet connectivity checks**
* **Disk space monitoring**
* **CPU and RAM usage checks**
* **Python program availability verification**

The project includes both a **Command-Line Interface (CLI)** and a **Web Interface** built with Flask, demonstrating backend functionality, automated testing, and optional frontend design.

---

## Features

1. **CLI Mode**

   * Lightweight, terminal-based interface for running diagnostics.
   * Displays real-time status of system components.

2. **Web Interface**

   * Interactive, browser-based interface using Flask.
   * Displays diagnostic results in **color-coded cards**:

     * ✅ Green = OK
     * ⚠️ Yellow = Warning
     * ❌ Red = Fail
   * Responsive design with centered layout and AutoFix logo.

3. **Automated Testing**

   * Uses `pytest` to ensure all checks and functions work correctly.
   * Fully tested core diagnostics functions.

---

## Tech Stack & Tools

* **Languages:** Python 3.13
* **Frameworks:** Flask (Web interface)
* **Testing:** Pytest
* **Other Tools:** Git & GitHub for version control

---

## Getting Started

Follow these steps to run AutoFix locally:

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/autofix-ai.git
cd autofix-ai
```

2. **Install dependencies**

```bash
python3 -m pip install -r requirements.txt
```

3. **Run CLI**

```bash
python3 -m autofix.cli
```

* Opens the command-line interface to run diagnostics.
* Shows real-time status of Internet, Disk, CPU, RAM, and Python program availability.

4. **Run Web App**

```bash
python3 -m autofix_web.app
```

* Opens the web interface at `http://127.0.0.1:5000`.
* Displays results in **color-coded cards** with a centered layout and logo.

5. **Run Tests**

```bash
python3 -m pytest
```

* Verifies all backend functions work correctly using automated tests.
* Ensures reliability of diagnostic checks.

6. **Optional**

* Customize **thresholds** for disk space, CPU, and RAM in `autofix/config.py`.
* Update the web interface logo or styling in `autofix_web/static/`.

---

