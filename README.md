# Portfolio_Project
This is an ALX specialization portfolio project in backend Software Engineering

# Flask App

This is a Flask web application that demonstrates a basic setup with user authentication, database management, and blueprint organization.

## Features

- **User Authentication**: Handles user login and session management using Flask-Login.
- **Database Management**: Uses SQLAlchemy for ORM and Flask-Migrate for database migrations.
- **Password Security**: Employs Flask-Bcrypt for password hashing.
- **Blueprints**: Modular design with blueprints to organize routes.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Login
- Flask-Migrate

You can install the required packages using pip:
```bash
pip install flask flask-sqlalchemy flask-bcrypt flask-login flask-migrate
```
## `app.py`

This file serves as the entry point for running the Flask application.

### How It Works

1. **Import the Application Factory**:
   
   ```python
   from app import create_app


