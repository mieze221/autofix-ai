![AutoFix Logo](./auto/picture.png)


# AutoFix – AI-Powered Tech Support Assistant 

**Diagnose everyday computer and Wi-Fi issues, get step-by-step solutions, and save your fix history.**

---

##  Features

### MVP
- User types a tech issue → AI returns a suggested solution
- CLI tool + API ready for integration

### Future
- Automated troubleshooting scripts (network, disk, etc.)
- History tracking & user dashboard
- Web frontend for a polished UI

---

##  Tech Stack
- **Backend:** Python + FastAPI  
- **CLI / Core Modules:** `core.py`, `checks/`, `fixers/`  
- **AI Integration:** OpenAI API (GPT)  
- **Database:** SQLite / DynamoDB (for history, optional)  
- **Frontend (optional):** React + Tailwind CSS  
- **Deployment & CI/CD:** Docker, GitHub Actions

---

## Installation

```bash
git clone https://github.com/yourusername/autofix.git
cd autofix
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt

