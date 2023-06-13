"""
Write a function called sameFrequency. Given two positive integers, 
find out if the two numbers have the same frequency of digits.
Your solution MUST have the following complexities:

Time: O(N)

Sample Input:

sameFrequency(182,281) // true
sameFrequency(34,14) // false
sameFrequency(3589578, 5879385) // true
sameFrequency(22,222) // false

"""

def same_frequency(first_int:int,second_int:int):
    assert (isinstance(first_int,int) and isinstance(second_int,int)), "the arguements has to be integers"
    first_int = str(first_int)
    second_int = str(second_int)

    if len(first_int) != len(second_int):
        return False

    first_dict = {}
    second_dict = {}
    for item in first_int:
        if first_dict.get(item, None):
            first_dict[item] += 1
        else:
            first_dict[item] = 1

    for item in second_int:
        if second_dict.get(item, None):
            second_dict[item] += 1
        else:
            second_dict[item] = 1
   
    for key, value in first_dict.items():
        if key not in second_dict:
            return False
        elif value != second_dict[key]:
            return False
    return True


print(same_frequency(182,281)) 
print(same_frequency(34,14) )
print(same_frequency(3589578, 5879385)) 
print(same_frequency(22,222)) 

print(".......................................duplicates?.................................................")

"""Implement a function called, areThereDuplicates which accepts a variable number of arguments, 
and checks whether there are any duplicates among the arguments passed in.  
You can solve this using the frequency counter pattern OR the multiple pointers pattern.
Examples:

areThereDuplicates(1, 2, 3) // false
areThereDuplicates(1, 2, 2) // true 
areThereDuplicates('a', 'b', 'c', 'a') // true 
Restrictions:

Time - O(n)

Space - O(n)
"""

def are_there_duplicates(*arg):
    if len(arg) == 0:
        return False

    left_pointer = 0
    right_pointer = 1

    
    



