from math import  log


def bubble_sort(lst):
    # very unoptimized
    temp = None
    length= len(lst)
    for a in range(length):
        for b in range(length):
            # print(lst[a], lst[b], lst)
            if lst[b] > lst[a]:
                temp = lst[a]
                lst[a] = lst[b]
                lst[b] = temp
        # print("one pass completed")

    return lst

def bubble_sort_b(lst):
    #still unoptimized
    temp = None
    length= len(lst)
    for a in range(length):
        for b in range(a+1, len(lst)):
            # print(lst[a], lst[b], lst)
            if lst[a] > lst[b]:
                temp = lst[a]
                lst[a] = lst[b]
                lst[b] = temp
        # length-=1

    return lst


print("bubble_sort", bubble_sort([4,2,7,1,9,4,9,1,0,10,79,5]))
print("bubble_sort",bubble_sort([39, 12, 18, 85, 72, 10, 2, 18]))


def bubble_sort_optimized(lst):

    not_swaped = True

    for a in range(len(lst), -1, -1):
        for b in range(a-1):
            if lst[b] > lst[b+1]:
                temp = lst[b]
                lst[b] = lst[b+1]
                lst[b+1]= temp
                not_swaped = False
        if not_swaped: break
    return lst

print("bubble_sort_optimized", bubble_sort_optimized([39, 12, 18, 85, 72, 10, 2, 18]))
print("bubble_sort_optimized", bubble_sort_optimized([1,2,3,4,6,5]))

def selection_sort(lst):

    
    for a in range(len(lst)):
        min_idx = a
        for b in range(a+1, len(lst)):
            if lst[b] < lst[min_idx]:
                min_idx = b 
        temp = lst[a]
        lst[a] = lst[min_idx]
        lst[min_idx] = temp 
    return lst

print("selection sort", selection_sort([39, 12, 18, 85, 72, 10, 2, 18]))




print("...................................radix sort.................................................")

def idx_element(numb, idx):
    return (abs(numb) // 10 **idx) % 10

def most_digit(lst):
    max_digit = 0
    for num in lst:
        max_digit = max(log(num), max_digit)

    return max_digit

print(most_digit([23,4555,1,9,5]))


def radix_sort():
    pass
    

