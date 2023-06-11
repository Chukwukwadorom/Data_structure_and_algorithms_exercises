"""
Write a function called same, which accepts two arrays. 
The function should return true if every value in the array has it's corresponding value squared in the second array. 
The frequency of values must be the same
"""


# naive implementation
def same(ls1:list, ls2:list):

    assert (isinstance(ls1, list) and isinstance(ls2, list)), "the arguements has to be lists"
                
    for element in ls1:
        assert (isinstance(element, int) or isinstance(element, float)), "list elements must be ints or floats"
        if element**2 not in ls2:
            return False
        else:
            ls2.remove(element**2)
    return True   



print(same([1,2,3,4],[1,4,9,16]))
print(same([1,2,1,4],[4,9,16,4]))
print(same([1,2,1],[4,1,1]))

print("\n")

print(same([1,2,3], [4,1,9]))
print(same([1,2,3], [1,9]))
print(same([1,2,1], [4,4,1])) 

try:
    same([1,2,"kedu"],[1,4,1])
except:
    print("some error occured")
else:
    print("succesfull")
finally:
    print("bye")