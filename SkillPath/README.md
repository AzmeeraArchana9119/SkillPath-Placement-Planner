# SkillPath — Smart B.Tech Placement Planner

**Team:** Binary Brains  
**Track:** Skill Tank (EdTech)  
**Problem:** Help B.Tech students plan skills, projects, internships and placement preparation year-wise.

SkillPath is a beginner-friendly local web app that lets a student choose their B.Tech year and career goal, view a roadmap, explore project and internship preparation suggestions, mark roadmap tasks complete, and track progress.

## Features

- Select academic year (1st–4th) and target career.
- View a year-specific roadmap.
- Mark tasks complete and track completion percentage.
- See career-specific skills, project ideas and internship-preparation suggestions.
- Persist profile and task progress in SQLite.
- Responsive dashboard for laptop and mobile screens.
- Health endpoint at `/health`.
- Automated smoke tests.

## Free technology stack

- Python 3
- Flask
- SQLite
- HTML, CSS
- Python `unittest`

No paid API or AI service is required. The initial recommender uses transparent rules and curated content; it is not a generative AI model.

## Run on Windows

1. Install Python 3 from https://www.python.org/downloads/windows/ if it is not already installed. During setup, select **Add Python to PATH** if shown.
2. Open this folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If `py` does not work, try `python` instead. If PowerShell blocks activation, run the commands below using Command Prompt terminal, or use `.\.venv\Scripts\python.exe` directly.

5. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Start the app:

   ```powershell
   python app.py
   ```

7. Open http://127.0.0.1:5000 in your browser.

Stop the server with `Ctrl+C` in the terminal.

## Run tests

With the virtual environment activated:

```powershell
python -m unittest discover -s tests -v
```

## Project structure

```text
SkillPath/
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    └── test_app.py
```

The SQLite database (`skillpath.db`) is created automatically when the app starts. It is intentionally excluded from Git.

## GitHub publishing

Create an empty public repository named `SkillPath-Placement-Planner` on GitHub. In this folder's terminal, run:

```powershell
git init
git add .
git commit -m "Build SkillPath placement planner MVP"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/SkillPath-Placement-Planner.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Do not upload passwords, tokens, private student data, or the generated database.

## Suggested demo flow

1. Open the dashboard and introduce the student problem.
2. Select a year and career goal; save the profile.
3. Show the matching roadmap and recommendations.
4. Mark one or two tasks complete.
5. Show the progress percentage changing.
6. Refresh the page and show that progress persists.
7. Explain limitations and planned improvements honestly.

## Current limitations and future work

- The first version is a local, single-profile demo; it has no multi-user login.
- Recommendations are rule-based and curated, not generative AI.
- Roadmap content should be reviewed by faculty, placement officers and students.
- Future versions could add separate student accounts, editable tasks, deadline reminders, a real AI service behind an optional integration, deployment, accessibility checks and analytics.
