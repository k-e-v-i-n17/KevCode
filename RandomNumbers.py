def create_random_numbers(text):
	import random
	#text = raw_input("start?")
	st= '1234567890'
	x=st
	y='Random Numbers: '
	for j in range(0,10):
		y+=random.choice(x)

	return y

#if file == __main__:
for i in range(0,10):
	print(create_random_numbers('aaa'))
