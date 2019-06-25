<?php
    function recursiveInput()
    {
	$output = readline("Input Number: ");
	if ($output != 42) {
	   echo($output . "\n");
	   recursiveInput();
	}
    }
    recursiveInput();
?>
