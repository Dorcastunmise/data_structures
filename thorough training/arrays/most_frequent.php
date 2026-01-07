class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function topKFrequent($nums, $k) {
        $freq = [];

        foreach($nums as $num) {
            if(isset($freq[$num])) {
                $freq[$num]++;
            } else {
                $freq[$num] = 1;
            }
        } 

        $heap = new SplPriorityQueue;
        foreach($freq as $key => $count) {
            $heap->insert($key, $count);
        }

        $result = [];
        for($i = 0; $i < $k; $i++) {
            $result[] = $heap->extract();
        }

        return $result;

    }
}