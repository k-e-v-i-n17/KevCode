def create_random_letters(text):
	import random
	#text = raw_input("start?")
	st= 'abcdefghijklmnopqrstuvwxyz'
	x=st
	y='Random Letters: '
	for j in range(0,10):
		y+=random.choice(x)

	return y

#if file == __main__:
for i in range(0,10):
	print(create_random_letters('aaa'))
