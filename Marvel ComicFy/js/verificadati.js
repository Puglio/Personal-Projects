function validazione()
{
    var nome=document.forms["regfile"]["nome"].value;
    var cognome=document.forms["regfile"]["cognome"].value;
    var nickname=document.forms["regfile"]["Nickname"].value;
    var email=document.forms["regfile"]["email"].value;
    var password=document.forms["regfile"]["password"].value;
    var password2=document.forms["regfile"]["password2"].value;
    var email_reg_exp = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-]{2,})+.)+([a-zA-Z0-9]{2,})+$/;
    
    if(nome === null || nome===""|| cognome === null ||cognome===""|| nickname === null ||nickname ==="" || email === null ||email===""|| password === null ||password===""|| password2 === null||password2===""){
    alert("Compilare tutti i campi.");
    return false;
    }
    else if(password != password2){
        alert("Le password devono combaciare.");
    return false;
}
else if (!email_reg_exp.test(email) || (email == "") || (email == "undefined")) {
    alert("Inserire la '@' nel campo E-mail.");
    return false;
 }
}
const nickk = document.querySelector("#Nick");
nickk.addEventListener('blur',nick);

function nick(){

    const text = document.getElementsByTagName("input")[2].value;
    const formData= new FormData();
    formData.append("Nickname",text);
    fetch("ControlloNick.php",{method:'POST',body:formData}).then(onResponse).then(onText);
}
function onText(text)
{
    var span= document.querySelector("#cont");
    if(text==="vero"){
        span.classList.remove("hidden");
    }
    else{
        if(!(span.classList.contains("hidden"))){
            span.classList.add("hidden");
        }
    }
}

function onResponse(response)
{
return response.text();
}



