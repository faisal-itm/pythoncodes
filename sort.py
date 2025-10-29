a =[3,4,5,1,2,9,10]
n = len(a)

for i in range(n):
	for j in range(0, n-i-1):
		if a[j] > a[j+1]:
			a[j], a[j+1] = a[j+1], a[j]

print(a)			