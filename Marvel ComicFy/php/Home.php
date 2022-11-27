<?php
session_start();
if(!($_SESSION['Nickname'])){
    header("Location:accesso.php");
}
?>
<?php
if($_SESSION['Nickname']){
$conn = mysqli_connect( "localhost", "root","", "homework");

if (isset($_POST['nome'])){
    $immagine="606bd214518485383b59664f893c5222.jpg";
$utente=$_SESSION['Nickname'];
$nome=mysqli_real_escape_string($conn, $_POST['nome']); 
$query="INSERT into raccolta(imurl,Nome,IdU) VALUES('".$immagine."','".$nome."','".$utente."');";
$res=mysqli_query($conn,$query);
if($res == true){
    header("Location:Home.php");
    mysqli_free_result($res);
}
else {
    $errore = true;
}
mysqli_free_result($res);
mysqli_close($conn);

}
}
?>
<html>
<head>
<link rel="stylesheet" href="styleHome.css"/> 
<script src="eventiHome.js" defer="true" > </script>
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

</div>
<center><img class="gif"src="https://tenor.com/view/marvel-mcu-gif-14033563.gif"></center>
</header>
 
<section>
<p class ="welcome">Benvenuto: <?php echo $_SESSION['Nickname'] ?> </p>

<p class="int"> Crea la tua libreria: </p>
<center><img class="evento" src="scribd-marvel-partner-for-subscription-based-comic_a73r.640 (1).jpg"></center>
<div id="nascosto" class="hidden">
<p class="dim">Aggiungi una mensola</p>

<form method="POST">
<p>
<label class="dati">Inserisci il nome della mensola:</label> <input id="sez" type= "text" placeholder="Scaffale" name="nome" required/>
</p> 
<p><input type ="submit" value ="Aggiungi Scaffale" name="Aggiungi" class="bottone"/></p>
</form>
</div>
<p class="miei"> La tua collezione: </p>

<div class="contenitore">
<div id="Scaffali"></div>
</div>

</section> 
</body>
<a></a>
<footer></footer>
</html>