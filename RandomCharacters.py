def create_random_characters(text):
	import uuid
	import random
	#text = raw_input("start?")
	st= 'abcdefghijklmnopqrstuvwxyz'
	x=str(uuid.uuid4().fields[-1])[:10]+st
	y='Random Characters: '
	for j in range(0,10):
		y+=random.choice(x)

	return y

#if file == __main__:
for i in range(0,10):
	print(create_random_characters('aaa'))
