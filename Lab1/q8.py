 # Q8. Store N number of integers in a List variable one by one. Search the particular element in list using binary search using for-else loop.

def store():
  list1 = []
  for i in range(n):
    x = int(input("Enter element: "))
    j=0
    while(j<len(list1) and list1[j]<x):
      j+=1
    list1.insert(j,x)
  return list1


def binary_search(list, n, key):
    low = 0
    high = n - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list[mid] < key:
            low = mid + 1
        elif list[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

list = []
n = int(input("Enter number of elements : "))
list = store()
print(list)
key = int(input("Enter element to search : "))
result = binary_search(list, n, key)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list")