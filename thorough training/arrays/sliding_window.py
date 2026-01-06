#Time Complexity O(n)
#Space Complexity O(k)
# Pattern used is Sliding Window with Hashing
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for index, num in enumerate(nums): #O(n)
            if index > k:
                window.remove(nums[index - k - 1]) #O(k) remove the first element to be brought in to shift and maintain the window size

            if num in window:
                return True
            
            window.add(num)

        return False


