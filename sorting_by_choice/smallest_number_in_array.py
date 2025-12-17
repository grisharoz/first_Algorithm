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
    smallest_number = arr[0] 
    smallest_index = 0  

  
    for i in range(1, len(arr)):
        if arr[i] < smallest_number:
            smallest_number = arr[i]  
            smallest_index = i 
    return smallest_index 

"""
    Sorts an array in ascending order using the selection sort algorithm.
    Parameters: arr (list): Original list of numbers to be sorted
    Returns:list: New list sorted in ascending order
    Time Complexity: O(n²) where n is the length of the array
    Space Complexity: O(n) for the new array and its copy
"""

def selection_sort(arr):
    new_arr = []  
    copiedArr = list(arr)  
    
    for i in range(len(copiedArr)):
        smallest = find_smallest_number(copiedArr)
        new_arr.append(copiedArr.pop(smallest))

    return new_arr 

print(selection_sort([3, 2, 1, 5, 6, 4, 7, 8, 9, 10]))
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
