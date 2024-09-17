# app/routes.py
from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify, session
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, UpdatePasswordForm
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required
import requests

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template('weather.html', title='map')
    return render_template('home.html')

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Change password to password_hash
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('weather.html', title='map')
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):  # Update to use 'password_hash'
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else render_template('weather.html', title='map')
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    
    return render_template('login.html', title='Login', form=form)


@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@main.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    password_form = UpdatePasswordForm()

    # Handle account updates (username, email)
    if form.validate_on_submit() and 'submit' in request.form:
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('main.account'))

    # Handle password change
    if password_form.validate_on_submit() and 'submit' in request.form:
        current_user.set_password(password_form.new_password.data)  # Use set_password
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('main.account'))

    # Populate the form fields with the current user's data on GET request
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', title='Account', form=form, password_form=password_form)

@main.route('/get_location', methods=['POST'])
@login_required
def get_location():
    data = request.get_json()
    place = data.get('place')
    session['place'] = place

    # Call the Meteosource API
    api_url = f"https://www.meteosource.com/api/v1/free/point?place_id={place}&sections=daily&timezone=auto&language=en&units=auto&key=x4r7nfopqo4fyp287xa6pq08fgbtyl7lxsuu9f1a"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        weather_data = response.json()
        lat = weather_data['lat'].rstrip("NS")
        lon = weather_data['lon'].rstrip("WE")
        return jsonify({"latitude": lat, "longitude": lon})
    else:
        return jsonify({"error": "Failed to fetch data from API"}), 400

@main.route('/weather_report', methods=['GET', 'POST'])
@login_required
def weather_report():
    place = session.get('place')

    # Call the Meteosource API
    api_url = f"https://www.meteosource.com/api/v1/free/point?place_id={place}&sections=daily&timezone=auto&language=en&units=auto&key=x4r7nfopqo4fyp287xa6pq08fgbtyl7lxsuu9f1a"
    response = requests.get(api_url)

    if response.status_code == 200:
        weather_data = response.json()

        # Extract the daily weather data
        daily_weather = weather_data['daily']['data']

        # Render the report page, passing the weather data
        return render_template('report.html', place=place, daily_weather=daily_weather)
    else:
        # Handle API error
        return f"Failed to fetch weather data for {place}", 400
    
@main.route('/migrate-data', methods=['GET'])
def migrate_data():
    from werkzeug.security import generate_password_hash
    users = User.query.all()
    for user in users:
        user.password_hash = generate_password_hash(user.password)
        db.session.add(user)
    db.session.commit()
    return 'Data migrated successfully!'