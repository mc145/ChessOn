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
        else:
            response_message = {
                "code": 1, 
                "message": "Account Successfully Made!" 
            }
            return json.dumps(response_message) 

        

        
    else: 
        return render_template('register.html') 


@auth.route('/logged', methods=['POST', 'GET']) 
def logged(): 
    return render_template('logged.html')





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
        
        
    
    



