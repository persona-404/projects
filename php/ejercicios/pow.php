<?php

function myPow($x, $n) {
    if ($n == 0) {
        return 1;
    }

    $tempn = $n;
    if ($n < 0) {
        $n = abs($n);
    }

    $res = 1;
    while ($n) {
        if ($n % 2) {
            $res *= $x;
            $n -= 1;
        } else {
            $x *= $x;
            $n = intdiv($n, 2);
        }
    }
    
    if ($tempn < 0) {
        $res = 1 / $res;
    }

    return $res;
}

echo myPow(2, 10);