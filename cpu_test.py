# this calculate the time the CPU take for carring calculation upto 10000000 

import time
start_time = time.time()
x=1
n=100000000000
for i in range(1, n):

	x *= i
	print(f'{x}\n)
	