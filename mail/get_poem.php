<?php
$servername = "localhost";
$username = "pubusr";
$password = "4@ZqSSj^9@LP#rU%";
$dbname = "employees";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT emp_no, first_name, last_name FROM employees LIMIT 10";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "Id: " . $row["emp_no"]. " - Name: " . $row["first_name"]. " " . $row["last_name"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();
?>