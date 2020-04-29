<?php
    /**
     * Work in progress
     */

    function getPrime() {
        $input = readline("Input Number: ");
        $end_set = $input;
        $is_prime = false;

        for ($to_check = $input; $to_check <= $end_set; $to_check++) {
            if (isPrime($to_check)) {
                $is_prime = true;
                echo($to_check . "\n");
            }
        }

        if ($is_prime) {
             getPrime();  
        }
    }

    getPrime();

    function isPrime($number) {
        $setNumber = floor(sqrt($number));

        if ( $number == 2 || $number == 1 ) {
            return false;
        }

        for ( $compare  = 2 ; $compare <= $setNumber ; ++$compare ) {
            if ( $number % $compare == 0 ) {
                break;
            }
        }

        if( $setNumber == $compare-1 ) {
            return true;
        }

        return false;
    }
?>
