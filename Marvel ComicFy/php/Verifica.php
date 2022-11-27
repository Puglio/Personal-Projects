<?php
session_start();

$conn = mysqli_connect( "localhost", "root","", "homework");
$query = "SELECT Titolo,Immagine FROM ((contenuto as c join rc as r on c.Titolo=r.IdCont )join raccolta as ra on r.IdRac = ra.Nome) where ra.Nome='".$_GET['id']."'";
$result=mysqli_query($conn,$query);
$i=mysqli_num_rows($result);
$gino=array();
if($i>0){   
while($row=mysqli_fetch_assoc($result)){
    $gino[]=$row;
}
mysqli_free_result($result);
}
else{
    exit;
}
mysqli_close($conn);
echo json_encode($gino);
header("Location:Contenuti.php");
?>