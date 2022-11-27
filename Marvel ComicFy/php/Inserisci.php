<?php
session_start();
if(isset($_POST['Titolo'])&&isset($_POST['Immagine'])&& isset($_POST['IDRaccolta'])){
$conn = mysqli_connect( "localhost", "root","", "homework");
$query = "INSERT into contenuto(Titolo,Immagine) values('".$_POST['Titolo']."','".$_POST['Immagine']."')";
$res=mysqli_query($conn, $query);
$query3="SELECT IdR,IdRac,IdCont FROM raccolta join rc on IDRaccolta=IdR where IdR='".$_POST['IDRaccolta']."'";
$re=mysqli_query($conn,$query3);
if(mysqli_num_rows($re)==0){
    $query4="UPDATE raccolta SET imurl = '".$_POST['Immagine']."' WHERE  IDRaccolta = '".$_POST['IDRaccolta']."'";
    $r=mysqli_query($conn,$query4);
}

$query2="INSERT into rc(IdR,IdRac,IdCont) values('".$_POST['IDRaccolta']."','".$_POST['TitoloRaccolta']."','".$_POST['Titolo']."')";
$result=mysqli_query($conn,$query2);


mysqli_close($conn);
}
?>
