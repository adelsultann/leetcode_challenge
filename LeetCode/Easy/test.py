class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store numbers and their indices
       for i in range(len(nums)):
        for j in range(i + len(nums)):
            print('this is i ', i)
            print("this is j ", j)

    
nums = [2, 7, 11, 15]
target = 9
# in python method that have self need an instance to call them so self refers to that instance 
# creating instance of the solution class 
s = Solution()
result = s.twoSum(nums, target)
print("Result:", result)  # Output: [0, 1]
