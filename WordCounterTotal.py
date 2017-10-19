
def count_total_number_of_words(text):
	import re
	#text = raw_input("Count number of words?")
	with open("english.txt") as f:
		return len(re.findall("\w+", f.read()))

print(count_total_number_of_words(len))
