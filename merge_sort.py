"""
Merge sort is a divide and conquer algorithm that divides an array into smaller sub arrays, sorts each subarray,
and then merges them back together in the correct order. It's a recursive algorithm that works in two steps:

Divide: Split the array into two halves until each subarray contains a single element (since a single element is always sorted).
Conquer (Merge): Combine the sub arrays by merging them back together in the correct order.
Steps of Merge Sort:
Recursion: Break the array down into smaller arrays (divide step).
Merge: Combine the smaller sorted arrays (conquer step).
"""

def merge_sort(arr):
    # Base case: If the array has only one element or is empty, it is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Step 4: Compare elements from both halves and merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Step 5: Append any remaining elements from the left half
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # Step 6: Append any remaining elements from the right half
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
