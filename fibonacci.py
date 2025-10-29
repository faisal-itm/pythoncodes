# Fibbonacci Sequence

N = int(input("enter the limit: "))

def fibonacci_seq(N):
	fibblist = [1]


	for i in range(N):

		present_term = fibblist[i]
		previous_term = fibblist[i-1]
		
		next_term = previous_term + present_term
		new_term = next_term

		fibblist.append(new_term)
		

	return fibblist


resulted_fibb = fibonacci_seq(N)

# Do you want to list all the sequence or a specific nth value in the Sequence
# enter the number to display the nth term value of the Sequence

print("To display whole list enter the '0' else enter the nth term number.")

nth_value = int(input("Enter the number for nth value : "))

if nth_value != 0:

	print(f'the requested term in the fibonacci Seq is ▶︎ {resulted_fibb[nth_value]}')

else:
	print(resulted_fibb)






