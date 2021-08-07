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
        account_exists = user_login_check(email, password) 
        print("ACCOUNT EXISTS", account_exists) 
        if account_exists: 
            result = login_user(email) 
            print("LOGIN USER", result) 

            return redirect(url_for('views.home'))
          

        else:
            response_message = {
                "code": 0, 
                "message": "Account doesn't exist" 
            }
            return json.dumps(response_message) 

       
    return render_template('login.html')
   # return redirect(url_for('views.home'))


    
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
            response_message_2 = add_user_session(email) 
            print(response_message_2) 
            return json.dumps(response_message) 
        
    else: 
        return render_template('register.html') 






def login_user(email): 
    try: 
        with sqlite3.connect("/home/mc145/Programming/ChessOn/website/users.db") as connection:
            cursor = connection.cursor() 
            cursor.execute("SELECT * FROM session WHERE email = ?", (email,)) 
            session_user = cursor.fetchone() 
            session_id = session_user[0]
            cursor.execute("UPDATE session SET email = ?, status = ? WHERE ID = ?;", (email, 1, session_id)) 
            result = 'Session updated' 
    except: 
            result = 'Session updating error'
    return result 



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

def add_user_session(email):
    try: 
        with sqlite3.connect("/home/mc145/Programming/ChessOn/website/users.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO session (email, status) values (?, ?);    
            """, (email, 0,))
            result = 'user session inserted'
    except: 
        result = 'error'
    return result 

def check_if_user_exists(email):
    with sqlite3.connect("/home/mc145/Programming/ChessOn/website/users.db") as connection:
        cursor = connection.cursor() 
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,)) 
        existing_email = cursor.fetchone() 
        if existing_email:
            return True
        return False 

def user_login_check(email, password): 
    with sqlite3.connect("/home/mc145/Programming/ChessOn/website/users.db") as connection:
        cursor = connection.cursor() 
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_email = cursor.fetchone() 
        print("EXISTING EMAIL", existing_email)
        if existing_email and existing_email[-1] == password:
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



        
        
    
    



