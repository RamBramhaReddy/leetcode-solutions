class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0 
        l, r = 0 , len(height)- 1
        while l < r :
            w = r - l
            h = min(height[l],height[r])
            area = h * w 
            maxarea = max(maxarea,area)

            if height[l] < height[r]:
                l += 1
            else :
                r -=1

        return maxarea