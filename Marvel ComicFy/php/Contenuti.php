<?php
session_start();
if(!(isset($_SESSION['Nickname']))){
    header("Location:accesso.php");
}
?>

<html>
<head>
<link rel="stylesheet" href="styleContenuti.css"/> 
<script src="eventiContenuti.js" defer='true' > </script>

</head>
<body>  
<header>
<nav> 
<center><nav class ="Home"><img  src="marvel-logo-card-1560x876_2.jpg"></button></center></nav>
 
<div class="allinea">
<ul id="menu">    
<li><a href="Home.php">Home</a></li>
<li><a href="IRicerca.php">Ricerca </a></li>
<li><a href="Logout.php">Logout</a></li>
</ul>
<center><img class="gif"src="https://tenor.com/view/marvel-mcu-gif-14033563.gif"></center>
</div>
<section>

<center><p class="tuoi">I tuoi FUMETTI: </p></center>
<div id="Inserisci" class='contenitore'>
<div class='cont'>
<?php
if(isset($_SESSION['Nickname'])){
if(isset($_GET['id'])){
$conn = mysqli_connect( "localhost", "root","", "homework");
$query = "SELECT IdR,Titolo,Immagine FROM ((contenuto as c join rc as r on c.Titolo=r.IdCont )join raccolta as ra on r.IdR = ra.IDRaccolta) where ra.IDRaccolta='".$_GET['id']."'";
$result=mysqli_query($conn,$query);
$i=mysqli_num_rows($result);
$figlio=array();
if($i>0){   
    while($row = mysqli_fetch_object($result)){

        echo "<div id = ".$row->IdR." class='contenuto'>
        <img class='imgC' src = ".$row->Immagine." >
        <p id='titolo' class='titolo'>".$row->Titolo."</p>
        <button class='bottoneC' onClick='manda(this);'class='elimina'> Elimina fumetto. </button> 
        </div>";
        
        
        
}
}
else{
    exit;
}
mysqli_free_result($result);
mysqli_close($conn);

}
}
?>
</div>
</div>
<div id="modal" class = "hidden"></div>
</section>
</body>
</html>