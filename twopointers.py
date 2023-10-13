#1 Valid palindrome
def isPalindrome1(s):
    l = 0 
    r = len(s)-1

    while l < r: 
        while l<r and s[l].isalnum() == False: 
            l += 1
        while l<r and s[r].isalnum() == False:
            r -= 1
        if (s[l].lower() == s[r].lower()):
            print(s[l].lower(),s[r].lower()) 
            l += 1
            r -= 1
        else: 
            return False
    return True
# print(isPalindrome1("A man, a plan, a canal: Panama"))

def isPalindrome2(s):
    s1 = ''
    for c in s.lower():
        if c.isalnum():
            s1 += c 
    return True if s1==s1[::-1] else False
# print(isPalindrome2("A man, a plan, a canal: Panama"))


#2 Two Sum II - Input Array is Sorted
def twoSum(numbers, target):
    l = 0
    r = len(numbers)-1
    while l < r:
        if (numbers[l]+numbers[r]==target):
            return [l+1,r+1]
        if (numbers[l]+numbers[r]> target):
            r -= 1
        else:
            l += 1
        print(numbers[l],numbers[r])
    return None
# numbers = [2,7,11,15]
# target = 9
# print(twoSum(numbers,target))


#3 Container with Most Water
def maxArea(height):
    maxArea = 0 
    left = 0 
    right = len(height) - 1

    while left < right: 
        currArea = min(height[left], height[right]) * (right - left)    
        maxArea = max(maxArea, currArea)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return maxArea

# print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([2,3,4,5,18,17,6]))
