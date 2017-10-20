#coding:utf-8
def filter_url_from_html(compile):
	import re

	with open('1.html','rb')as f:
		data = f.read()
		
	data = data.replace('\r','').replace('\b','').replace('\n','')
	find = re.compile(r'href="(.*?)"')
	result = find.findall(data)
	for x in result:
		print x

print(filter_url_from_html(compile))
