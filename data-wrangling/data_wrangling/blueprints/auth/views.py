from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
import json
import requests
from oauthlib.oauth2 import WebApplicationClient
from werkzeug.security import generate_password_hash, check_password_hash

from .models import Users
from constants import GOOGLE_DISCOVERY_URL, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from db.db import db


auth = Blueprint('auth', __name__, template_folder="templates/auth")
client = WebApplicationClient(GOOGLE_CLIENT_ID)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user_logging_in = Users.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user_logging_in or not check_password_hash(user_logging_in.password, password):
        flash('please check your login details and try again.')
        return redirect(url_for('auth.login'))
    # if the above check passes, then we know the user has the right credentials
    login_user(user_logging_in, remember=remember)
    return redirect(url_for('main.profile'))

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@auth.route('/login_with_google', methods=['POST'])
def login_with_google():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@auth.route("/login_with_google/callback")
def callback():
    # get authorization code and tokens from google
    code = request.args.get("code")  
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code   
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    client.parse_request_body_response(json.dumps(token_response.json()))

    # get user details from google
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # check email is verified by google
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    google_user = Users(
        id=unique_id, name=users_name, email=users_email
    )
    # if google user email is not already in db, insert user into db
    if not Users.query.filter_by(email=users_email).first():
        db.session.add(google_user)
        db.session.commit()

    login_user(google_user)
    return redirect(url_for("main.index"))


@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # if a user with the same email is found, redirect to signup page so user can try again
    existing_user = Users.query.filter_by(email=email).first()
    if existing_user: 
        flash('a user with that email address already exists')
        return redirect(url_for('auth.signup'))

    # add new user to the database
    new_user = Users(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))