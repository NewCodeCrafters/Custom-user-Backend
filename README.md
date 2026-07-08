# Django Custom User Authentication

A Django project configured with a custom user model that uses **email authentication** instead of the default username-based authentication.

---

# Features

- Custom User Model
- Email Authentication
- Custom User Manager
- User Registration
- User Login
- User Logout
- Profile Picture Upload
- Django Admin Integration
- Password Hashing
- Media File Support
- Poetry Dependency Management

---

# Tech Stack

- Python 3.12+
- Django
- PostgreSQL
- Poetry
- Pillow

---

# Prerequisites

Before starting, ensure you have installed:

- Python 3.12 or later
- Poetry
- PostgreSQL
- Git

Check your installations:

```bash
python --version
poetry --version
psql --version
git --version
```

---

# Clone the Repository

```bash
git clone <repository-url>
```

Move into the project.

```bash
cd <project-folder>
```

---

# Install Dependencies

## Using Poetry (Recommended)

Install all project dependencies.

```bash
poetry install
```

Activate the virtual environment.

```bash
poetry shell
```

If your Poetry version doesn't support `shell`, use:

```bash
poetry env activate
```

---

## Using pip

Create a virtual environment.

Linux/macOS

```bash
python -m venv .venv
```

Activate it.

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Installing Required Packages

If starting from scratch:

```bash
poetry add django
```

```bash
poetry add pillow
```

```bash
poetry add psycopg[binary]
```

Optional packages:

```bash
poetry add python-decouple
```

```bash
poetry add whitenoise
```

```bash
poetry add gunicorn
```

Development packages:

```bash
poetry add --group dev black isort flake8
```

```bash
poetry add --group dev pytest pytest-django
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key

DEBUG=True

DATABASE_NAME=database_name
DATABASE_USER=postgres
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

---

# Configure the Database

Create a PostgreSQL database.

Example:

```sql
CREATE DATABASE custom_user_db;
```

Update `settings.py` with your database credentials.

---

# Apply Migrations

Create migration files.

```bash
python manage.py makemigrations
```

Apply migrations.

```bash
python manage.py migrate
```

---

# Create a Superuser

```bash
python manage.py createsuperuser
```

Provide:

- Email
- Password

---

# Start the Development Server

```bash
python manage.py runserver
```

Open your browser.

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin/
```

---

# Common Django Commands

Run server

```bash
python manage.py runserver
```

Run server on another port

```bash
python manage.py runserver 8001
```

Create migrations

```bash
python manage.py makemigrations
```

Apply migrations

```bash
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Collect static files

```bash
python manage.py collectstatic
```

Open Django shell

```bash
python manage.py shell
```

Run tests

```bash
python manage.py test
```

Show migration status

```bash
python manage.py showmigrations
```

Create a new app

```bash
python manage.py startapp app_name
```

---

# Project Structure

```
project/
│
├── apps/
│   └── user/
│       ├── migrations/
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── managers.py
│       ├── models.py
│       ├── urls.py
│       └── views.py
│
├── media/
├── static/
├── templates/
├── manage.py
├── pyproject.toml
├── poetry.lock
├── .env
├── .gitignore
└── README.md
```

---

# User Model Fields

| Field | Description |
|---------|-------------|
| first_name | User's first name |
| last_name | User's last name |
| email | Login email (unique) |
| phone_number | User phone number |
| profile_picture | Optional profile picture |
| is_active | Active account |
| is_staff | Staff permission |
| is_superuser | Superuser permission |
| is_verified | Verification status |
| date_joined | Registration timestamp |

---

# Media Configuration

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

---

# Authentication

The project uses:

- Email authentication
- Password hashing
- Custom User model
- Django Authentication Backend

No username is required.

---

# Useful Poetry Commands

Install dependencies

```bash
poetry install
```

Add a package

```bash
poetry add package-name
```

Remove a package

```bash
poetry remove package-name
```

Update packages

```bash
poetry update
```

Show installed packages

```bash
poetry show
```

Run a command inside Poetry

```bash
poetry run python manage.py runserver
```

Export requirements (optional)

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

---

# Git

Initialize Git

```bash
git init
```

Add files

```bash
git add .
```

Commit

```bash
git commit -m "Initial commit"
```

Add remote

```bash
git remote add origin <repository-url>
```

Push

```bash
git push -u origin main
```

---

# Future Improvements

- Email Verification
- OTP Authentication
- Password Reset
- JWT Authentication
- Swagger Documentation
- REST API
- Wallet Integration
- Social Login
- Docker Support
- CI/CD Pipeline

---

# License

This project is open for educational and personal use.

---

# Author

**David Onyekachi**

Backend Developer

GitHub: https://github.com/onikageyoshi
