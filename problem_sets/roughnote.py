"""

Binary Search Exercise
Write a function called binarySearch which accepts a sorted array and a
 value and returns the index at which the value exists. Otherwise, return -1.

This algorithm should be more efficient than linearSearch - you can read how to implement it here -
 https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search and 
 here - https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/

Examples:

binarySearch([1,2,3,4,5],2) // 1
binarySearch([1,2,3,4,5],3) // 2
binarySearch([1,2,3,4,5],5) // 4
binarySearch([1,2,3,4,5],6) // -1
binarySearch([
  5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 
  40, 44, 64, 79, 84, 86, 95, 96, 98, 99
], 10) // 2
binarySearch([
  5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 
  40, 44, 64, 79, 84, 86, 95, 96, 98, 99
], 95) // 16
binarySearch([
  5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 
  40, 44, 64, 79, 84, 86, 95, 96, 98, 99
], 100) // -1
"""

print("............................................Binary Search.....................................................")

def binary_search(lst, elem):
    left = 0
    right = len(lst)-1

    while left <= right:
        mid = (left + right)//2

        if lst[mid]== elem:
            return mid
        elif elem > lst[mid]:
            left = mid +1
        else:
            right = mid -1 

    return -1


print(binary_search([1,2,3,4,5],2))
print(binary_search([1,2,3,4,5],3))
print(binary_search([1,2,3,4,5],5))
print(binary_search([1,2,3,4,5],6))
print(binary_search([
  5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 
  40, 44, 64, 79, 84, 86, 95, 96, 98, 99
], 10)) 
print(binary_search([
  5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 
  40, 44, 64, 79, 84, 86, 95, 96, 98, 99
], 95) )
print(binary_search([
  5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 
  40, 44, 64, 79, 84, 86, 95, 96, 98, 99
], 100)) 


print("..................................naive string search....................................................")

def naive_string_search(string1, string2):
  count = 0
  win = len(string2)
  if win > len(string1): return 0

  for idx in range(len(string1)):
    for win in range(len(string2)):
      if string1[idx] == string2[win]:
        if string1[idx:idx+len(string2)] == string2:
          count += 1
        else:
          break
  
  return count

print(naive_string_search('wowzmg', 'omg'))
print(naive_string_search('wowomgomgzomg', "omg"))

print("..................................naive? string search....................................................")
def naive_string_search_b(string1, string2):
  
  count = 0
  win = len(string2)

  if win > len(string1): return 0
  for idx in range(len(string1)):

    if string1[idx] == string2[0] and string1[idx:idx+win] == string2:
      count += 1
    else:
      # review this later. check the steps hopped
      idx += win
    
  return count


print(naive_string_search_b('wowzmg', 'omg'))
print(naive_string_search_b('wowomgomgzomg', "omg"))
print(naive_string_search_b('ggggggggggggg', "g"))
print(naive_string_search_b('lorie loled', "lo"))
print(naive_string_search_b('lorie loled', "po"))
print(naive_string_search_b("lolomglolololrofl", "lolol"))
print(naive_string_search_b("lololgmmlolololrofl", "lolol"))
print(naive_string_search_b("lolomllllololrofl", "lolol"))

## to do:
## implement naive string search with nexted loop
## implement string search with KMP 




print("..........................merge function............................................")

def merge(ls1,ls2):
  lp = 0
  rp = 0
  new_lst = []
  while lp < len(ls1) and rp < len(ls2):
    if ls1[lp] < ls2[rp]:
      new_lst.append(ls1[lp])
      lp += 1
    else:
      new_lst.append(ls2[rp])
      rp += 1

    # print(lp,rp)

  new_list = new_lst + ls1[lp:] + ls2[rp:]

  return new_list


print("merged: ", merge([1,10,50],[2,10,14,99,100,200])) 

print("......................................merge sort...................................")

import numpy as np

def merge_sort(lst):
  length = len(lst)
  m = length//2

  if length <= 1:
    return lst
  else:
    a = merge_sort(lst[:m])
    b = merge_sort(lst[m:length])
    return (merge(a,b))


# ls = list(np.random.randint(size=10000))
print("merge_sort: ", merge_sort([39, 12, 18, 85, 72, 10, 2, 18]))
# print("merge_sort: ", merge_sort(ls))


print(".......................pivot helper................................................")

def pivot_helper(lst, start, end):
  #  using first element as pivot
  pivot = start 
  less_count = 0

  for a in range(start+1, end):
    if lst[a] <  lst[pivot]:
      less_count += 1
      temp = lst[a]
      lst[a] = lst[less_count]
      lst[less_count] = temp
      

  lst[0], lst[less_count] = lst[less_count], lst[pivot]
  
  return  less_count

data = [39, 12, 18, 85, 72, 10, 2, 18]
print("pivot helper:", pivot_helper(data, 0, len(data)-1 ))
data = [4,8,2,1,5,7,6,3]
print("pivot helper:", pivot_helper(data, 0, len(data)-1 ))
data = [4, 6, 9, 1, 2, 5]
print("pivot helper:", pivot_helper(data, 0, len(data)-1 ))

def quick_sort(lst, start, end):
  
  # very buggy
  if start < end:
    mid_point = pivot_helper(lst, start, end)
    print(start, end, mid_point, lst[mid_point], lst)
    left = quick_sort(lst, start=0, end=mid_point-1)
    right = quick_sort(lst, start=mid_point+1, end = end)
  
  return lst
   

  
# data = [39, 12, 18, 85, 72, 10, 2, 18]
# print("quicksort:", quick_sort(data, 0, len(data)-1))

data2 = [4, 6, 9, 1, 2, 5]
print("quicksort:", quick_sort(data2, 0, len(data)-1))

    


