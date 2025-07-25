

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('regBtn').addEventListener('click', function(event) {
        event.preventDefault();
        
        const fullName = document.getElementById('fullName').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        console.log(fullName, email, password);

        const data = {
            full_name: fullName,
            email: email,
            password: password,
            buisness_id: 0
        };

        sendHttpRequest('POST','http://localhost:3000/authAdapter', data).then(responseData => {
            console.log(responseData);
            if(responseData.statusCode.code == "SC000"){
                console.log('success');
                document.getElementById('tostMsg').style.display = 'block';
                document.getElementById('msg').textContent = responseData.message;

                let buisnessid = responseData.param.buisness_id;
                const status = responseData.param.status;

                localStorage.setItem('buisnessid', buisnessid);
                localStorage.setItem('status', status);

                window.location = "bmr/index.html";
                
            }
        }).catch(err => {
            console.log(err);
            if(err.statusCode.code == "F005"){
                document.getElementById('tostMsg').style.display = 'block';
                document.getElementById('msg').textContent = err.message;
                
            }

        });
    
    });
    console.log('Hello, world!');
    
});