class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if len(s) != len(t):

            return False

        result = [0] * 26

        for c in s:
            result[ord(c) - ord("a")] += 1
        
        for c in t:
            result[ord(c) - ord("a")] -= 1

        for num in result:
            if num != 0:
                return False

        return True