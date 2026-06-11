class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =0
        element = None

        for i in nums:
            if count ==0:
                element = i
            
            if i == element:
                count+=1
            else:
                count -=1

        return element