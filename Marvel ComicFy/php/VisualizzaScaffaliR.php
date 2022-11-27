<?php
session_start();
$conn2 = mysqli_connect( "localhost", "root","", "homework");
$query2 = "SELECT IDRaccolta,Nome FROM raccolta where IdU = '".$_SESSION['Nickname']."'";
$result = mysqli_query($conn2,$query2);
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
mysqli_close($conn2);
echo jSon_encode($gino);
?>