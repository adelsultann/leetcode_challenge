
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        print(roman_to_int[s[0]]) #50
        print(roman_to_int[s[1]]) #5
        result = 0
        for i in range(len(s)):
            
            # we add i + 1 to check if there is next character | so we avoid index error
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                result += roman_to_int[s[i]]
        return result
                   
           
      
        
    
num = "LVIII"
target = 9
s = Solution()
result = s.romanToInt(num)
print("Result:", result)  
