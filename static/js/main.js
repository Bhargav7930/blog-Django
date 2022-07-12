



function login(){
    var username =document.getElementById('username').value;
    var password =document.getElementById('password').value;
    var csrf = document.getElementById('csrf').value;

    if (username=="" & password==""){
        alert("you must enter both")
    }

    var data = {
        "username":username,
        "password":password
    }

    fetch('/api/login/',{
        method:'POST',
        headers :{
            'Content-Type':'application/json; charset=UTF-8',
            'X-CSRF Token': csrf,
        },
        
        'body':JSON.stringify(data)
    }).then(result=>result.json())
    .then(response=>{
        if(response.status == 200){
            window.location.href="/"
        }
        else{
            alert(response.message)
        }
    })

}