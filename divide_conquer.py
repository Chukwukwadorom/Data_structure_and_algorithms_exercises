"""
Divide and Conquer
This pattern involves dividing a data set into smaller chunks and
 then repeating a process with a subset of data.
This pattern can tremendously decrease time complexity

An Example
Given a sorted array of integers, write a function called search, that 
accepts a value and returns the index where the value passed to the function is located. 
If the value is not found, return -1
search([1,2,3,4,5,6],4) // 3
search([1,2,3,4,5,6],6) // 5
search([1,2,3,4,5,6],11) // -1(or None)
"""

def linear_search(lst:list, item):
    
    assert isinstance(lst,list), "a iterable is required in the first arguement"

    for index in range(len(lst)):
        if lst[index] == item:
            return index

    return None

print(".........................linear search...................")
print(linear_search([1,2,3,4,5,6],4)) 
print(linear_search([1,2,3,4,5,6],6)) 
print(linear_search([1,2,3,4,5,6],11))


def binary_search(lst:list, item):
    assert isinstance(lst,list), "a iterable is required in the first arguement"

    left_pointer = 0
    right_pointer = len(lst)-1

    while left_pointer <= right_pointer:
        midway = (left_pointer + right_pointer)//2
        if lst[midway] == item:
            return midway
        elif item > lst[midway]:
            left_pointer = midway + 1
        else:
             right_pointer = midway - 1

    return None



print(".........................Binary search...................")
print(binary_search([1,2,3,4,5,6],4)) 
print(binary_search([1,2,3,4,5,6],6)) 
print(binary_search([1,2,3,4,5,6],11))