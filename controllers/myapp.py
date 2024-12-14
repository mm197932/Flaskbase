from flask import Blueprint, render_template, request, redirect

myapp = Blueprint("myapp", __name__, url_prefix='/myapp')

@myapp.route('/')
def index():
    return render_template('myapp/index.html')