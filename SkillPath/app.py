from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "skillpath.db"
app = Flask(__name__)
app.secret_key = "change-this-local-demo-key"

CAREER_GOALS = {
    "Software Development": {
        "skills": ["Python or Java fundamentals", "Data structures and algorithms", "Git and GitHub", "SQL basics", "HTML, CSS and JavaScript"],
        "projects": ["Student Task Manager", "College Event Registration App", "Placement Preparation Tracker"],
        "internships": ["Prepare a one-page resume", "Publish one project on GitHub", "Practise coding problems 3 times per week"]
    },
    "Data Science": {
        "skills": ["Python fundamentals", "SQL", "Excel or spreadsheet analysis", "Pandas and data cleaning", "Data visualisation"],
        "projects": ["Student Performance Analysis", "Placement Trends Dashboard", "Public Dataset Exploratory Analysis"],
        "internships": ["Create a data-project portfolio", "Practise SQL queries", "Write a short project case study"]
    },
    "Data Analytics": {
        "skills": ["Excel", "SQL", "Data cleaning", "Power BI or another visualisation tool", "Communication and storytelling"],
        "projects": ["Student Performance Dashboard", "Sales Data Analysis", "Survey Results Dashboard"],
        "internships": ["Create two dashboard screenshots", "Practise business questions with SQL", "Prepare a portfolio summary"]
    },
    "Government Technical Jobs": {
        "skills": ["Core CSE fundamentals", "Programming practice", "Computer networks and operating systems", "Quantitative aptitude", "Exam syllabus and notification tracking"],
        "projects": ["Technical Notes Organiser", "Practice Test Tracker", "CSE Revision Planner"],
        "internships": ["Maintain a weekly study plan", "Track official exam notifications", "Practise timed mock tests"]
    }
}

YEAR_TASKS = {
    1: [
        ("Programming foundations", "Skills", "Learn variables, conditions, loops, functions and basic problem solving."),
        ("Study routine", "Career", "Create a weekly study timetable and review it every Sunday."),
        ("GitHub basics", "Portfolio", "Create a GitHub account and publish one small practice program."),
        ("Explore career paths", "Career", "Compare software, analytics, data science and government technical roles.")
    ],
    2: [
        ("Core programming", "Skills", "Strengthen Python or Java and solve beginner programming problems."),
        ("SQL and databases", "Skills", "Practise SELECT, WHERE, JOIN, GROUP BY and basic database design."),
        ("Build a mini-project", "Project", "Complete one useful project and document how it works."),
        ("Create a GitHub portfolio", "Portfolio", "Add a README, screenshots and setup instructions to your repository."),
        ("Explore internships", "Internship", "Prepare a resume draft and identify relevant internship requirements.")
    ],
    3: [
        ("Data structures and algorithms", "Skills", "Practise arrays, strings, hashing, stacks, queues, trees and complexity."),
        ("Career-specific skills", "Skills", "Follow the selected career goal's skill list and build evidence for each skill."),
        ("Build a substantial project", "Project", "Complete a project with a clear user problem, database and tests."),
        ("Apply for internships", "Internship", "Track suitable opportunities and tailor your resume truthfully."),
        ("Interview practice", "Placement", "Practise explaining projects and answering technical questions.")
    ],
    4: [
        ("Revise core subjects", "Placement", "Revise DBMS, operating systems, networks, programming and other target-exam topics."),
        ("Polish portfolio projects", "Portfolio", "Ensure projects run from a clean setup and include screenshots and tests."),
        ("Resume and applications", "Placement", "Tailor your resume to each role and keep an application tracker."),
        ("Mock interviews", "Placement", "Practise technical, behavioural and project explanation questions."),
        ("Placement or exam plan", "Career", "Set weekly targets based on the roles or examinations you are pursuing.")
    ]
}

def connect_db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    with connect_db() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS profile (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                student_name TEXT NOT NULL DEFAULT 'Student',
                year INTEGER NOT NULL DEFAULT 2,
                goal TEXT NOT NULL DEFAULT 'Software Development'
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                year INTEGER NOT NULL,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                UNIQUE(year, title)
            )
        """)
        con.execute("INSERT OR IGNORE INTO profile (id, student_name, year, goal) VALUES (1, 'Student', 2, 'Software Development')")
        for year, items in YEAR_TASKS.items():
            for title, category, description in items:
                con.execute("""
                    INSERT OR IGNORE INTO tasks (year, title, category, description)
                    VALUES (?, ?, ?, ?)
                """, (year, title, category, description))

@app.route("/", methods=["GET"])
def index():
    init_db()
    with connect_db() as con:
        profile = con.execute("SELECT * FROM profile WHERE id = 1").fetchone()
        year = int(request.args.get("year", profile["year"]))
        if year not in (1, 2, 3, 4):
            year = profile["year"]
        goal = request.args.get("goal", profile["goal"])
        if goal not in CAREER_GOALS:
            goal = profile["goal"]
        tasks = con.execute("SELECT * FROM tasks WHERE year = ? ORDER BY id", (year,)).fetchall()
    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    percent = round((completed / total) * 100) if total else 0
    recs = CAREER_GOALS[goal]
    return render_template("index.html", profile=profile, year=year, goal=goal,
                           goals=list(CAREER_GOALS.keys()), tasks=tasks, total=total,
                           completed=completed, percent=percent, recs=recs)

@app.route("/save-profile", methods=["POST"])
def save_profile():
    name = request.form.get("student_name", "Student").strip()[:60] or "Student"
    try:
        year = int(request.form.get("year", 2))
    except ValueError:
        year = 2
    if year not in (1, 2, 3, 4):
        year = 2
    goal = request.form.get("goal", "Software Development")
    if goal not in CAREER_GOALS:
        goal = "Software Development"
    with connect_db() as con:
        con.execute("UPDATE profile SET student_name=?, year=?, goal=? WHERE id=1", (name, year, goal))
    flash("Your profile and roadmap preferences were saved.")
    return redirect(url_for("index", year=year, goal=goal))

@app.route("/toggle-task/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    with connect_db() as con:
        task = con.execute("SELECT id, year, completed FROM tasks WHERE id=?", (task_id,)).fetchone()
        if task:
            con.execute("UPDATE tasks SET completed=? WHERE id=?", (0 if task["completed"] else 1, task_id))
            profile = con.execute("SELECT year, goal FROM profile WHERE id=1").fetchone()
            year = task["year"]
            goal = profile["goal"]
        else:
            year, goal = 2, "Software Development"
    return redirect(url_for("index", year=year, goal=goal))

@app.route("/reset-progress", methods=["POST"])
def reset_progress():
    with connect_db() as con:
        con.execute("UPDATE tasks SET completed=0")
        profile = con.execute("SELECT year, goal FROM profile WHERE id=1").fetchone()
    flash("Progress was reset for the demo.")
    return redirect(url_for("index", year=profile["year"], goal=profile["goal"]))

@app.route("/health")
def health():
    return {"status": "ok", "app": "SkillPath"}

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
