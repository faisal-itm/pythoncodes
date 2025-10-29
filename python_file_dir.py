'''

fp = open(r"/Users/faisalshahzad/Desktop/Python_filess/sample.txt" ,'r')


print(fp.read())

fp = open(r"/Users/faisalshahzad/Desktop/Python_filess/sample.txt" ,'w')

fp.write("Faisal Khan s/o Malak Amir M. Khan")


fp = open(r"/Users/faisalshahzad/Desktop/Python_filess/sample.txt" ,'r')
print(fp.read())

fp.close

'''
''
with open ('/Users/faisalshahzad/Desktop/Python_filess/sample.txt', 'r', encoding='utf-8') as file1, open ('/Users/faisalshahzad/Desktop/Python_filess/sample4.txt', 'x') as file4:

	for line in file1:
		file4.write(line)
file_4 = open ('/Users/faisalshahzad/Desktop/Python_filess/sample4.txt', 'r')

print(file_4.read())








