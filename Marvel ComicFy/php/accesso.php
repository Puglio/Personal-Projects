

<html>
<head>
<link rel="stylesheet" href="stylefisso.css"/>
<script src="verificadati.js"></script>
</head>
<body> 

<header>
	<nav>
<center><img class="Home" src="marvel-logo-card-1560x876_2.jpg"></center>
</nav>
</header>
<section>
<p class="inizio">Benvenuto nell'universo Marvel.</p>
<p class="accesso">Accedi o registrati per sfogliare e comporre la tua personale raccolta di fumetti.</p>
<br>
<br>

<div class="contenitore">
<FORM method='POST'>
<p><label class="dati"> Nickname:  <input type="text"placeholder="Nickname" name="Nickname" required> </label></p>
<p><label class="dati">  Password:  <input type="password"placeholder="Password" name="Password"required></label></p>
<label class="bottone"><input type="submit" value="Accedi"/></label>
<?php
session_start();
if(isset($_SESSION["Nickname"]))
{
	
	header("Location:Home.php");
	exit;
}
if(isset($_POST["Nickname"]) && isset($_POST["Password"])){
	$conn = mysqli_connect("localhost","root" , "", "homework");
	if(! $conn){
		echo "Errore durante la connessione a MySQL.";
		exit();
		}
		$nickname = mysqli_real_escape_string($conn,$_POST["Nickname"]);
		$password = mysqli_real_escape_string($conn,$_POST["Password"]);
		$res = mysqli_query($conn, "SELECT * FROM utente WHERE Nickname = '".$nickname."' 
		AND Pswd = '".$password."'");
		if (mysqli_num_rows($res)>0){
			$_SESSION["Nickname"]=$nickname;
			mysqli_close($conn);
			header("Location:Home.php");
			exit();
		}
		else {
		echo "<p> Credenziali non valide </p>";
		}
}
?>
</FORM>
</div>

<p class="registrazione">Non sei ancora registrato?<a href="Registrazione.php">Clicca qui</a>per effettuare la registrazione.</p>
<center><img src="download.jpg"></center>
<br>
<br>
</section>
<footer></footer>
</body>


</html>