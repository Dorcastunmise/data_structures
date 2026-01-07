import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}

        for num in nums:
            freq[num] =  freq.get(num, 0) + 1

        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))
        
        result = []
        for _ in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)

        return result
        