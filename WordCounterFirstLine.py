#_*_ encoding: utf-8 _*_
def count_words_first_line(file):
	import re
	while True:
		#text = raw_input("Press Enter")
		import re
		inputfile=file("test.txt");
		count=0;
		for line in inputfile.readlines():
			word=re.findall(r"\w+",line);
			count+=len(word);
			return "Total Word Count for the first line is "+ str(count)

print (count_words_first_line(file))
