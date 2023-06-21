"""Sliding Window - maxSubarraySum
Given an array of integers and a number, write a function called maxSubarraySum, 
which finds the maximum sum of a subarray with the length of the number passed to the function.

Note that a subarray must consist of consecutive elements from the original array. In the first example below,
 [100, 200, 300] is a subarray of the original array, but [100, 300] is not.

maxSubarraySum([100,200,300,400], 2) // 700
maxSubarraySum([1,4,2,10,23,3,1,0,20], 4)  // 39 
maxSubarraySum([-3,4,0,-2,6,-1], 2) // 5
maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2) // 5
maxSubarraySum([2,3], 3) // null
Constraints:

Time Complexity - O(N)

Space Complexity - O(1)"""


def max_subarray_sum(lst:list, n:int):
    assert (isinstance(lst,list) and isinstance(n,int)), "arguement expects list and int"
    if n > len(lst):
        return None

    running_sum = 0
    for idx in range(n):
        running_sum += lst[idx]

    
    max_sum = running_sum
  
    for idx in range(n, len(lst)):
        running_sum = (running_sum + lst[idx]) - lst[idx - n]
        if running_sum > max_sum:
            max_sum = running_sum

    return max_sum

print(max_subarray_sum([100,200,300,400], 2)) 
print(max_subarray_sum([1,4,2,10,23,3,1,0,20], 4))   
print(max_subarray_sum([-3,4,0,-2,6,-1], 2)) 
print(max_subarray_sum([3,-2,7,-4,1,-1,4,-2,1],2)) 
print(max_subarray_sum([2,3], 3))


print("......................Sliding Window - minSubArrayLen........................................")

"""
Write a function called minSubArrayLen which accepts two parameters - an array of positive integers and
 a positive integer. This function should return the minimal length of a contiguous subarray of which the 
 sum is greater than or equal to the integer passed to the function. If there isn't one, return 0 instead.

Examples:

minSubArrayLen([2,3,1,2,4,3], 7) // 2 -> because [4,3] is the smallest subarray
minSubArrayLen([2,1,6,5,4], 9) // 2 -> because [5,4] is the smallest subarray
minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52) // 1 -> because [62] is greater than 52
minSubArrayLen([1,4,16,22,5,7,8,9,10],39) // 3
minSubArrayLen([1,4,16,22,5,7,8,9,10],55) // 5
minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11) // 2
minSubArrayLen([1,4,16,22,5,7,8,9,10],95) // 0
Time Complexity - O(n)

Space Complexity - O(1)
"""

def min_subarray_len(lst:list, n:int):
    ##presently flawed!!!
    assert (isinstance(lst,list) and isinstance(n,int)), "arguement expects list and int"   
    if sum(lst) < n:
        return 0

    left_pointer = 0
    right_pointer = 0

    running_sum = 0
    running_len = len(lst)
    cur_lst = None

    while left_pointer < len(lst):

        if lst[left_pointer] >= n:
            return [lst[left_pointer]], 1

        if running_sum < n and right_pointer < len(lst):
            running_sum += lst[right_pointer]
            right_pointer += 1



        elif running_sum >= n:
            running_len = min((right_pointer - left_pointer), running_len)
            cur_lst = lst[left_pointer:right_pointer+1]
            running_sum = running_sum - lst[left_pointer]
            left_pointer += 1

        else:
            break

          

    return cur_lst, running_len




print(min_subarray_len([2,3,1,2,4,3], 7)) 
print(min_subarray_len([2,1,6,5,4], 9)) 
print(min_subarray_len([3,1,7,11,2,9,8,21,62,33,19], 52))
print(min_subarray_len([1,4,16,22,5,7,8,9,10],39)) 
print(min_subarray_len([1,4,16,22,5,7,8,9,10],55)) 
print(min_subarray_len([4, 3, 3, 8, 1, 2, 3], 11) )
print(min_subarray_len([1,4,16,22,5,7,8,9,10],95))





print("......................Sliding Window - findLongestSubstring........................................")

"""
Sliding Window - findLongestSubstring
Write a function called findLongestSubstring, which accepts a string and returns the length of the
 longest substring with all distinct characters.

findLongestSubstring('') // 0
findLongestSubstring('rithmschool') // 7
findLongestSubstring('thisisawesome') // 6
findLongestSubstring('thecatinthehat') // 7
findLongestSubstring('bbbbbb') // 1
findLongestSubstring('longestsubstring') // 8
findLongestSubstring('thisishowwedoit') // 6
Time Complexity - O(n)
"""

def find_longest_substring(string:str):
    running_len = 0
    first_pointer = 0
    last_pointer = 0

    while first_pointer < len(string):

        