class Solution:
    def countDigits(self, num: int) -> int:
        c = 0
        lst = [i for i in str(num)]
        for i in lst:
            if num % int(i) ==0:
                c+=1
        return c 