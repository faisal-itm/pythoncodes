array = [int(x) for x in input("Enter the numbers").split()]

print(f'unsorted array: {array}')


for i in range(len(array)):
	for j in range(0, len(array)-i-1):
		if array[j] > array[j+1]:
			array[j], array[j+1] = array[j+1], array[j]

print(f'sorted array : {array}')