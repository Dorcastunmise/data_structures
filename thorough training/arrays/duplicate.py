#Time Complexity O(n)
#Space Complexity O(n)
# Pattern used is Hashing

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))