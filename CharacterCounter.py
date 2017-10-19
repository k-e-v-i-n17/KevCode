def length_of_char_and_number_of_unique_char(list):
	filter = [line.rstrip() for line in list]

while True:
    text = raw_input("Enter word or number")
    for x in text:
        if x in text:
            print len(x)
            text = text.replace(x, '*'*len(x))
    print text + "= Total Length"
