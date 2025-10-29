# Fibbonacci Sequence
# this will return the sum of all even items in fibonacci seq
# upto your entered limit


limit = int(input("enter the limit: "))

def fibonacci_seq(limit):

	# we define fibonacci list with first value
	fibblist = [1]

	# this list will store all the even values in the fibonacci seq
	even_list = list()
	

	for i in range(limit):

		present_term = fibblist[i]

		# for the first term i-1 = 0-1 = -1 & 
		# the fibblist[-1] = fibblist[1] 
		# because for first term the list has only one item

		previous_term = fibblist[i-1]
		
		next_term = previous_term + present_term

		new_term = next_term

		fibblist.append(new_term)

# check the value, if it is even , then add that value into even_list

		if fibblist[i] % 2 == 0:

			even_list.append(new_term)
		

	return fibblist, sum(even_list)


fibo_seq, sum_even_fib = fibonacci_seq(limit)	



print(sum_even_fib)






