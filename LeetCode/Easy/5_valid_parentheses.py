

#In object-oriented programming, a class is a blueprint for creating objects (a particular data structure).
class Solution:
    # define a method name isValid within the solution class
    def isValid(self, s: str) -> bool:
        # this list will be used to store all the opening Brackets
        open_bracket = []
        
        # this dic will maps each closing bracket to its corresponding opening bracket 
        bracket_map = {')': '(', '}': '{', ']': '['}
        print('this is open',bracket_map[')'])
        for i in s:
            print(i)
            if len(s) <= 1:
                return False

            # this line check if i is opening brackets 
            if i in bracket_map.values():
                open_bracket.append(i)
                print('after the append', open_bracket)

            # this lines handle the close bracket 
            elif i in bracket_map.keys():
                # if the list open_bracket is not empty and 
                # list items == bracket_map[i] , eg i = ] |
                #  bracket_map[']'] = [  | we put the keys to retrive the values 
                if open_bracket and open_bracket[-1] == bracket_map[i]:
                    print('thi s', bracket_map[i])
                    # this line remove the last item from open bracket list
                    open_bracket.pop()
                    print('after the pop', open_bracket)

                    #if either open_bracket is empty or the last item in open_bracket does not match the corresponding opening bracket for i
                else:
                    return False
        
        return len(open_bracket) == 0

    
        


s = "([])"

solution = Solution()

result = solution.isValid(s)

print(result)