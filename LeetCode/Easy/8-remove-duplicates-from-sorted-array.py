class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
     
    

     k = 1 
     for i in range(1, len(nums)):
            if nums[i] != nums[i -1]:
               nums[k] = nums[i]
               k += 1
               print(k)
     print(k)
     return k


    

     
     



solution = Solution()

result = solution.removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4])