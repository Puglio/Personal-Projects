<?php
session_start();
if(isset($_POST['vai'])){
$clientkey="d0d5cb723624992732d2e584bc3654e3";
$hash="4a43c671811450c659f37a398185b66f";
$curl = curl_init();
$data = http_build_query(array("ts" => 1, "title" => $_POST["vai"], "apikey" => $clientkey, "hash" => $hash));
curl_setopt($curl, CURLOPT_URL,"http://gateway.marvel.com/v1/public/comics?".$data);
curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);

$result = curl_exec($curl);
echo json_encode($result);
curl_close($curl);
}
?>
