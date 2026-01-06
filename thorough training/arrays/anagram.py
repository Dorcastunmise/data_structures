#Time Complexity O(n) - loop through s once and t once (combined length = n).
#Space Complexity O(26) -> O(1) ...for hashmap (sArr) filled with constant 26 alphabets. If s and t can contain any characters (Unicode), space is O(n) in the worst case.
# Pattern used is HashMap
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        sArr = {}
        for char in s:
            sArr[char] = sArr.get(char, 0) + 1
        
        for char in t:
            if char in sArr:
                sArr[char] -=1
            if char not in sArr:
                return False
            if sArr[char] < 0:
                return False

        return True
        