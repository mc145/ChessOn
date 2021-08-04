from flask import Blueprint, render_template, request, jsonify, flash 
from flask_login import login_required, current_user 
import json 


views = Blueprint('views', __name__) 


@views.route('/')
def home():
    return render_template('home.html')
