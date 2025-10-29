# sum of all odd squares

N = int(input("Enter the Number upto which you want to Add the odd squares:  "))	


def sum_of_odd_squares(N):
	sum_of_squares=0

	for i in range(1, N+1):
		if i % 2 != 0:
			square = i * i
			sum_of_squares += square
	return sum_of_squares


print(sum_of_odd_squares(N))