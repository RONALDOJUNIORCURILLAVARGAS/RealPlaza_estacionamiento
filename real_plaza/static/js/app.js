
const  form_toggle = document.querySelector('#form_toggle');
const form_ = document.querySelector('#form_');


form_toggle.style.visibility ='visible';
form_.style.visibility ='hidden';    
form_toggle.style.marginTop ='-700px';
function cambio(){

    form_.style.visibility ='hidden';
    form_toggle.style.visibility ='visible';  
}
function cambio2(){
    form_.style.visibility ='visible';
    form_toggle.style.visibility ='hidden'; 
}
