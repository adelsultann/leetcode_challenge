class Solution:
        def removeElement(self, nums: list[int], val: int) -> int:
     
         k = len(nums)
        

         for i in range(len(nums)):
            if nums[i] == val:
               nums[i] = '-'
               k -= 1
        
         print(k)
         print(nums)
        
    

    

     
     



solution = Solution()


nums=[0,1,2,2,3,0,4,2]
val = 2
result = solution.removeElement(nums,val)