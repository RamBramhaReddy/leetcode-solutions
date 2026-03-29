class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = 0
        res = []

        while i >= 0 or k > 0 or carry:
            digit_num = num[i] if i >= 0 else 0
            digit_k = k % 10
            k //= 10

            s = digit_num + digit_k + carry
            res.append(s % 10)
            carry = s // 10

            i -= 1

        res.reverse()
        return res