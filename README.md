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
   ```

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

## Models

### User Model

The `User` model represents the user entity in the application and is responsible for handling authentication-related tasks such as password hashing and validation.

- **Fields**:
  - `id`: A unique identifier for each user.
  - `username`: The user's unique username, limited to 20 characters.
  - `email`: The user's unique email address, limited to 120 characters.
  - `password_hash`: A hashed version of the user's password for security purposes.

- **Methods**:
  - `set_password(password)`: Hashes the password using Flask-Bcrypt and stores it in the `password_hash` field.
  - `check_password(password)`: Validates a provided password against the stored password hash.
  - `__repr__()`: Returns a string representation of the `User` object for easier debugging.

### User Loader

The `load_user` function is used by Flask-Login to load a user from the database based on their user ID.

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

## Routes

### User Routes:
1. **Home**: `/home` — Renders the home page or the weather page if logged in.
2. **Register**: `/register` — Allows new users to register.
3. **Login**: `/login` — Authenticates users and logs them in.
4. **Logout**: `/logout` — Logs users out.
5. **Account**: `/account` — Allows users to update account info and change passwords.

### Weather Routes:
1. **Get Location**: `/get_location` — Fetches latitude and longitude of a given place.
2. **Weather Report**: `/weather_report` — Fetches and displays the weather report for the selected place.

### Utility Routes:
1. **Data Migration**: `/migrate-data` — Migrates and updates user data (for development).
