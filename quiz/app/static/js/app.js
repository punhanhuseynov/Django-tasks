let questcount = document.getElementsByClassName('question-div')
let questions = document.getElementsByClassName('variant')
let seeResultbtn = document.getElementById('resultBtn')

let notchecked = true
let trueanswer = 0
let falseanswer = 0
let failanswer=[]
let correctanswer=[]

seeResultbtn.onclick = () => {

   
    for (let i = 0; i < questions.length; i++) {

        if (questions[i].firstElementChild.checked) {

            if (questions[i].firstElementChild.parentElement.id == questions[i].parentNode.id) {
                
                trueanswer += 1
                correctanswer.push(
                    {
                        "question":questions[i].parentNode.parentNode.firstElementChild.firstElementChild.innerHTML,
                        "answer":questions[i].firstElementChild.parentElement.id,
                        
                        
                    }
                )
                

            }
            else if (questions[i].firstElementChild.parentElement.id != questions[i].parentNode.id){
                
                falseanswer += 1
                console.log(questions[i].firstElementChild.parentElement.id)
                
                failanswer.push(

                    {
                        "question":questions[i].parentNode.parentNode.firstElementChild.firstElementChild.innerHTML,
                        "answer":questions[i].firstElementChild.parentElement.id,
                        "correct":questions[i].parentNode.id
                        
                    }
                )


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
   

    window.location.href='/'
   

    

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
        "resultfail":failanswer,
        "resulttrue":correctanswer,
        "category_id":window.location.href.split('/')[window.location.href.split('/').length-1]
       
    }

    xhr.send(JSON.stringify(data));
    failanswer=[]
    correctanswer=[]

}
