let registerForm = document.querySelector('form'); 

let API_URL_1 = 'http://localhost:5000/register'; 
let API_URL_2 = 'http://localhost:5000/loggedin'

let statusCode = -1; 


registerForm.addEventListener('submit', (event) =>{
    event.preventDefault(); 
    const registerData = new FormData(registerForm); 

    const email = registerData.get('email');   
    const password = registerData.get('password'); 
    const password2 = registerData.get('password2');

    registerForm.reset(); 

    const registerDatatoSend = {
        'email': email,
        'password': password,
        'password2': password2 
    }; 



    fetch(API_URL_1, {
        method: 'POST',
        body: JSON.stringify(registerDatatoSend),
        headers:{
            'content-type': 'application/json'
        }
    }).then(response => response.json())
        .then(registerResponse => {
            statusCode = registerResponse.code; 
            let message = registerResponse.message; 

            console.log(statusCode, message); 

            document.getElementById('create-message').innerHTML = message; 
            if(statusCode == 0){
                document.getElementById('alert-container').style.backgroundColor = 'rgb(241,15,15)'; 
            }
            else{
                document.getElementById('alert-container').style.backgroundColor = 'rgb(20, 187, 20)'; 
   
            }

            document.getElementById('alert-container').style.opacity = "100%";  

            if(statusCode == 1){
                window.location = 'http://localhost:5000/logged'; 
            }

        });

}); 



