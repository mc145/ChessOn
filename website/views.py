from flask import Blueprint, render_template, request, jsonify, flash 
import json 


views = Blueprint('views', __name__) 


@views.route('/')
def home():
    return render_template('home.html')
