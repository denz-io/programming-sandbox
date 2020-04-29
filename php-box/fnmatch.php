<?php
    //allow fn to match with wildcard. 
    $unit = "7";
    $aspect = "test";
    $txt =  "7_test_1";
    if (fnmatch($unit . '_' . $aspect . '_' . '*',$txt)) {
        echo "We have a match";
    }
