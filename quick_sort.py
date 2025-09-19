"""
Quick sort is another divide and conquer algorithm, but unlike merge sort, it uses a pivot element to partition
the array into sub arrays. The elements smaller than the pivot go to the left, and the elements greater than the
pivot go to the right. The process is recursively applied to the sub arrays until the entire array is sorted.

Steps of Quick Sort:
Choose a pivot: Pick an element from the array (commonly the first, last, or middle element).
Partitioning: Rearrange the elements so that:
All elements smaller than the pivot go to the left.
All elements larger than the pivot go to the right.
Recursion: Recursively apply quick sort to the left and right sub arrays.
Concatenate: Combine the sorted sub arrays and the pivot to form the final sorted array.
"""
from pandas import pivot


def quick_sort(arr):
    # Base case: If the array has only one element or is empty, it is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Choose a pivot (here we choose the last element)
    pivot = arr[-1]

    # Step 2: Partition the array into two halves
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    # Step 3: Recursively apply quick sort to the left and right subarrays
    return quick_sort(left) + [pivot] + quick_sort(right)


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)



# def prep_quick(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[-1]
#
#     left = [x for x in arr[:-1] if x <= pivot]
#     right = [x for x in arr[:-1] if x>pivot]
#
#     return prep_quick(left) + [pivot] + prep_quick(right)
# print(prep_quick([1,5,2,3,1]))