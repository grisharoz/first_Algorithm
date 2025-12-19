#we want to find sum in the array
def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])
print("Total:",sum([1,2,3]))

#counting elements in the array
def count_elements(arr):
    if len(arr) == 0:
        return 0
    return 1 + count_elements(arr[1:])
print("Count: ",count_elements([1,2,3]))

#find max value in the array
def max_value(arr):
    max=0
    if len(arr) == 0:
        return 0
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max
print("Max is number",max_value([1,2,3,4,5]))
