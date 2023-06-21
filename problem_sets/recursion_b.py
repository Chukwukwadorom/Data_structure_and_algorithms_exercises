

print("........................................reverse.................................................. ")
"""
reverse
Write a recursive function called reverse which accepts a string and returns a new string in reverse.

// reverse('awesome') // 'emosewa'
// reverse('rithmschool') // 'loohcsmhtir'
"""

def reverse(string:str):
    if len(string)==0:
        return ""
    
    return string[-1] + reverse(string[:-1])

print(reverse("awesome"))
print(reverse("rithmschool"))



print("........................................is_palindrome.................................................. ")
"""isPalindrome
Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome 
(reads the same forward and backward). Otherwise it returns false.
isPalindrome('awesome') // false
// isPalindrome('foobar') // false
// isPalindrome('tacocat') // true
// isPalindrome('amanaplanacanalpanama') // true
// isPalindrome('amanaplanacanalpandemonium') // false
"""


def is_palindrome(string:str):

    def helper(string):
        if len(string)==0:
            return ""
        
        return string[-1] + helper(string[:-1])
    
    return helper(string) == string 

print(is_palindrome('awesome'))
print(is_palindrome('foobar'))
print(is_palindrome('tacocat')) 
print(is_palindrome('amanaplanacanalpanama'))
print(is_palindrome('amanaplanacanalpandemonium'))

print("........................................is_palindrome_b.................................................. ")

def is_palindrome_b(string:str):
    left = 0
    right = -1
    

    if len(string) <= 1: return True
    if string[left]!= string[right]: return False

    return is_palindrome_b(string[left+1: right])


print(is_palindrome_b('awesome'))
print(is_palindrome_b('foobar'))
print(is_palindrome_b('tacocat')) 
print(is_palindrome_b('amanaplanacanalpanama'))
print(is_palindrome_b('amanaplanacanalpandemonium'))


print("........................................some_recursive......................................................")
"""
someRecursive
Write a recursive function called someRecursive which accepts an array and a callback. 
The function returns true if a single value in the array returns true when passed to the callback. 
Otherwise it returns false.

//const isOdd = val => val % 2 !== 0;

// someRecursive([1,2,3,4], isOdd) // true
// someRecursive([4,6,8,9], isOdd) // true
// someRecursive([4,6,8], isOdd) // false
// someRecursive([4,6,8], val => val > 10); // false
"""




def is_odd(n):
    return (n % 2)!= 0

def greater_10(n):
    return n >  10

def some_recursive(lst:list, func):

    # print(lst)

    if len(lst) == 0:
        return False

    if func(lst[0]):
        return True

    return some_recursive(lst[1:], func) 

print(some_recursive([1,2,3,4], is_odd)) 
print(some_recursive([4,6,8,9], is_odd)) 
print(some_recursive([4,6,8], is_odd)) 
print(some_recursive([4,6,8], lambda val : val > 10))



print("........................................flatten.............................................................")
"""
flatten
Write a recursive function called flatten which accepts an array of arrays and 
returns a new array with all values flattened.

// flatten([1, 2, 3, [4, 5] ]) // [1, 2, 3, 4, 5]
// flatten([1, [2, [3, 4], [[5]]]]) // [1, 2, 3, 4, 5]
// flatten([[1],[2],[3]]) // [1,2,3]
// flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]) // [1,2,3]
"""

def flatten(old_arr):
    new_arr = []
    for element in old_arr:
        if isinstance(element, list):
            new_arr = new_arr + flatten(element)
        else:
            new_arr.append(element)
    	
   
    return new_arr

print(flatten([1, 2, 3, [4, 5] ])) 
print(flatten([1, [2, [3, 4], [[5]]]])) 
print(flatten([[1],[2],[3]]))
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))

print("........................................flatten_with_helper.............................................................")

def flatten_with_helper(lst:list):
  new_lst = []
  
  def helper(lst):
    for element in lst:
      if isinstance(element, list):
        helper(element)
      else:
        new_lst.append(element)
      
  helper(lst)    
  return new_lst

print(flatten_with_helper([1, 2, 3, [4, 5] ])) 
print(flatten_with_helper([1, [2, [3, 4], [[5]]]])) 
print(flatten_with_helper([[1],[2],[3]]))
print(flatten_with_helper([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))




print("........................................Capitalize first.............................................................")
"""
capitalizeFirst
Write a recursive function called capitalizeFirst. 
Given an array of strings, capitalize the first letter of each string in the array.

capitalizeFirst(['car','taco','banana']); // ['Car','Taco','Banana']

"""

def capitalize_first_helper(lst:list):
    new_lst = []

    def helper(lst):
        if len(lst)==0:
            return
        elem = lst[0].capitalize()
        new_lst.append(elem) 
        helper(lst[1:])


    helper(lst)
    return new_lst
    


print(capitalize_first_helper(['car','taco','banana']))


print("........................................Capitalize first, pure recursion.............................................................")


def capitalize_first(lst):
    new_list = []

    if len(lst)==0:
        return new_list
        
    new_list.append(lst[0].capitalize())
    
    return new_list + capitalize_first(lst[1:])


print(capitalize_first(['car','taco','banana']))


"""
nestedEvenSum
Write a recursive function called nestedEvenSum. 
Return the sum of all even numbers in an object which may contain nested objects.

nestedEvenSum(obj1); // 6
nestedEvenSum(obj2); // 10
"""
obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def nested_even_sum(obj):
    nos = []
    def helper(obj):
        for key in obj:
            if isinstance(obj[key],dict):
                helper(obj[key])
            elif isinstance(obj[key],int) and (obj[key] % 2 == 0):
                nos.append(obj[key])

    helper(obj)  
    return sum(nos)


print("........................................nested_even_sum, helper function.............................................................")
print(nested_even_sum(obj1))
print(nested_even_sum(obj2))


print("........................................nested_even_sum, pure recursion.............................................................")

def nested_even_sum_b(obj):
    total = 0
    for key, value in obj.items():
        if isinstance(value, dict):
            total += nested_even_sum_b(value)
        elif isinstance(value, int) and value % 2 == 0:
            total += value

    return total

print(nested_even_sum_b(obj1))
print(nested_even_sum_b(obj2))

print("........................................capitalize words, helper function.............................................................")
"""
capitalizeWords
Write a recursive function called capitalizeWords. 
Given an array of words, return a new array containing each word capitalized.
"""

def capitalize_words(lst:list):
    new_lst = []
    def helper(lst):
        if len(lst) == 0: return 
        new_lst.append(lst[0].upper())

        helper(lst[1:])

    helper(lst)
    return new_lst

words = ['i', 'am', 'learning', 'recursion'];
print(capitalize_words(words))

print("........................................capitalize words, recursion.............................................................")


def capitalize_words_b(lst:list):
    new_lst = []
    if len(lst)==0:
        return new_lst
    new_lst.append(lst[0].upper())
    return new_lst + capitalize_words_b(lst[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capitalize_words_b(words))


print("........................................stringify_numbers.............................................................")

        
"""
stringifyNumbers
Write a function called stringifyNumbers which takes in an object and 
finds all of the values which are numbers and converts them to strings. 
Recursion would be a great way to solve this!
"""

obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}


# stringifyNumbers(obj)


# {
#     num: "1",
#     test: [],
#     data: {
#         val: "4",
#         info: {
#             isRight: true,
#             random: "66"
#         }
#     }
# }


def stringify_numbers(obj):
    for key, value in obj.items():
        if isinstance(value, dict):
            stringify_numbers(value)
        elif isinstance(value, int):
            obj[key] = str(value)
    return obj 

        
print(stringify_numbers(obj))
    
"""
collectStrings
Write a function called collectStrings which accepts an object and returns an
 array of all the values in the object that have a typeof string
collectStrings(obj); // ["foo", "bar", "baz"])
"""

print("........................................collect_strings helper function.............................................................")

obj = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {
                "info": "bar",
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": "baz"
                    }
                }
            }
        }
    }
}


def collect_strings(obj):
    lst = []

    def helper(obj):
        for key, value in obj.items():
            if isinstance(value,dict):
                helper(value)
            elif isinstance(value,str):
                lst.append(value)

    helper(obj)
    return lst


print(collect_strings(obj))

print("........................................collect_strings recursion.............................................................")

def collect_strings_recursion(obj):
    lst = []
    for key, value in obj.items():
        if isinstance(value, dict):
            lst += collect_strings_recursion(value) 
        elif isinstance(value, str):
            lst.append(value)
    
    return lst  


print(collect_strings_recursion(obj))