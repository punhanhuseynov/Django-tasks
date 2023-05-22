let submit_btn=document.getElementById('subbtn')
let username=document.getElementById('username')
let password=document.getElementById('password')
let email=document.getElementById('email')
let names=document.getElementById('name')
let surname=document.getElementById('surname')

let csrftoken=document.getElementsByName('csrfmiddlewaretoken')[0].value
let alertmodel=document.getElementById('error_card')

submit_btn.addEventListener('click',()=>{
    sendLogin(username.value,password.value,email.value,names.value,surname.value)

})

function sendLogin(username,password,email,fname,surname){
  
    
    let xhr=new XMLHttpRequest()
    let url='http://localhost:8000/userregister/'
    xhr.open('POST',url,true)
    xhr.setRequestHeader("X-CSRFToken", csrftoken); 
    xhr.setRequestHeader("Content-Type", "application/json")
   
    xhr.onload=()=>{
        data=JSON.parse(xhr.responseText)
        console.log(data)
        if(data.message=='created'){
           
            document.body.innerHTML=`
            <div class="container">
  <div class="row d-flex justify-content-center">
    <h2>Elektron Poçtunuza gələn mesaj ilə hesabınızı təsdiqləyin </h2>
  </div>
</div>
            `
        }
        
        
    }

    data={
        "username":username,
        "password":password,
        "email":email,
        "first_name":fname,
        "last_name":surname
      
    }
    
    xhr.send(JSON.stringify(data))

}
