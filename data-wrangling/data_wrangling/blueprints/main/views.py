from flask import Blueprint, request, url_for, redirect, render_template, flash
main = Blueprint('main', __name__, template_folder="templates/main")

@main.route("/")
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('layouts/404.html'), 404