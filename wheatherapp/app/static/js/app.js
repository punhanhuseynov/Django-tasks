let subbtn=document.getElementById('subbtn')
let city_name=document.getElementById('cityname')
let resultcard=document.getElementById('result')
subbtn.onclick=()=>{
    getWhet(city_name.value)
}

function getWhet(cityname){
    let xhr=new XMLHttpRequest
    let url=`https://api.openweathermap.org/data/2.5/weather?q=${cityname}&appid=YOUR_API_KEY`

    xhr.open('GET',url,true)

  

    xhr.onload=()=>{
       data=JSON.parse(xhr.responseText)
    // data=xhr.responseText
      
    
       resultcard.innerHTML=`
       <h2>${data.name}</h2>
       <hr>
       <p>Country<h3>${data.sys.country}</h3></p>
       <hr>
       <p> Weather<h3>${data.main.temp}° ${data.weather[0].main} <img  style='background-color:#5a57f7; border-radius:15px'src='https://openweathermap.org/img/wn/${data.weather[0].icon}.png' /></h3></p>
        <p>Type <h3>${data.weather[0].description}</h3></p>
       `
       
    }
    xhr.send()
}