class Solution:
    def reverse(self, x: int) -> int:
        
        rev = 0
        
        negative_number = False
        if x < 0:
            negative_number = True
            x = abs(x)
        while x > 0:
            dig = x % 10
            x = x // 10
            rev = rev*10 + dig
            
        if rev > 2**31 - 1 or rev < -2**31:
            return 0
        if negative_number:
            return -(rev)
        
        return rev
