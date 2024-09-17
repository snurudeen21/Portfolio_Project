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
   from app import create_app ```

## Forms

The application uses **Flask-WTF** for handling forms and form validation. Below is a summary of the forms available:

1. **RegistrationForm**:
   - Fields: `username`, `email`, `password`, `confirm_password`
   - Custom validation ensures unique usernames and emails during registration.

2. **LoginForm**:
   - Fields: `email`, `password`, `remember`
   - Used for logging in users.

3. **UpdateAccountForm**:
   - Fields: `username`, `email`
   - Allows users to update their account information.
   - Custom validation ensures that updated usernames and emails are unique.

4. **UpdatePasswordForm**:
   - Fields: `current_password`, `new_password`, `confirm_password`
   - Used for changing the user's password.
   - Custom validation ensures that the current password is correct before allowing a password change.

### Notes:
- All form data is validated before being processed.
- Custom validators are implemented to ensure that usernames and emails remain unique in the database.




