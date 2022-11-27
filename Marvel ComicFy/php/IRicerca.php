<?php
session_start();
if(!(isset($_SESSION['Nickname']))){
    header("Location:accesso.php");
}
?>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" href="styleRicerca.css"/> 
        <script src="eventiApi.js" defer ='true'></script>
  
    </head>
    <header> <nav> 
<center><nav class ="Home"><img  src="marvel-logo-card-1560x876_2.jpg"></button></center>
</nav>
<ul id="menu">
<li><a href="Home.php">Home</a></li>
<li><a href="IRicerca.php">Ricerca </a></li>
<li><a href="Logout.php">Logout</a></li>
<ul>

</header>

    <body>
    <section class="Ric">
    <div id="cover">
    <form name = "abc" method ="POST">
    <div class="tb">
    <div class="td">
    <label class="dati"></label> <input type= "text" placeholder="Ricerca.." name="vai" required/>
    </div>
      <div class="td" id="s-cover">
    <button type ="submit" value ="Ricerca" name="Aggiungi" class="bottone">
    <div id="s-circle"></div>
    <span></span>
</button>
</div>
</div>
    </form>
    <div class = "Bonobi"></div>
</div>
<div id="modal" class = "hidden"></div>
<div id="dio"></div>

</section>
    <footer></footer>
    </body>
</html>