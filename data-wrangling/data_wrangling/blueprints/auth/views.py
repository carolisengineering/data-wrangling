from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from db.db import db

auth = Blueprint('auth', __name__, template_folder="templates/auth")


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('please check your login details and try again.')
        return redirect(url_for('auth.login'))
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # if a user with the same email is found, redirect to signup page so user can try again
    existing_user = User.query.filter_by(email=email).first()
    if existing_user: 
        flash('a user with that email address already exists')
        return redirect(url_for('auth.signup'))

    # add new user to the database
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return 'Logout'