def input_and_output(input):
	s=input()
	with open('filtered_words.txt') as f:
		word_filter=set()
		for w in f.readlines():
			word_filter.add(w.strip())
	while True:
		if s == 'exit':
			break
		if s in word_filter:
			return('Freedom')
		else:
			return('Human Rights')
print(input_and_output(input))
