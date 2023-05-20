let submit_btn=document.getElementById('submitBtn')
let username=document.getElementById('username')
let password=document.getElementById('password')
let csrftoken=document.getElementsByName('csrfmiddlewaretoken')[0].value
let alertmodel=document.getElementById('error_card')
let loginrow=document.getElementById('loginrow')
let userrow=document.getElementById('userrow')

submit_btn.addEventListener('click',()=>{
    sendLogin(username.value,password.value)

})

function sendLogin(username,password){
  
    
    let xhr=new XMLHttpRequest()
    let url='http://localhost:8000/userlogin/'
    xhr.open('POST',url,true)
    xhr.setRequestHeader("X-CSRFToken", csrftoken); 
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.onload=()=>{
        data=JSON.parse(xhr.responseText)
        if(data.message=='fill'){
            alertmodel.innerHTML=`
            <div class="alert alert-warning d-flex align-items-center" role="alert">
          
            <div>
              Zəhmət olmasa xanaları doldurun
            </div>
          </div>`
        }
        if(data.message=='wrongusername'){
            alertmodel.innerHTML=`
            <div class="alert alert-danger d-flex align-items-center" role="alert">
          
            <div>
              Istifadəçi adı vəya şifrə yanlışdır
            </div>
          </div>`
        }

        if(data.message=='welcome'){
            userrow.style.height='100%'
            loginrow.style.height='0%'
            alertmodel.innerHTML=`
            <div class="alert alert-success d-flex align-items-center" role="alert">
          
            <div>
              Xoş gəlmisiniz
            </div>
          </div>`
        }

    }

    data={
        "username":username,
        "password":password
    }

    xhr.send(JSON.stringify(data))

}

