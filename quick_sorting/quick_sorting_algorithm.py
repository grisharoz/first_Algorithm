#quick sort with pivot element
def quick_sort(array):
    if len(array) < 2:
        return array
    pivot=array[0]
    less=[i for i in array[1:] if i<=pivot]
    greater=[i for i in array[1:] if i>pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([2,8,4,1,5,7,8,5,7,0]))