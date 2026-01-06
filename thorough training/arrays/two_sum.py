#Time Complexity O(n)
#Space Complexity O(n)
# Pattern used is Hashing
#nums = [2,7,11,15], target = 9
class Solution:
    def twoSum(nums, target): #Time - O(n), Space - O(n): due additional set to store the result for memoization
        hashResult = {}

        for index, num in enumerate(nums):
            remval = target - num
            if remval in hashResult: #O(1)
                return [hashResult[remval], index]
            hashResult[remval] = index

