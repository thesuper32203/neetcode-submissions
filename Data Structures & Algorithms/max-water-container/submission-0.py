class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1

        volume = 0

        while l < r:

            height = min(heights[l], heights[r])
            distance = r - l
            water = height * distance

            volume = max(volume, water)

            if heights[l] <= heights[r]:
                l = l + 1
            else:
                r = r - 1
        
        return volume
