class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        length=len(s)
        left=0
        right=length-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            
            left+=1
            right-=1
        return True

        
        