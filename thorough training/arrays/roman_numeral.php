<?php

function romanToInt($s) {
    $values = [
        "I" => 1,
        "V" => 5,
        "X" => 10,
        "L" => 50,
        "C" => 100,
        "D" => 500,
        "M" => 1000
    ];

    $total = 0; 
    $length = strlen($s);  // Get the length of the string

    // Step 2: Loop through the string
    for ($i = 0; $i < $length; $i++) {
        $current_value = $values[$s[$i]];
        if ($i + 1 < $length) {
            $next_value = $values[$s[$i + 1]]; 
            if ($current_value < $next_value) {
                $total -= $current_value; 
            } else {
                $total += $current_value;  
            }
        } else {
            $total += $current_value;     
        }
    }

    return $total;
}
