#  1 <= T <=100 the number of test you want to run
# 1 <= N <= 1000 the number of people / sample group
# total money is 10^9 = 1000000000


Test = int(input("How many test(s)? : "))

Money = 10**9

if Test <= 100:
	for i in range(Test):
		people = int(input("How many peoples: "))
		total_payout = 0

		if people <= 1000:

			T_and_D = str(input(f'in what order {people} had T or D ?  ')).upper()

			if total_payout<Money:
	
				current_pot = 1
				

				for person in T_and_D:

					if person =='D':

						current_pot = current_pot * 2
						
					elif person =='T':

						total_payout = total_payout + current_pot
						current_pot = 1

				print(f'Mr. Bren have to pay {total_payout}')		
			else:

				print(f"your payout {total_payout} exceeds the limit {Money}")	
				break	
		else:
			print("too much people")
else:
	print("100 is limit for test")			
		
	



