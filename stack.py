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
stackObj = MinStack()
stackObj.push(3)
stackObj.push(-2)
stackObj.push(-5)
stackObj.pop()
stackObj.push(-3)
stackObj.push(4)
# print(stackObj.top())
# print(stackObj.getMin())


def binarySearch(nums,target):
    
    left,right=0,len(nums)-1
    while left<=right:
        mid=left+(right-left)//2
        if nums[mid]>target:
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
        else:
            return mid
    return -1


nums = [-1,0,3,5,9,12,18,19,20]
target = 19
print(binarySearch(nums,target))

