def reverseInteger(x: int):
        rev = 0
        while x > 0:
            dig = x % 10
            x = x // 10
            rev = rev*10 + dig
            
        return rev

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        res = reverseInteger(x)
        if res == x:
            return True
        else:
            return False
