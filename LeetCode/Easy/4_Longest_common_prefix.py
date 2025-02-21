

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
         res = ''

         # we access the first word of the list to get the length
         for i in range(len(strs[0])):
              print('this is i', i)
              # we access all the word in the lsit and loop through them
              for s in strs:
                   print('this is s',s, 'and this is length', len(s))
                  # we check if the current index of the word is equal to the length of the s or if the current index of the word is not equal to the first word of the given list
                   if i == len(s) or s[i]!= strs[0][i]:
                        print(s[i])
                        return res
                   
               # else we add the current index of the first word to the result
              res += strs[0][i]
         return res

        
   

       


#strs = ["ab", "a"]

#strs = ["dog","racecar","car"]

strs = ["flower","flow","flight"]
s = Solution()

result = s.longestCommonPrefix(strs)

print(result)