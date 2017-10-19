def heads_or_tails(text):
	import random
	#text = raw_input("start?")
	st= 'heads', 'tails'
	x=st
	y='Coin Flipped: '
	for j in range(0,1):
		y+=random.choice(x)

	return y

#if file == __main__:
for i in range(0,1):
	print(heads_or_tails('aaa'))
