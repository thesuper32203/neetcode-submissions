class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexs = {}

        for i in range(len(nums)):

            indexs[nums[i]] = i

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in indexs and i != indexs[diff]:
                return [i,indexs[diff]]
        
        return []