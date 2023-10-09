# 1. Contains Duplicate
def containsDuplicate(nums):
    hset = set()
    for i in nums:
        if i in hset:
            return True
        hset.add(i)
    return False
# nums=[1,2,3,1]
# print(containsDuplicate(nums))


# 2. Valid Anagram 
def isAnagram(word1, word2):
    sorted_1 = sorted(word1)
    sorted_2 = sorted(word2)
    return sorted_1 == sorted_2
# print(isAnagram("anaram","nagaram"))


# 3. Two Sum
def twoSums(nums, target):
    numDict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in numDict:
            return [numDict[diff],i]
        numDict[nums[i]] = i
# nums = [3,2,4]
# target = 6
# print(twoSums(nums,target))


# 4. Group Anagrams 
def groupAnagrams(strs):
    # loop through each string and get its characters
    lstAnagram = {}
    for i in strs:
        sorted_i = "".join(sorted(i))
        if sorted_i in lstAnagram:
            lstAnagram[sorted_i].append(i)    
        else:
            arr = []
            arr.append(i)
            lstAnagram[sorted_i] = arr

    return list(lstAnagram.values())

# stringList = ["eat","tea","tan","ate","nat","bat"]
# print(groupAnagrams(stringList))


# 5. Top K Frequent Elements (v1)
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
def topKFrequent(nums, k):
    countDict = {}
    for i in nums:
        if i in countDict:
            countDict[i] += 1
        else: 
            countDict[i] = 1

    sorted_dict = dict(sorted(countDict.items(), key=lambda item: item[1], reverse=True))
    lst = list(sorted_dict.keys())
    return lst[:k]

# 5. Top K Frequent Elements (v2)
def topKFrequent2(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums:
        count[n] = 1 + count.get(n,0)
    for n,c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res)==k:
                return res

# nums = [1,1,1,2,2,3]
# k = 2
# print(topKFrequent(nums,k))
# print(topKFrequent2(nums,k))


# 6. Product of Array Except Self
def productExceptSelf(nums):
    res=[]
    for i in nums:
        mul = 1
        for j in nums:
            if j != i:
                mul *= j
        res.append(mul)
    return res


# nums = [0,0]
# print(productExceptSelf(nums))

# Given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
def solution(a):
    sorted_a = sorted(a)
    hset = set()
    for i in sorted_a:
        if i > 0:
            hset.add(i)
    for j in range(1,len(hset)+2, 1):
        if j not in hset:
            return j 
            
# a = [1, 3, 6, 4, 1, 2]
# print(solution(a))


# 7. Longest Consecutive Sequence 
def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0 
    for n in num_set:
        if (n-1) not in num_set:
            length = 1
            while (n+length) in num_set:
                length += 1
            longest = max(longest,length)
    return longest

    # if i != len(sorted_nums) and ((sorted_nums[i+1] - sorted_nums[i] != 1) or (sorted_nums[i+1] - sorted_nums[i] != 0)):
    #     return length
            
# nums = [0,3,7,2,5,8,4,6,0,1]
# print(longestConsecutive(nums))


# 8. Valid Sudoku 
def isValidSudoku(lstStr): 

    # store a set for each column, row, and blocks to track numbers
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    blocks = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            curr = lstStr[i][j]
            if curr == ".":
                continue 
            # checks if curr is in the particular set's row/column/block 
            if curr in rows[i] or curr in cols[j] or curr in blocks[i//3][j//3]:
                return False
            # adds to particular sets if number is not inside sets
            rows[i].add(curr)
            cols[j].add(curr)
            blocks[i//3][j//3].add(curr)
    
    return True



board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

