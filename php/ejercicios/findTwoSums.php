<?php

function twoSum($nums, $target) {
    for ($i = 0; $i < count($nums); $i++) {
        for ($j = ($i + 1); $j < count($nums); $j++) {
            if ($nums[$i] + $nums[$j] == $target) {
                return [$i, $j];
            }
        }
    }
}

var_dump(twoSum([2,5,5,11], 10));