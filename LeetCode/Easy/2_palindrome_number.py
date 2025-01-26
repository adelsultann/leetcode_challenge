class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10
            print(temp)

        return reversed_num == x

 
x = 212

s = Solution()

result = s.isPalindrome(x)

print("Result:", result)  # Output: [0, 1]
