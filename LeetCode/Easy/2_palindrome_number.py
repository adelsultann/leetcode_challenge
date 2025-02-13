
class Solution:
    # slef is used when the function is part of calss 
    def isPalindrome(self, x: int) -> bool:
        # handle edge Case : a situation or input that not typical or comman in may require special handling 
        #150 % 10 = 0 | 122 % 10 = 2 | it always take the last digit
        # x > 0 and x % 10 == 0 | this line check if the number is positive and last digit is 0 eg 20 % 10 = 0
        if x < 0 or (x > 0 and x % 10 == 0):  
            
            # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
            return False
        result = 0
        while x > result:
            # get the last digit for eg x = 1221 the result will be 1 in the first itration the second will be 2
            # in the second itration result is = 12 so it is not greater than x we will stop the while loop 
            result = result * 10 + x % 10
            print("this is result", result)
            x = x // 10
            print(x)
        # x == result | this is for even number if the reveresed half equal the remaning half of x
        # Eg x = 1221 , first 
        return True if (x == result or x == result // 10) else False
 
x = 212
s = Solution()
result = s.isPalindrome(x)
print("Result:", result)  # Output: [0, 1]
