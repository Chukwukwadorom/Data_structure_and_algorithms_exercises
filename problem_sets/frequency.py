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
    freq_dict = {}
    for item in arg:
        if freq_dict.get(item, None):
            return True 
        else:
            freq_dict[item] = 1

    return False

    
    
print(are_there_duplicates(1, 2, 3)) 
print(are_there_duplicates(1, 2, 2)) 
print(are_there_duplicates('a', 'b', 'c', 'a'))  

def are_there_duplicates_mp(*arg):
    """using multiple pointers"""
    arg_list = list(arg)
    arg_list.sort()

    first_pointer = 0
    second_pointer = 1

    while second_pointer != len(arg_list):
        if arg_list[second_pointer] != arg_list[first_pointer]:
            ## arg_list[second_pointer] == arg_list[first_pointer] return true will work!
            first_pointer += 1
            arg_list[first_pointer] = arg_list[second_pointer]
        
        second_pointer +=1

    if (first_pointer + 1) != len(arg_list):
        return True
    else:
        return False

print("\n")

print(are_there_duplicates_mp(1, 2, 3)) 
print(are_there_duplicates_mp(1, 2, 2)) 
print(are_there_duplicates_mp('a', 'b', 'c', 'a')) 


def are_there_duplicates_lf(*arg):
    """linear function"""
    return len(set(arg)) != len(arg)


print("\n")

print(are_there_duplicates_lf(1, 2, 3)) 
print(are_there_duplicates_lf(1, 2, 2)) 
print(are_there_duplicates_lf('a', 'b', 'c', 'a')) 
