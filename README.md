# Personal Expense Tracker

A simple Django + SQLite personal expense tracker based on the project report.

## Main modules
- User registration/login
- Income tracking
- Expense tracking and categories
- Bill management
- Dashboard/balance summary
- Notifications/reminders
- Feedback and ratings
- Basic report/export structure

## Run
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/
