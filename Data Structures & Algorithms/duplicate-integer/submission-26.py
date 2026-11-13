class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        u = set()

        for num in nums:

            if num in u:
                return True
            u.add(num)
        
        return False
