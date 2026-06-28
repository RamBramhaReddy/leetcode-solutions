class Solution:
    def maxPower(self, s: str) -> int:
        left = 0
        ans = 1

        for right in range(1, len(s)):
            if s[right] != s[right - 1]:
                left = right
            ans = max(ans, right - left + 1)

        return ans