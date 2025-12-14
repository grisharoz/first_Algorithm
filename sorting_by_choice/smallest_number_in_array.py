"""
    Finds the index of the smallest element in an array.
    This function iterates through all elements of the array and returns
    the index of the first occurrence of the smallest value.
    Parameters: arr (list): List of numbers to search
    Returns: int: Index of the smallest element in the array
    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(1)
"""

def find_smallest_number(arr):
    smallest_number = arr[0]  # Assume the first element is the smallest
    smallest_index = 0  # Store the index of the assumed smallest element

    # Iterate through all elements starting from the second one
    for i in range(1, len(arr)):
        # If we find an element smaller than the current smallest
        if arr[i] < smallest_number:
            smallest_number = arr[i]  # Update the smallest value
            smallest_index = i  # Update the index of the smallest element

    return smallest_index  # Return the index of the smallest element

"""
    Sorts an array in ascending order using the selection sort algorithm.
    Parameters: arr (list): Original list of numbers to be sorted
    Returns:list: New list sorted in ascending order
    Time Complexity: O(n²) where n is the length of the array
    Space Complexity: O(n) for the new array and its copy
"""

def selection_sort(arr):
    new_arr = []  # Create empty list for sorted elements
    copiedArr = list(arr)  # Create a copy of the original array for modification

    # Repeat for as many times as there are elements in the original array
    for i in range(len(copiedArr)):
        # Find the index of the smallest element in the remaining array
        smallest = find_smallest_number(copiedArr)

        # Remove the smallest element from the copied array and append it to the new array
        new_arr.append(copiedArr.pop(smallest))

    return new_arr  # Return the fully sorted array


# Test the selection sort function
print(selection_sort([3, 2, 1, 5, 6, 4, 7, 8, 9, 10]))
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
