function manda(element){
const p = element.parentNode;
const par = p.querySelector("p").textContent;
const form= new FormData(); 
form.append("id",p.id);
form.append("Titolo",par);
fetch("EliminaC.php",{method:'POST',body:form});
window.location.replace("Home.php");
}