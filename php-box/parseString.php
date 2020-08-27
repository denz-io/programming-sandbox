<?php
    $stringToParse = "3 Bed, 2.5 Bath";
    $re = '/[\d.]+ ([A-Z]{1})/';
    preg_match_all($re, $stringToParse, $matches, PREG_SET_ORDER, 0);
    $description = "";
    foreach ($matches as $match) {
        $description .= str_replace(" ","",$match[0]);
    }
    echo $description;
?>
