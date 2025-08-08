class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store numbers and their indices
        num_map = {}
        
        # Loop through the list, in this case i is the index num is the number 
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_map:
                # If it exists, return the indices of the complement and the current number
                print('this is num_map', num_map[complement])
                return [num_map[complement], i]
            
            # If the complement doesn't exist, add the current number 
            # and its index to the dictionary
            num_map[num] = i
            print(num_map)
           
        
        # If no solution is found (though the problem guarantees one)
        return []
    
nums = [2, 7, 11, 15]
target = 9
# in python method that have self need an instance to call them so self refers to that instance 
# creating instance of the solution class 
s = Solution()
result = s.twoSum(nums, target)
print("Result:", result)  # Output: [0, 1]
