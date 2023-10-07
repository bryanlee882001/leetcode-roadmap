#1 Valid Parentheses
def isValidParenthesis(s):
    
    stack = []
    pairings = {"(":")","[":"]","{":"}"}

    for bracket in s:
        if bracket in pairings: 
            stack.append(bracket)
        # check if stack is empty / closing bracket not equals to top of the stack (opening)
        # NOTE: OPENING BRACKETS MUST BE CLOSED IN A CORRECT ORDER
        elif len(stack)==0 or bracket!=pairings[stack.pop()]:
            return False
        
    return len(stack) == 0

str1 = "{(([)])}"
print(isValidParenthesis(str1))