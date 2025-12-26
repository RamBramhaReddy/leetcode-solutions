class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        
        for num in nums:
            x = num
            while x > 0:
                digit_sum += x % 10
                x //= 10
        
        return abs(element_sum - digit_sum)

