def filter_long_words_from_list(list):
	filter = [line.rstrip() for line in list]
while True:
	text = raw_input("please input:")
	for x in text:
		if x in text:
			print "Freedom"
			break
	else:
		print "Human Rights"
list = ['Human','rights','Rights']
print(list)
