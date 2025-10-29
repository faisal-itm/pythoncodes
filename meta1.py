'''
1. pick 2 dishes i & j
2. compare the temp of i and j and warm the cold one
3. first input T = test cases
4. for each test case enter the number of dishes (N=10 etc)
5. enter the dishes initial temprature = A = {A1, A2, A3 ... An}
6. enter the dishes target temprature = B = {B1, B2, B3, ... Bn}
-- for each test case N represents the total number of elements in A & B
-- if the inital temprature is greater than target temprature then throw error
'''
T = int(input("How many test you want to run? :  "))

if T >= 1 and T <= 95:
	for t in range(1, T+1):
		N= int(input("total number of dishes  --  "))

		input_string1 = input("Enter Initial Temprature of dishes: ")
		A = list(map(int, input_string1.split()))

		input_string2 = input("Enter Final or Targeted Temprature of dishes:  ")
		B = list(map(int, input_string2.split()))
		
		if N >= 1 and N <= 500000:
			if N == len(A) and N == len(B):
				K = 0
				result=list()

				for i in range(N):	
					if A[i] > B[i]:
						# impossible i.e initial temp > taget temp
						K = -1
						result=list()
						break
					elif A[i] == B[i]:
						continue 
					elif A[i] < B[i]:
						K += 1
						a,b=A[i],B[i]
						group=(a,b)
						result.append(group)

				print(f'Case #{t}: {K} ')
				for k in range(K):
					print(result[k][0], result[k][1])
			else:
				print("temp of dish is not equal to number of dishes")		
		else:
			print("Enter valid number of dishes; 1 to 500,000")	
else:
	print("Enter valid number for test")



