// Define Variables
let langData1=document.getElementById('langdata-1')
let langData2=document.getElementById('langdata-2')
let word=document.getElementById('word')
let translateBtn=document.getElementById('tbtn')

translateBtn.onclick=()=>{
    translateWord(word.value)
}
function translateWord(w){
    let xhr=new XMLHttpRequest()
    url=`https://translate.yandex.net/api/v1.5/tr.json/translate?text=${w}&lang=${langData1.options[langData1.selectedIndex].value}-${langData2.options[langData2.selectedIndex].value}&key=trnsl.1.1.20200328T084758Z.eceb954fcde9ad30.6be819299efb83d4d00afe2d0de468198cc362a4`
    xhr.open('GET',url,true)

    xhr.onload=()=>{
        if(xhr.status==200){
            // newword=JSON.parse(xhr.responseText)
            document.getElementById('word2').innerHTML=xhr.responseText
        }
        else{
            console.log('tapilmadi')
        }
    }

    xhr.send()
}