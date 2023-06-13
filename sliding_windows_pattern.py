"""
This pattern involves creating a window which can either be an array or number from one position to another
Depending on a certain condition, the window either increases or closes (and a new window is created)

Very useful for keeping track of a subset of data in an array/string etc
An Example: Write a function called maxSubarraySum which accepts an array of integers and a number called n. 
The function should calculate the maximum sum of n consecutive elements in the array
"""

def max_subarray_sum_naive(lst:list, n, step=1):
    """ Time Complexity - O(N^2) """

    if len(lst)== 0 or n > len(lst):
        return [], None
    sum_dict = {}
    start = 0
    end = n
    idx = 0
    while idx != len(lst):
        window =  tuple(lst[start:end])
        sum_dict[window] =  sum(window)

        start += step
        end += step

        idx += 1
    
    cur_max = float('-inf')
    cur_key  = None
    for key, value in sum_dict.items():
        if value > cur_max:
            cur_max = value
            cur_key = key

    return cur_key, cur_max




print("........................naive implemtation...............................")

print(max_subarray_sum_naive([1,2,5,2,8,1,5],2)) 
print(max_subarray_sum_naive([1,2,5,2,8,1,5],4)) 
print(max_subarray_sum_naive([4,2,1,6],1))
print(max_subarray_sum_naive([4,2,1,6,2],4)) 
print(max_subarray_sum_naive([],4)) 



def max_subarray_sum_naive_b(lst:list, n):
    """ Time Complexity - O(N^2) """
    if len(lst)== 0 or n > len(lst):
        return None

    max_numb = float('-inf')
    for a in range(len(lst)-n+1):
        accum = 0
        for b in range(n):
            accum += lst[a+b]
        if accum > max_numb:
            max_numb = accum

    return max_numb

print("........................another naive implemtation...............................")
print(max_subarray_sum_naive_b([1,2,5,2,8,1,5],2)) 
print(max_subarray_sum_naive_b([1,2,5,2,8,1,5],4)) 
print(max_subarray_sum_naive_b([4,2,1,6],1))
print(max_subarray_sum_naive_b([4,2,1,6,2],4)) 
print(max_subarray_sum_naive_b([],4))



    
def max_subarray_sum(lst:list, n:int):
    """ Time Complexity - O(N) """
    assert (isinstance(lst,list) and isinstance(n, int)), f"arguement {lst} is expected to be a list and {n} and integer"

    if len(lst)== 0 or n > len(lst):
        return None

    running_sum = 0
    for index in range(n):
        running_sum += lst[index]

    max_sum = running_sum
    for index in range(n, len(lst)):
        running_sum = (running_sum + lst[index]) - lst[index-n]
        # if running_sum > max_sum:
        #     max_sum = running_sum
        max_sum = max(max_sum,running_sum)
        
    return max_sum




print("........................a better implemtation...............................")
print(max_subarray_sum([1,2,5,2,8,1,5],2)) 
print(max_subarray_sum([1,2,5,2,8,1,5],4)) 
print(max_subarray_sum([4,2,1,6],1))
print(max_subarray_sum([4,2,1,6,2],4)) 
print(max_subarray_sum([],4))



    

