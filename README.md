# Django Project Setup Guide

This repository contains the initial setup for a Django web application, including virtual environment creation, project scaffolding, and a starter app named `LittleLemon`.

---

## ✅ Step 1: Create Virtual Environment

```bash
python -m venv env
```

## ✅ Step 2: Activate Virtual Environment

  
  ```bash
  env\Scripts\activate
  ```


## ✅ Step 3: Install Django

```bash
pip install django
```

## ✅ Step 4: Create Django Project

```bash
django-admin startproject projectname .
```

> The `.` at the end ensures files are created in the current directory.

## ✅ Step 5: Start a New App

```bash
python manage.py startapp LittleLemon
```

> Replace `LittleLemon` with your desired app name.

## ✅ Step 6: Register App in `settings.py`

In your `projectname/settings.py` file, add the app name to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'LittleLemon',
]
```

## ✅ Step 7: Make Migrations

```bash
python manage.py makemigrations
```

## ✅ Step 8: Apply Migrations

```bash
python manage.py migrate
```

## ✅ Step 9: Run the Development Server

```bash
python manage.py runserver
```

> Visit `http://127.0.0.1:8000/` in your browser to view your running Django project.

---

## 🎉 You're All Set!
