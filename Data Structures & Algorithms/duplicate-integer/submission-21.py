class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        u = set()

        for i in nums:
            if i not in u:
                u.add(i)
            else: 
                return True
        return False