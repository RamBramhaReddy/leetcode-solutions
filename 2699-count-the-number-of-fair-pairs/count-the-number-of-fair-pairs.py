class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()

        def count_less_than(x):
            left = 0
            right = len(nums) - 1
            total = 0

            while left < right:
                if nums[left] + nums[right] < x:
                    total += right - left
                    left += 1
                else:
                    right -= 1

            return total

        return count_less_than(upper + 1) - count_less_than(lower) 
