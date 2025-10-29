'''
Problem
sum of the multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of any number, e.g multiple of 3 or 5. The sum of these multiples is $23$.</p>
Find the sum of all the multiples of $3$ or $5$ below $1000$.
----------------------------
'''

#N = int(input("Enter the Number upto which you want to find sum of multiples:  "))
#M = int(input("Multiples of : "))

def find_multiple():
	total_sum=0
	for i in range(1, 1000):
		if i % 3 == 0 or i % 5 == 0:
			total_sum += i
	return total_sum		

total_sum = find_multiple()
print(total_sum)

#print(f'The total sum of all the multiples of 3 or 5 below {N} is = {total_sum}')

# Here is the same solution but with list comprehension

print(sum(n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0))

print(total_sum)
