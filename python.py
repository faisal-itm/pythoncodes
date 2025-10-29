arr = [8, 9,4,3,5,6,7]
n=len(arr)
# now what i want to do is to count it without using buildin funtion
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

aar = [9,7,8,3,2,4,1,5]
assk =bubble_sort(aar)

print(assk)