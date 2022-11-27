<html>
<head>
<link rel="stylesheet" href="stylefisso.css"/>
<script src="verificadati.js" defer='true'></script>
  
</head>
 <body> 
<header>
  <nav>
<center><img class="Home" src="marvel-logo-card-1560x876_2.jpg"></center>
</nav>
</header>

<section>
      
<p class="inizio">Inserisci i tuoi dati.</p>
</p>
</center>
<div class="contenitore">
<form name ='regfile'action='Registrazione.php' method = 'post'onsubmit="return validazione()">
<p>
    <label class ="dati">Nome: <input type='text'placeholder="Nome" name='nome'required ></label>
    </p>
    <p>
    <label class="dati">Cognome: <input type='text'placeholder="Cognome" name='cognome'required></label>
    </p>
    <p> 
      <label class="dati"> Nickname:  <input id="Nick" type= 'text'placeholder="Nickname" name = 'Nickname'>
      </p>
      <center><span id="cont" class="hidden">Nickname già utilizzato.</span></center>
    <p>
    <label class="dati">E-mail: <input type='text' placeholder="E-mail"name='email'required></label>
    </p>
    <p>
      <label class="dati">Password: <input type='password'placeholder="Password" name='password'required></label>
    </p>
    <p>
      <label class="dati">Conferma Password: <input type='password'placeholder="Conferma" name='password2'required></label>
    </p>
    <p>
      <label class="bottone">&nbsp;<input type="submit" value= 'Prosegui'></label>
    </p>
  </form>
  </div>
  <?php
  session_start();
  if(isset($_SESSION["Nickname"]))
  {
    
    header("Location:Home.php");
    exit;
  }
$conn = mysqli_connect( "localhost", "root","", "homework");
if (isset($_POST['nome'])&& isset($_POST['cognome']) && isset($_POST['Nickname']) &&  isset($_POST['email']) && isset($_POST['password']) ) {
$nome = mysqli_real_escape_string($conn, $_POST['nome']);
$cognome = mysqli_real_escape_string($conn,$_POST['cognome']);
$nickname = mysqli_real_escape_string($conn,$_POST['Nickname']);
$email = mysqli_real_escape_string($conn, $_POST['email']);
$password = mysqli_real_escape_string($conn, $_POST['password']);
$password2= mysqli_real_escape_string($conn, $_POST['password2']);
$query2 ="SELECT Nickname from utente where Nickname = '".$nickname."'";
$result=mysqli_query($conn, $query2);

if(mysqli_num_rows($result) > 0){
  echo "vero";
}
else{
$query = "INSERT INTO utente(Nome,Cognome,Nickname,Email,Pswd) 
VALUES('".$nome."','".$cognome."','".$nickname."','".$email."', '".$password."');";
$res=mysqli_query($conn, $query);
if($res == true){
  $_SESSION['Nickname'] = $_POST['Nickname'];
  header("Location:home.php");
  exit;
}
mysqli_close($conn);
header('Location:accesso.php');
}   
}

?>
<center><img src="0d180cf154047d0e43b1b72656d68d3d.jpg"></center> 


</section>
<footer></footer>
</body>
</html>