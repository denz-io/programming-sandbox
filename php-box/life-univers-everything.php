<?php
    /** Challenge:
      * Create a program that takes an input and prints it out as long as
      * input is not the number 42.
      */
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
