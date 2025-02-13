
// : number || this is the output 
function romanToInt(s: string): number {
     let result = 0;
     let prevValue = 0;
     // we are creating Object dic and we specifiy the key is strign 
     // key : string

     //number: The number part specifies that each value associated with the key should be a number
     const romanValues: { [key: string]: number } = {
         'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000
     };
     // initializes the loop variable i to the last character in the string array s | the last char is s.length - 1 

     // i >= 0 this is the condition for continuing the loop 
     // the loop is continue as long as i is greater than or equal to 0
     // i-- | decrements the loop varaible i by after each iteration
     for (let i = s.length - 1; i >= 0; i--) {
         const currValue = romanValues[s[i]];
         if (currValue < prevValue) {
             result -= currValue;
         } else {
             result += currValue;
         }
         prevValue = currValue;
     }
     return result;
 };
 
 
 const s = "MCMXCIV"
 
 const romanToResult = romanToInt(s)
 
 console.log("this is the result:", romanToResult)