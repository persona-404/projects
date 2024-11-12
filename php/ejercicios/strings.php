<?php

/**
 * @param String $str1
 * @param String $str2
 * @return String
 * 
 * Encontrar el comun denominador (el numero mayor que divide a ambos strings, mejor conocido como Euclid's algorithm - en su casa)
 */
function gcdOfStrings($str1, $str2) {
    /*
    if (substr_count($str1, $str2) < 1 && substr_count($str2, $str1) < 1) {
        return '';
    }

    if (strlen($str1) > strlen($str2) && substr_count($str1, ($str2 . $str2)) < 1) {
        return '';
    }

    if (substr_count($str1, $str2) > 1) {
        return $str2;
    }
    */

    if ($str1 . $str2 != $str2 . $str1) {
        return '';
    }

    //$toCheck = strlen($str1) > strlen($str2) ? $str2 : $str1;

    // find the largest set of chars that repeats in str2
    //$subStr      = '';
    //$finalStr    = '';
    //$moreRepeats = 0;
    /*for ($i = 0; $i <= (strlen($toCheck) - 1); $i++) {
        $subStr .= $toCheck[$i];
        
        $repeats = substr_count($toCheck, $subStr);
        if ($repeats >= $moreRepeats) {
            $moreRepeats = $repeats;
            $finalStr    = $subStr;
        }
    }*/
    $count = getGcd(strlen($str1), strlen($str2));
    return substr($str1, 0, $count);
    
    //return $finalStr;
}

function getGcd($num1, $num2) {
    if ($num2 == 0) {
        return $num1;
    }

    return getGcd($num2, ($num1 % $num2));
}

echo gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") . "\n"; //tauxx
echo gcdOfStrings("ABCABC", "ABC") . "\n"; // abc
echo gcdOfStrings("ABABAB", "ABAB") . "\n"; // ab
echo gcdOfStrings("CODE", "LEET") . "\n"; // empty
echo gcdOfStrings("ABCDEF", "ABC") . "\n"; // empty
echo gcdOfStrings("ABABCCABAB", "ABAB") . "\n"; // empty
echo gcdOfStrings("ABABABAB", "ABAB") . "\n"; // ab
echo getGcd(25, 45);