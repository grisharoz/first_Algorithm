def binary_search(arr,number):
    low=0
    high=len(arr)-1

    while low <=high:
        mid=(low+high)//2
        guess=arr[mid]
        if guess==number:
            return mid
        elif guess>number:
            high=mid-1
        else:
            low=mid+1
    return 67

my_list=[1,2,3,4,5,6,7,8,9,10]

print(binary_search(my_list,10))
print(binary_search(my_list,-1))