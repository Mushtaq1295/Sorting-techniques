
"""
Steps:
Start with the second element (the first element is considered sorted).
Compare the current element with the elements in the sorted portion.
Move elements that are greater than the current element one position to the right.
Insert the current element in its correct position.
Repeat until the entire list is sorted.

Original array: [12, 11, 13, 5, 6]
[11, 12, 13, 5, 6]
[11, 12, 13, 5, 6]
[5, 11, 12, 13, 6]
[5, 6, 11, 12, 13]

"""

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key at the correct position
        arr[j + 1] = key
        print(arr)

# Example usage
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)
