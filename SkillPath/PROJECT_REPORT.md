# SkillPath — Smart B.Tech Placement Planner
## Project Report

**Team:** Binary Brains  
**Hackathon track:** Skill Tank (EdTech)  
**Project type:** Web application MVP  
**Technology:** Python, Flask, SQLite, HTML, CSS

## 1. Abstract

B.Tech students often need to coordinate technical skills, portfolio projects, internships and placement preparation but may be unsure what to prioritise at each stage of their degree. SkillPath is a student-focused placement planning web application that organises preparation into a year-wise roadmap. A student selects their current year and target career, reviews a curated set of tasks and recommendations, marks tasks as complete, and sees a progress indicator. Profile choices and task completion are stored in a local SQLite database. The MVP is designed to be free to run on a Windows laptop and easy to demonstrate.

## 2. Problem statement

Help B.Tech students plan skills, projects, internships and placement preparation year-wise.

## 3. Objectives

- Provide a clear year-wise preparation roadmap.
- Recommend skills and portfolio projects relevant to a selected career goal.
- Encourage internship preparation and project documentation.
- Track completed tasks and display progress.
- Deliver an accessible, low-cost MVP that runs locally.

## 4. Target users

B.Tech students in years 1–4 who want a structured plan for software development, data science, data analytics or government technical-job preparation. The content is guidance, not a guarantee of employment or internship selection.

## 5. Proposed solution and workflow

1. The student opens the dashboard.
2. The student enters a display name, chooses an academic year and target career.
3. Flask validates the inputs and saves the profile to SQLite.
4. The application loads roadmap tasks for the selected year.
5. Career-goal rules select matching skill, project and internship suggestions.
6. The student marks roadmap tasks complete.
7. SQLite stores task completion, and the dashboard recalculates progress.
8. The student can refresh the page and see saved progress.

## 6. Architecture

**Presentation layer:** HTML template and responsive CSS render the dashboard and forms.

**Application layer:** Flask routes handle dashboard rendering, profile updates, task completion, progress reset and health checks. Python rules choose career recommendations.

**Data layer:** SQLite stores one local profile and roadmap tasks, including completion state.

**Request flow:** Browser → Flask route → validation and recommendation logic → SQLite read/write → rendered HTML response.

## 7. Main modules

- Profile and year selection
- Roadmap display
- Task completion
- Progress calculation
- Career-goal recommendation rules
- Project suggestion panel
- Internship-preparation panel
- SQLite persistence
- Health endpoint and automated smoke tests

## 8. Technology choices

Python and Flask provide a simple web backend. SQLite avoids a separate database server and stores data locally. HTML and CSS provide a responsive interface. The standard-library `unittest` framework supports basic automated tests. The MVP does not require paid APIs or services.

## 9. AI/SaaS relevance and honesty

The MVP currently uses a **rule-based recommendation engine**, which chooses curated skills, projects and internship actions from the user's career goal. This is personalised software logic but is not generative AI or a trained machine-learning model. A future optional AI integration could generate explanations or adapt roadmaps from a student's profile, but it must use a permitted service, protect student data, and be tested for accuracy. Judges should be shown the actual implemented behaviour rather than an unbuilt AI claim.

## 10. Testing plan

- Confirm the dashboard returns HTTP 200.
- Confirm the health endpoint returns a healthy status.
- Save a profile and confirm the chosen name and year appear.
- Mark a roadmap task complete and confirm the progress count changes.
- Refresh the page and verify completion persists.
- Change year and career goal and verify relevant content appears.
- Test invalid year and unknown career values are safely replaced by defaults.
- Review layout at desktop and narrow/mobile widths.

Automated tests are in `tests/test_app.py`. Manual end-to-end checks are still needed before submission.

## 11. Limitations

- The MVP is a local single-profile demo and has no user accounts.
- Recommendations are curated and rule-based.
- The roadmap is general guidance; it does not guarantee job outcomes.
- It does not yet include real-time job listings, calendar reminders, resume parsing, or an external AI model.
- The database is local to the machine.

## 12. Future enhancements

- Multi-user authentication and privacy-aware student profiles.
- Student-editable tasks, due dates and reminder preferences.
- A transparent recommendation explanation for every suggested task.
- Optional AI-generated recommendations with user consent and safeguards.
- Import/export of a roadmap, analytics, accessibility improvements and deployment.
- Content review with students, faculty and placement professionals.

## 13. Industry relevance

Early-career learners benefit from turning broad career ambitions into specific tasks and measurable progress. SkillPath demonstrates concepts used in career-tech and learning platforms: onboarding, profile-driven content, CRUD-style updates, persistence, dashboard visualisation, recommendation logic and software testing. These are transferable web-development skills, although the MVP is a prototype and should not be described as a production placement system.

## 14. Conclusion

SkillPath converts a broad placement-preparation problem into a structured and demonstrable workflow. Its core value is a year-wise roadmap, career-specific recommendations and persistent progress tracking. The next development priorities are user testing, content quality, accessibility, stronger automated tests, and an optional responsibly implemented AI feature.
