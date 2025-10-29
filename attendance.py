list=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","0","1","0","0","1","1","0","1","1","0","0","1","0","0","0","0"]

presnt = 0
absent = 0
for item in list:
	if item == "1":
		presnt+=1
	else:
		absent+=1
print(presnt, absent, presnt+absent, (presnt/(presnt+absent))*(100))