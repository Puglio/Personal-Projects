<?php
session_start();
session_destroy();
header("Location: accesso.php");
exit;
?>