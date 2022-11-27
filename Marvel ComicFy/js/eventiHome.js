
function Visualizza(event){
    const div= document.querySelector('#nascosto');
    div.classList.remove('hidden');
}
const image=document.querySelector('.evento');
image.addEventListener('click',Visualizza);


    fetch("VisualizzaScaffali.php").then(onResponse).then(onJson);
    
    
    function onResponse(response){
        return response.json();
    }
    
    function onJson(json){
        const lista =document.querySelector("#Scaffali");
        lista.innerHTML = ''; 
        for(gino of json){
            const new_div = document.createElement("div");
            const p = document.createElement("p");
            const new_img = document.createElement("img");
            const a = document.createElement("a");
            p.textContent = gino.Nome;
            a.classList.add("link");
            p.classList.add("raccogli");
            new_img.classList.add("imRac");
            a.setAttribute('href',"Contenuti.php?id="+gino.IDRaccolta);
            new_img.setAttribute('src', gino.imurl);
            a.appendChild(new_img);
            a.appendChild(p);
            new_div.appendChild(a);
            lista.appendChild(new_div);
           
            
        }
    }
function creazione_raccolta(){
var titolo=document.forms[""]["Nome"].value;
if(titolo === null || titolo === ""){
     alert("Compilare il campo");
        return false;
        }
    }
    
