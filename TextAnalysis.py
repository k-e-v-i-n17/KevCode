def analyse_words_in_text(dict):
	import os,re
	path = 'test/'
	dirlist = os.listdir(path)

	for x in dirlist:
		abspath = os.path.join(path,x)
		if os.path.isfile(abspath):
			if os.path.splitext(abspath)[1] == '.txt':
				with open(abspath,'r')as f:
					data = f.read()
				result = re.split(r'[^a-zA-Z]', data)
				words = [x for x in result if x!='']
				items = dict([(i,words.count(i)) for i in words])
				items = sorted(items.iteritems(),key =lambda d:d[1],reverse = True)
				print abspath,'Most Common Word:',items[0][0],'Times Mentioned:',items[0][1],'Second Most Common:',items[1][0],'Times Mentioned:',items[1][1]

print(analyse_words_in_text(dict))
