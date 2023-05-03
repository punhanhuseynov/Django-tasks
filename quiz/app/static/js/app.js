let questcount = document.getElementsByClassName('question-div')
let questions = document.getElementsByClassName('variant')
let seeResultbtn = document.getElementById('resultBtn')

let notchecked = true
let trueanswer = 0
let falseanswer = 0

seeResultbtn.onclick = () => {

   
    for (let i = 0; i < questions.length; i++) {

        if (questions[i].firstElementChild.checked) {

            if (questions[i].firstElementChild.parentElement.id == questions[i].parentNode.id) {
                
                trueanswer += 1
            }
            else {
                
                falseanswer += 1

            }



        }
    }
    
    if(trueanswer==0 && falseanswer==0){

    }
    else{
        senddata()
        
        window.alert(`${questcount.length} sualdan ${trueanswer} dogru ${falseanswer} yanlisiniz oldu`)

    }

    
   
    trueanswer = 0
    falseanswer = 0

    window.location.replace('/');

    

}

function senddata(){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/add/', true);

    xhr.setRequestHeader('Content-Type', 'application/application/json');
    xhr.setRequestHeader('X-CSRFToken',document.getElementById('csrf').firstElementChild.value)
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(JSON.parse(xhr.responseText));
        }
        else{

        }
    };
    data={
        "true":trueanswer,
        "false":falseanswer,
        "category_id":window.location.href.split('/')[window.location.href.split('/').length-1]
       
    }
    xhr.send(JSON.stringify(data));

}
