<?php
session_start();
if(isset($_POST['Nickname'])){
$conn2=mysqli_connect("localhost", "root","", "homework");
$nick = mysqli_real_escape_string($conn2,$_POST['Nickname']);
$query2 ="SELECT Nickname from utente where Nickname = '".$nick."'";
$result=mysqli_query($conn2,$query2);
if(mysqli_num_rows($result) > 0){
  echo "vero";
}
mysqli_free_result($result);
mysqli_close($conn2);
}
?>