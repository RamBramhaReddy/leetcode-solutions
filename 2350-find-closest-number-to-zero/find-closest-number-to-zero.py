class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        c = nums[0]
        for i in nums:
            if abs(i) < abs(c) or (abs(i) == abs(c) and i > c ) :
                c = i 
        return c 