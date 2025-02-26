

function isValid(s: string): boolean {
     //A variable openBracket is initialized as an empty array
     let openBracket: string[] = [];

     const bracketMap: { [key: string]: string } = { ')': '(', '}': '{', ']': '[' };

     for (let i of s) {
         if (s.length <= 1) {
             return false;
         }
         //Check if the Character is an Open Bracket 
         //Object.values(bracketMap) retrieves the values of the bracketMap object, which are the open brackets
         if (Object.values(bracketMap).includes(i)) {
             openBracket.push(i);
     
             //Check if the Character is a Closing Bracket 
             //Object.keys(bracketMap) retrieves the keys of the bracketMap object, which are the closing brackets
         } else if (Object.keys(bracketMap).includes(i)) {

          //openBracket.length - 1 | to get the last element 
             if (openBracket.length && openBracket[openBracket.length - 1] === bracketMap[i]) {
                 openBracket.pop();
             } else {
                 return false;
             }
         }
     }

     return openBracket.length === 0;
 }


// Example usage:
const s = "()[]{";
const solution = isValid(s)
console.log(isValid(s));  // This should print false

