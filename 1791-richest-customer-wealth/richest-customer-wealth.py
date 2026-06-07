class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for i in accounts:
            s = 0
            for j in i:
                s +=  j 
            if s > max_wealth :
                max_wealth = s
        return max_wealth