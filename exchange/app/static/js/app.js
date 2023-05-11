// Variables

let excBtn=document.getElementById('exchangeBtn')

let currency1=document.getElementById('firstCurrency')

let currency2=document.getElementById('secondCurrency')

excBtn.onclick=()=>{
    exchangeCurrency()
}

function exchangeCurrency(){
   

    let xhr=new XMLHttpRequest()
    url=`https://api.fastforex.io/convert?from=${currency1.options[currency1.selectedIndex].value}&to=${currency2.options[currency2.selectedIndex].value}&amount=${document.getElementById('numValue').value}.0&api_key=YOUR_API_KEY`
    xhr.open('GET',url,true)

    xhr.onload=()=>{
        if(xhr.status==200){
            newword=JSON.parse(xhr.responseText)
            a=currency2.options[currency2.selectedIndex].value
            console.log(a)
            document.getElementById('num2').value=newword.result[a]
            console.log(newword)
        }
        else{
            console.log('tapilmadi')
        }
    }

    xhr.send()


}