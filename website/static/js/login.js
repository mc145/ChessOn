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
    });

}); 