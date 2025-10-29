# Fibbonacci Sequence
# this will return the sum of all even items in fibonacci seq
# upto your entered limit


limit = int(input("enter the limit: "))

def fibonacci_seq(limit):

	fibblist = [1]

	even_list = list()
	

	for i in range(limit):

		if fibblist[i] < 4000000:

			present_term = fibblist[i]

			previous_term = fibblist[i-1]
			
			next_term = previous_term + present_term

			fibblist.append(next_term)

			# check the value, if it is even , then add that value into even_list

			if next_term % 2 == 0:

				even_list.append(next_term)

		elif fibblist[i] >= 4000000:

			print(f"the value reached {fibblist[i]}.")

			break
		

	return fibblist, sum(even_list)


fibo_seq, sum_even_fib = fibonacci_seq(limit)	



print(sum_even_fib)






