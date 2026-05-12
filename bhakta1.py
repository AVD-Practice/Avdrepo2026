#search number useing binary search 
#a = [10, 20, 30, 40, 50]
def binary_search(a, key):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low+high)//2
        if a[mid] == key:
            return mid 
        elif a[mid]<key:
            low = mid+1
        else:
            high = mid-1
    return -1 
a = [10, 20, 30, 40, 50]
key = int(input("Enter the number you want to search : "))
res = binary_search(a, key)
if res != -1:
    print("number is present in the list")
else:
    print("number is not present in the list")