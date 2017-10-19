def filter_words_from_list(compile):
	import re

	filter_words=''
	with open('filtered_words.txt','r') as f:
		for line in f:
			filter_words += line.strip()+'|'

	filter_words = filter_words.strip('|')
	fw = re.compile(filter_words)

	content= "love"
	if(fw.search(content)):
		print "Word Found"
	else:
		print "Word Not Found"
		
print(filter_words_from_list(compile))

