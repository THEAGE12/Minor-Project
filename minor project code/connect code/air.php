<?php
$servername = "hostname";
$database = "databaseName";
$username = "user";
$password = "pass";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
}
 
echo "Connected successfully";
 
$sql = "INSERT INTO air (Air quality) VALUES ('".$_POST["air"]."')"; 
if (mysqli_query($conn, $sql)) {
      echo "New record created successfully";
} else {
      echo "Error: " . $sql . "
" . mysqli_error($conn);
}
mysqli_close($conn);
