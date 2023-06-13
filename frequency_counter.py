"""
This pattern uses objects or sets to collect values/frequencies of values
This can often avoid the need for nested loops or O(N^2) operations with arrays / strings

Example:Write a function called same, which accepts two arrays. 
The function should return true if every value in the array has it's corresponding value squared in the second array. 
The frequency of values must be the same
"""


# naive implementation
def same_naive(ls1:list, ls2:list):

    """ Time Complexity -O(N^2)"""

    assert (isinstance(ls1, list) and isinstance(ls2, list)), "the arguements has to be lists"
                
    for element in ls1:
        assert (isinstance(element, int) or isinstance(element, float)), "list elements must be ints or floats"
        if element**2 not in ls2:
            return False
        else:
            ls2.remove(element**2)
    return True   


def same_better(ls1:list, ls2:list):

    """Time Complexity - O(n)"""
    assert (isinstance(ls1, list) and isinstance(ls2, list)), "the arguements has to be lists"
    
    if len(ls1) != len(ls2):
        return False

    freq_dict1 ={}
    freq_dict2 ={}
    for element in ls1:
        assert (isinstance(element, int) or isinstance(element, float)), "list elements must be ints or floats"
        if freq_dict1.get(element,None):
            freq_dict1[element]+=1
        else:
            freq_dict1[element] = 1

    for element in ls2:
        assert (isinstance(element, int) or isinstance(element, float)), "list elements must be ints or floats"
        if freq_dict2.get(element,None):
            freq_dict2[element]+=1
        else:
            freq_dict2[element] = 1

    for element in freq_dict1:
        if not freq_dict2.get(element**2,None):
            return False
        elif freq_dict2[element**2] != freq_dict1[element]:
            return False  

    return True









# print(same_naive([1,2,3,4],[1,4,9,16]))
# print(same_naive([1,2,1,4],[4,9,16,4]))
# print(same_naive([1,2,1],[4,1,1]))

# print("\n")

# print(same_naive([1,2,3], [4,1,9]))
# print(same_naive([1,2,3], [1,9]))
# print(same_naive([1,2,1], [4,4,1])) 

# try:
#     same_naive([1,2,"kedu"],[1,4,1])
# except:
#     print("some error occured")
# else:
#     print("succesfull")
# finally:
#     print("bye")



# print(same_better([1,2,3,4],[1,4,9,16]))
# print(same_better([1,2,1,4],[4,9,16,4]))
# print(same_better([1,2,1],[4,1,1]))

# print("\n")

# print(same_better([1,2,3], [4,1,9]))
# print(same_better([1,2,3], [1,9]))
# print(same_better([1,2,1], [4,4,1])) 

# try:
#     same_better([1,2,"kedu"],[1,4,1])
# except:
#     print("some error occured")
# else:
#     print("succesfull")
# finally:
#     print("bye")

############################################..ANAGRAMS..#############################################################
"""
Given two strings, write a function to determine if the second string is an anagram of the first. 
An anagram is a word,phrase, or name formed by rearranging the letters of another, 
such as cinema, formed from iceman
validAnagram('', '') // true
validAnagram('aaz', 'zza') // false
validAnagram('anagram', 'nagaram') // true
validAnagram("rat","car") // false) // false
validAnagram('awesome', 'awesom') // false
validAnagram('qwerty', 'qeywrt') // true
validAnagram('texttwisttime', 'timetwisttext') // true

"""

def validAnagramNaive(str1:str, str2:str):
    assert (isinstance(str1, str) and isinstance(str2, str)), "the arguements has to be strings" 
    # assert str1 != str2, "the string  has to be different"
    if len(str1) != len(str2):
        return False
    str2 = list(str2)
    for char in str1:
        if char in str2:
            str2.remove(char)
        else:
            return False
    return True


# print(validAnagramNaive('', '')) 
# print(validAnagramNaive('aaz', 'zza')) 
# print(validAnagramNaive('anagram', 'nagaram')) 
# print(validAnagramNaive("rat","car")) 
# print(validAnagramNaive('awesome', 'awesom'))
# print(validAnagramNaive('qwerty', 'qeywrt')) 
# print(validAnagramNaive('texttwisttime', 'timetwisttext')) 


def validAnagram(str1:str, str2:str):
    assert (isinstance(str1, str) and isinstance(str2, str)), "the arguements has to be strings"
    
    if len(str1) != len(str2):
        return False

    freq_dict1 = {}
    freq_dict2 = {}

    for char in str1:
        if freq_dict1.get(char, None):
            freq_dict1[char] += 1
        else:
            freq_dict1[char] = 1

    for char in str2:
        if freq_dict2.get(char, None):
            freq_dict2[char] += 1
        else:
            freq_dict2[char] = 1

    for char in freq_dict1:
        if not char in freq_dict2:
            return False
        elif freq_dict1[char] != freq_dict2[char]:
            return False

    return True



print(validAnagram('', '')) 
print(validAnagram('aaz', 'zza')) 
print(validAnagram('anagram', 'nagaram'))
print(validAnagram("rat","car")) 
print(validAnagram('awesome', 'awesom'))
print(validAnagram('qwerty', 'qeywrt')) 
print(validAnagram('texttwisttime', 'timetwisttext')) 