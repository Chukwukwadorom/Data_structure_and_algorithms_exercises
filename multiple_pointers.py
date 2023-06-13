"""Creating pointers or values that correspond to an index or position and 
move towards the beginning, end or middle based on a certain condition
Very efficient for solving problems with minimal space complexity as well


AN EXAMPLE
Write a function called sumZero which accepts a sorted array of integers. 
The function should find the first pair where the sum is 0. Return an array that
 includes both values that sum to zero or undefined if a pair does not exist
 sumZero([-3,-2,-1,0,1,2,3]) // [-3,3] 
sumZero([-2,0,1,3]) // undefined
sumZero([1,2,3]) // undefined
"""

def sum_zero_naive(lst:list):

    """ Time Complexity - O(N^2). Space Complexity - O(1)"""

    assert isinstance(lst,list), "arguement must be a list"
    for a in range(len(lst)):
        for b in range(a+1,len(lst)):
            if lst[a] + lst[b] == 0:
                return (lst[a],lst[b])

    return False
    

print("naive approach:",  sum_zero_naive([-3,-2,-1,0,1,2,3]))



def sum_zero_better(lst:list):
    """ using pointers. Time Complexity - O(n). space complexity O(1)"""
    assert isinstance(lst,list), "arguement must be a list"

    left_pointer = 0
    right_pointer = len(lst)-1

    while left_pointer != right_pointer:
        if (lst[left_pointer] + lst[right_pointer]) > 0:
            right_pointer -= 1
        elif (lst[left_pointer] + lst[right_pointer]) < 0:
            left_pointer += 1
        else:
            return(lst[left_pointer], lst[right_pointer])

    return False 


print("multiple pointer approach:" , sum_zero_better([-3,-2,-1,0,1,2,3]))
print("multiple pointer approach:" , sum_zero_better([-2,0,1,3]))




#################################### count unique values ########################################################
"""countUniqueValues
Implement a function called countUniqueValues, which accepts a sorted array, and counts the unique values in the array. There can be negative numbers in the array, but it will always be sorted.

countUniqueValues([1,1,1,1,1,2]) // 2
countUniqueValues([1,2,3,4,4,4,7,7,12,12,13]) // 7
countUniqueValues([]) // 0
countUniqueValues([-2,-1,-1,0,1]) // 4"""


def countUniqueValues_set(lst):
    """count unique values using set. time complexity:O(N)"""
    return len(set(lst))


print("counting unique values using set:", countUniqueValues_set([1,1,1,1,1,2]))
print("counting unique values using set:", countUniqueValues_set([1,2,3,4,4,4,7,7,12,12,13]))
print("counting unique values using set:", countUniqueValues_set([]))
print("counting unique values using set:", countUniqueValues_set([-2,-1,-1,0,1]))


def countUniqueValues_freq_counter(lst):

    """count unique values using freq counter. time complexity:O(N)"""
    freq_dict = {}

    for element in lst:
        if freq_dict.get(element, None):
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1

    
    return len(freq_dict)

print("...................using freq counter..................")

print("counting unique values using frequency counter:", countUniqueValues_freq_counter([1,1,1,1,1,2]))
print("counting unique values using frequency counter:", countUniqueValues_freq_counter([1,2,3,4,4,4,7,7,12,12,13]))
print("counting unique values using frequency counter:", countUniqueValues_freq_counter([]))
print("counting unique values using frequency counter:", countUniqueValues_freq_counter([-2,-1,-1,0,1]))



def countUniqueValues_multi_pointer(lst):
    """count unique values using pointer, altering the list. time complexity:O(N)
    this method presupposes that the list is sorted
    """
    i = 0
    j =  1
    if len(lst) == 0:
        return 0

    while j != len(lst):
      if lst[i] != lst[j]:
          i += 1
          lst[i] = lst[j]
      j += 1
    return i+1, lst[:i+1]  

print("...................using multi pointer..................")

print("counting unique values using multi pointer:", countUniqueValues_multi_pointer([1,1,1,1,1,2]))
print("counting unique values using multi pointer:", countUniqueValues_multi_pointer([1,2,3,4,4,4,7,7,12,12,13]))
print("counting unique values using multi pointer:", countUniqueValues_multi_pointer([]))
print("counting unique values using multi pointer:", countUniqueValues_multi_pointer([-2,-1,-1,0,1]))





