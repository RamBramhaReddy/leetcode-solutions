class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        lst1 = []
        for i in range(0, len(nums), 2):
            lst1.append(nums[i + 1])
            lst1.append(nums[i])
        return lst1

