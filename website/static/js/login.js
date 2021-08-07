let loginForm = document.querySelector('form'); 

let API_URL = 'http://localhost:5000/login'; 


loginForm.addEventListener('submit', (event) =>{
    event.preventDefault(); 
    const loginData = new FormData(loginForm); 

    const email = loginData.get('email');   
    const password = loginData.get('password'); 

    loginForm.reset(); 

    const loginDatatoSend = {
        'email': email,
        'password': password
    }; 


    fetch(API_URL, {
        method: 'POST',
        body: JSON.stringify(loginDatatoSend),
        headers:{
            'content-type': 'application/json'
        }
    })
    .then(response => response.json())
        .then(loginResponse =>{

            statusCode = loginResponse.code; 
            let message = loginResponse.message; 

            console.log(statusCode, message); 

            document.getElementById('create-message').innerHTML = message; 
            if(statusCode == 0){
                document.getElementById('alert-container').style.backgroundColor = 'rgb(241,15,15)'; 
            }
            else{
                document.getElementById('alert-container').style.backgroundColor = 'rgb(20, 187, 20)'; 
   
            }

            document.getElementById('alert-container').style.opacity = "100%";  
        });

}); 