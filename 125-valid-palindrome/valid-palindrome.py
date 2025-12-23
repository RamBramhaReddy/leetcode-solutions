class Solution:
    def isPalindrome(self, s: str) -> bool:
        string =''
        for i in s.lower():
            if i.isalnum():
                string+=i
            
        return string == string[::-1]