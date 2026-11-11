class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff = {}

        for i in range(len(nums)):
            diff[nums[i]] = i
        
        for i in range(len(nums)):

            d = target - nums[i]

            if d in diff and i != diff[d]:
                return [i, diff[d]]
        return []

        

            

        return []