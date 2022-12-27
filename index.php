<?php
// Get the user's input
$input = $_POST['input'];
 
// Set the file name
$file = 'input.txt';
 
// Write the data to the file
file_put_contents($file, $input);

// Get the path to the Python file
$python_file = '/path/to/file.py';
 
// Execute the Python file
exec('python '.$python_file);

?>
