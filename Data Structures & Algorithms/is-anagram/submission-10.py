class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        an1 = {}
        an2 = {}

        for i in range(len(s)):
            
            if s[i] not in an1:
                an1[s[i]] = 1
            else:
                an1[s[i]] += 1

            if t[i] not in an2:
                an2[t[i]] = 1
            else:
                an2[t[i]] += 1
        
        for k in an1:
            if an2.get(k) is None or an1[k] != an2[k]:
                return False

        return True

            
            

                

            
