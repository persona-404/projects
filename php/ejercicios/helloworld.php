<?php

function romanToInt($s) {
    $values = [
        'I' => 1, 'V' => 5, 'X' => 10, 'L' => 50, 'C' => 100, 'D' => 500, 'M' => 1000
    ];
        
    $prev = '';
    $count = 0;
    $arrString = str_split($s);
    foreach ($arrString as $letter) {
        $count += $values[$letter];

        if (empty($prev)) {
            $prev = $letter;
            continue;
        }
        
        if ($values[$letter] > $values[$prev]) {
            $count -= $values[$prev];
            $count -= $values[$prev];
        }

        $prev = $letter;
    }
    
    return $count;
}

$s = 'XXXIII';
echo romanToInt($s);
        
?>