class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l , r = 0 , n-1
        idx = n-1

        while l <= r:
            l_sq = nums[l] * nums[l]
            r_sq = nums[r] * nums[r]

            if l_sq > r_sq:
                res[idx] = l_sq
                l+=1
            else:
                res[idx] = r_sq
                r -=1
            idx -=1
        return res