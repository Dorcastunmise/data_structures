<?php
class Solution {

    /**
     * @param String[] $words
     * @param String $order
     * @return Boolean
     */
    function isAlienSorted($words, $order) {
        $rank = [];

        for($i = 0; $i < strlen($order); $i++) {
            $rank[$order[$i]] = $i;
        }

        for($w = 0; $w < count($words) - 1; $w++) {
            $current_word = $words[$w];
            $next_word = $words[$w + 1];

            $currlength = strlen($current_word);
            $nextlength = strlen($next_word);
            $minlength = min($currlength, $nextlength);

            for($minword = 0; $minword < $minlength; $minword++) {
                $frstletter = $current_word[$minword];
                $nextletter = $next_word[$minword];

                if($rank[$frstletter] < $rank[$nextletter]) {
                    break;
                } elseif($rank[$frstletter] > $rank[$nextletter]) {
                    return false;
                }
            }

            if(($minword == $minlength) && ($currlength > $nextlength)) {
                return false;
            }
        }

        return true;
    }
}