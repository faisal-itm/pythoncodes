#decorators

def decorated_function(original_function):
	#allow us to accept any arbitrary number of arguments

	def wrapper_funtion(*args, **kwargs):
		print("wrapper executed here, before {} funtion".format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_funtion


#@decorated_function
def display_info(name, age):
	print(" {} is of {} years old, and this run with arguments".format(name, age))

#display_info("ali", 19)






#class decorators

 


#@decorated_class
def display_info(name, age):
	print(" {} is of {} years old, and this run with arguments".format(name, age))

#display_info("ali", 19)



def logging_funtion(original_function):

	import logging 
	logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

	def wrapper_funtion(*args,**kwargs):
		
		logging.info(
			"ran with arguments {}, and Kwargs {}".format(*args,**kwargs))
	
		return original_function(*args, **kwargs)
	
	return wrapper_funtion




@logging_funtion

def display_info(name, age):
	print(" {} is of {} years old, and this run with arguments".format(name, age))




def time_funtion(original_function):

	import time

	def wrapper_funtion(*args, **kwargs):

		t1 = time.time()

		result= original_function(*args, **kwargs)

		t2 = time.time() - t1
 
		print ('{} ran in this much {} sec'.format(original_function.__name__, t2))


		return result

	return wrapper_funtion


import time

@time_funtion
def demo_funtion(a,b):

	time.sleep(0)
	sum1=a+b
	m1=a*b 
	return sum1, m1

ahm=demo_funtion(9,8)
print(ahm)



print(demo_funtion.__name__)




