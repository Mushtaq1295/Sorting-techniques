""""
Steps:
Start with the first element.
Find the smallest element in the unsorted part of the list.
Swap it with the first unsorted element.
Move the boundary between sorted and unsorted by one position to the right.
Repeat the process until the entire list is sorted.

"""
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
