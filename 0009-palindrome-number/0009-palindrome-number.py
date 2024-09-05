class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s == s[::-1] and x>=0:
            return True
        else:
            return False
        