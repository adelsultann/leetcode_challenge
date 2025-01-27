class Solution:
    # slef is used when the function is part of calss 
    def isPalindrome(self, x: int) -> bool:
        # handle edge Case : a situation or input that not typical or comman in may require special handling 
        #150 % 10 = 0 | 122 % 10 = 2 | it always take the last digit
        if x < 0 or (x > 0 and x % 10 == 0):  
            
            # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
            return False

        result = 0
        while x > result:
            result = result * 10 + x % 10
            print("this is result", result)
            x = x // 10
            print(x)

        return True if (x == result or x == result // 10) else False
 
x = 212

s = Solution()

result = s.isPalindrome(x)

print("Result:", result)  # Output: [0, 1]
