function manda(){
    event.preventDefault();
    const formdata= new FormData();
    var lugozzi = document.forms["abc"]["vai"].value;
    formdata.append("vai",lugozzi);
    fetch("Ricerca.php",{method:'POST',body: formdata}).then(onResponse).then(Visualizza);
}
const bottone = document.querySelector(".bottone");
bottone.addEventListener('click',manda);

function onResponse(response){
    return response.json(); 
}
function Visualizza(json){
   const js_ob= JSON.parse(json);
    const add_url ="/portrait_uncanny.jpg";
    const lista = document.querySelector(".Bonobi");
    lista.innerHTML='';
    if(js_ob.data.count>0){
        for(const ris of js_ob.data.results){
            const titolo = ris["title"];
            const img = ris.thumbnail.path+add_url;
            const descrizione = ris["description"];
            const new_div = document.createElement("div");
            const new_p = document.createElement("p");
            const new_img = document.createElement("img");
            const buttonA = document.createElement("button");
            const divB = document.createElement("div");
            divB.classList.add("sezBottone");
            new_div.classList.add("sezstampa");
            new_p.textContent = titolo;
            const nomeB = "Aggiungi ad una mensola";
            buttonA.textContent = nomeB;
            new_img.setAttribute('src', img);
            new_div.appendChild(new_img);
            new_div.appendChild(new_p);
            divB.appendChild(buttonA);
            lista.appendChild(new_div);
            lista.appendChild(divB);
            new_img.classList.add("Fumetto");
            new_div.classList.add("disposizione");
            buttonA.classList.add("Aggiungi");
            new_p.classList.add("nomeF");
            buttonA.addEventListener('click',function(){fetch("VisualizzaScaffaliR.php").then(risposta).then(function(json){
                    const vediamo = document.querySelector("#modal");
                    const seleziona = document.createElement("p");
                    seleziona.textContent = "Scegli la raccolta in cui vuoi inserire il fumetto";
                    vediamo.appendChild(seleziona);
                    seleziona.classList.add("vedilo");
                    for(gino of json){
                        const divV = document.createElement("div");
                        
                        const buttonV = document.createElement("button");
                        divV.classList.add("sezioneNomi");
                        buttonV.classList.add("BottoneSelezione");
                        seleziona.classList.add("SelezionaR");
                      
                        buttonV.textContent = gino.Nome;
                        const id = gino.IDRaccolta;
                        divV.appendChild(buttonV);
                        vediamo.appendChild(divV);
                        
                        vediamo.classList.remove('hidden');
                        vediamo.scrollIntoView();
                        buttonV.addEventListener('click',function(){
                            const dati = new FormData();
                            dati.append("Titolo",titolo);
                            dati.append("Immagine",img);
                            dati.append("IDRaccolta",id);
                            dati.append("TitoloRaccolta",buttonV.textContent);
                            fetch("Inserisci.php",{method:'POST',body:dati});
                        
                })
            }
            })
        })
        

            
            
            new_div.addEventListener('click', function(){
            const appendilo = document.querySelector("#modal");
            const immagine = document.createElement('img');
            const p = document.createElement('p');
            const d = document.createElement('div');
            
            immagine.classList.add("vicino");
            p.classList.add("descrizione");
            d.classList.add("Vediamo");
            immagine.setAttribute('src',img);
            p.textContent = descrizione;
            d.appendChild(p);
            d.appendChild(immagine);
            appendilo.appendChild(d);
            appendilo.classList.remove('hidden');
            appendilo.scrollIntoView();
        })
      

    }
  } 
    
}   
const modal = document.querySelector("#modal");
modal.addEventListener('click', onClick);

function onClick(){
    modal.classList.add('hidden');
    modal.innerHTML = '';
}
function risposta(response){
    return response.json(); 
}





