import sqlite3
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import json 


auth = Blueprint('auth', __name__) 



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.get_json()['email']
        password = request.get_json()['password']
        print(email, password) 

       
    return render_template('login.html')
    
@auth.route('/register', methods=['GET', 'POST']) 
def register(): 
    if request.method == 'POST': 
        email = request.get_json()['email']
        password = request.get_json()['password'] 
        password2 = request.get_json()['password2'] 


        if password != password2:
            response_message = {
                "code": 0,
                "message": "Passwords are not matching"
            }
            return json.dumps(response_message) 
        
        email_code = if_email_valid(email) 
        password_code = if_password_valid(password) 

        if email_code == False:
            response_message = {
                "code": 0, 
                "message": "Email is invalid"
            }
            return json.dumps(response_message) 
        elif password_code == False: 
            response_message = {
                "code": 0,
                "message": "Passwords must contain uppercase letters, lowercase letters, and numbers" 
            }
            return json.dumps(response_message)     
    
        elif check_if_user_exists(email) == True:
            #Make sure the email being used to sign up isn't already in use
            print("EXISTS", check_if_user_exists(email))
            response_message = {
                "code": 0, 
                "message": "This email is associated with an existing account. Please login to access your account" 

            }
            return json.dumps(response_message) 
        else:
            response_message = add_user(email, password) 
            return json.dumps(response_message) 
        
    else: 
        return render_template('register.html') 


@auth.route('/logged', methods=['POST', 'GET']) 
def logged(): 
    return render_template('logged.html')




def add_user(email, password): 
    try:
        with sqlite3.connect("/home/mc145/Programming/ChessOn/website/users.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO users (email, password) values (?, ?);
                """, (email, password,))
            result = {
                "code": 1,
                "message": "Account created successfully!"
            }
    except:
        result = {
            "code": 0,
            "message": "Database Error" 
        }
    return result 

def check_if_user_exists(email):
    with sqlite3.connect("/home/mc145/Programming/ChessOn/website/users.db") as connection:
        cursor = connection.cursor() 
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,)) 
        existing_email = cursor.fetchone() 
        if(existing_email):
            return True
        return False 



#For Signup

def if_email_valid(email):
    #[letters]@[domain].com
    has_at = False 
    has_dot = False 
    for char in email:
        if char == '@':
            has_at = True 
        elif char == '.':
            has_dot = True 
    
    
    if has_at == False or has_dot == False: 
        return False 
    else:
        return True 


def if_password_valid(password):
    # Check for capital letter, lowercase letter, number
    capital = False
    lowercase = False 
    number = False 
    for char in password:
        if char.isupper():
            capital = True 
        elif char.islower():
            lowercase = True 
        elif char.isdigit():
            number = True 
    
    if capital == False or lowercase == False or number == False:
        return False 
    else: 
        return True 



        
        
    
    



