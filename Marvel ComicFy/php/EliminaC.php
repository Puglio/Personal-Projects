<?php
if(isset($_POST['id']) && isset($_POST['Titolo'])){
    $conn = mysqli_connect( "localhost", "root","", "homework");
  
    $query2 ="DELETE FROM rc WHERE IdCont = '".$_POST['Titolo']."' AND IdR='".$_POST['id']."'";
    $res=mysqli_query($conn,$query2);
    $query="SELECT IdCont from rc JOIN contenuto on IdCont=Titolo WHERE Titolo='".$_POST['Titolo']."'";
    $r=mysqli_query($conn,$query);
    if(mysqli_num_rows($r)==0){
        $immagine="606bd214518485383b59664f893c5222.jpg";
       $query3="DELETE FROM contenuto WHERE Titolo ='".$_POST['Titolo']."'";
       $re=mysqli_query($conn,$query3);
       $query4="UPDATE raccolta SET imurl = '".$immagine."' WHERE IDRaccolta = '".$_POST['id']."'"; 
       $resetta=mysqli_query($conn,$query4);
      
    }
    mysqli_close($conn);
    

}
?>