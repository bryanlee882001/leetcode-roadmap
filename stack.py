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
# str1 = "{(([)])}"
# print(isValidParenthesis(str1))


#2 MinStack
# Idea: Create two stacks: 1 being the actual stack and the other to track minimum 
# when appending to stack
class MinStack: 

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if len(self.minStack)!=0 else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
# stackObj = MinStack()
# stackObj.push(3)
# stackObj.push(-2)
# stackObj.push(-5)
# stackObj.pop()
# stackObj.push(-3)
# stackObj.push(4)
# print(stackObj.top())
# print(stackObj.getMin())


# 3. Evaluate Reverse Polish Notation
def evalRPN(tokens):

    p = []
    for i in tokens:
        if i == "+" or i == "-" or i == "*" or i == "/":
            a = p.pop()
            b = p.pop()
            p.append(int(eval(str(b)+i+str(a))))
        else: 
            p.append(i)
    
    return int(p[0])

# tokens = ["2","1","+","3","*"]
# print(evalRPN(tokens))
        

# 4. Daily Temperatures
# def dailyTemperatures(temp):
    
    arr = []

    # p1 will keep track of the indexes, and p2 will keep track of increasing temperatures
    p1 = 0 

    while p1 <= len(temp)-1:
    
        if p1 == len(temp)-1:
            arr.append(0)
            return arr

        if temp[p1+1] > temp[p1]:
            arr.append(1)             
        else: 
            count = 2
            p2 = p1+2
            while p2 <= len(temp)-1:
                if temp[p2] > temp[p1]:
                    arr.append(count)
                    break
                count += 1 
                p2 += 1 
        p1 += 1
    
    return arr 

def dailyTemperatures(temperatures):
    
    stk = []
    days = [0] * len(temperatures)

    for i in range(len(temperatures)):
        
        while len(stk) != 0 and temperatures[stk[-1]] < temperatures[i]:
            unsettledDays = stk.pop()
            days[unsettledDays] = i - unsettledDays

        stk.append(i)
    return days 

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))