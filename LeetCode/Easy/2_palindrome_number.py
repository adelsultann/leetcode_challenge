class Solution(object):
    def isPalindrome(self, x):
        """
        reverse the number 
        check if its equel to the original number 
        """
        if x < 0:
            return False

        s =str(x)
        s=  s[::-1]
        s = int(s)

        return x == s
      
        

x = 212

s = Solution()

result = s.isPalindrome(x)

print("Result:", result)  # Output: [0, 1]
