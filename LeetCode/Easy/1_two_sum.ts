// the function take num: an arry of numbers | target = numbers | it return arry of numbers []

function twoSum(nums: number[], target: number): number[] {

     // create a map that will store the numbers and corresponding indices
     //new Map() creates an empty Map object, ready for use. | without it the variable would be undefined
    const hashmap: Map<number, number> = new Map();
    for (let i = 0; i < nums.length; i++) {

     //Example: If target = 9 and nums[i] = 2, then complement = 9 - 2 = 7.
        const complement = target - nums[i];
        //Checks if the complement is already in the Map.
        if (hashmap.has(complement)) {
          //If true, it means a previous number and the current number sum up to the target.
          //The ! indicates that the value is guaranteed to exist (TypeScript syntax).
            return [hashmap.get(complement)!, i];
        }
        //Add Current Number to the Map | Each number (nums[i]) is stored as a key, and its index (i) is stored as the value.
        hashmap.set(nums[i], i);
    }
    // Return an empty array if no solution is found
    return [];
}
 // Example usage
 const nums = [2, 7, 11, 15];
 const target = 9;
 const result = twoSum(nums, target);
 console.log("Indices of the two numbers:", result);