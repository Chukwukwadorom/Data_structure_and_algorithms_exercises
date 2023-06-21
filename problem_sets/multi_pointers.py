"""
Multiple Pointers - averagePair
Write a function called averagePair. Given a sorted array of integers and a target average,
 determine if there is a pair of values in the array where the average of the pair equals the target average. 
 There may be more than one pair that matches the average target.

Bonus Constraints:

Time: O(N)

Space: O(1)

Sample Input:

averagePair([1,2,3],2.5) // true
averagePair([1,3,3,5,6,7,10,12,19],8) // true
averagePair([-1,0,3,4,5,6], 4.1) // false
averagePair([],4) // false
"""

def average_pair(lst:list,avr):
    assert (isinstance(lst,list) and (isinstance(avr,int) or isinstance(avr,float))),"the function expects a list and a float/int"


    if len(lst) == 0:
        return False

    first_pointer = 0
    last_pointer = len(lst)-1

    while first_pointer != last_pointer:
         if (lst[first_pointer] + lst[last_pointer])/2 > avr:
            last_pointer -= 1
         elif (lst[first_pointer] + lst[last_pointer])/2 < avr:
            first_pointer += 1
         else:
            return (lst[first_pointer] , lst[last_pointer]), True

    return False
        


print(average_pair([1,2,3],2.5)) 
print(average_pair([1,3,3,5,6,7,10,12,19],8))
print(average_pair([-1,0,3,4,5,6], 4.1)) 
print(average_pair([],4)) 



print("....................................isSubsequence...............................................")

"""
Multiple Pointers - isSubsequence
Write a function called isSubsequence which takes in two strings and checks whether the characters in the 
first string form a subsequence of the characters in the second string.
In other words, the function should check whether the characters in the first string appear somewhere 
in the second string, without their order changing.

Examples:

isSubsequence('hello', 'hello world'); // true
isSubsequence('sing', 'sting'); // true
isSubsequence('abc', 'abracadabra'); // true
isSubsequence('abc', 'acb'); // false (order matters)
Your solution MUST have AT LEAST the following complexities:

Time Complexity - O(N + M)

Space Complexity - O(1)
"""

def is_subsequence(str1:str, str2:str):
    assert isinstance(str1,str) and isinstance(str2,str), "both arguements has to be strings"

    if len(str1)  == 0 or len(str2) == 0:
        return False

    
    if len(str1)  > len(str2):
        return False
    

    large_pointer = 0
    small_pointer = 0
    while large_pointer < len(str2):
        if str2[large_pointer] == str1[small_pointer]:
            small_pointer += 1
        large_pointer += 1
        if small_pointer == len(str1):
            return True

    return False



print(is_subsequence('hello', 'hello world'))
print(is_subsequence('sing', 'sting'))
print(is_subsequence('abc', 'abracadabra'))
print(is_subsequence('abc', 'acb'))