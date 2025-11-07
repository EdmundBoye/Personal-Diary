
# Personal Diary (Django + MySQL)
Prepared for GitHub user: EdmundBoye

This is a plain Django project configured to use **MySQL** via environment variables.
It includes a simple diary app with auth, CRUD for entries, templates and static files.

## Quick start (local, using a system MySQL)

1. Create and activate a virtualenv:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and edit values (especially `SECRET_KEY`, DB credentials).

3. Ensure MySQL is running and a database exists:
```sql
CREATE DATABASE diary_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'diary_user'@'localhost' IDENTIFIED BY 'diary_pass';
GRANT ALL PRIVILEGES ON diary_db.* TO 'diary_user'@'localhost';
FLUSH PRIVILEGES;
```

4. Run migrations & create superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
python manage.py runserver
```

5. Visit http://127.0.0.1:8000

## Notes
- For deployment use Gunicorn + Nginx and set DEBUG=0 in `.env`.
- This repo is ready to be pushed to GitHub. Rename the repo to your preference.
