from flask import Blueprint, render_template, request, jsonify, flash, url_for, redirect, abort  
import json 
import sqlite3 


views = Blueprint('views', __name__) 


@views.route('/', methods=['GET']) 
def home():

    # email = request.args.get('email') 
    # password = request.args.get('password') 
    # if email and password:
    #     user_exists = user_login_check(email, password)
    #     print("VIEWS", email, password, user_exists, check_session_true(email)) 
    #     if user_exists and check_session_true(email):
    #         print("LOGGED HELLO")
    #         return render_template('logged.html') 

    return render_template('home.html')




def user_login_check(email, password): 
    with sqlite3.connect("/home/mc145/Programming/ChessOn/website/users.db") as connection:
        cursor = connection.cursor() 
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_email = cursor.fetchone() 
        if existing_email and existing_email[-1] == password:
            return True 
        return False 

def check_session_true(email): 
    with sqlite3.connect("/home/mc145/Programming/ChessOn/website/users.db") as connection:
        cursor = connection.cursor() 
        cursor.execute("SELECT * FROM session where email = ?", (email,)) 
        user_session = cursor.fetchone() 
        if user_session[-1] == 1: 
            return True 
        return False 
