#write a program to perform search activity using linear and binary search
#linear search
def linear_search(x,target):
    for i in x:
        if(i==target):
            print("Yes")
        else:
            print("No")


def binary(x, target):
    left = 0
    right = len(x) - 1
    while left <= right:
        mid = (left + right) // 2
        if x[mid] == target:
            return mid
        elif x[mid] < target:
            left = mid + 1
        else:
            right = mid - 1  
    return -1

x = [1, 2, 3, 5, 40]
target = 40
linear_search(x,target)
print("")
print(binary(x, target))

