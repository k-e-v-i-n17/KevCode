#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jinyang'
def most_common_word(file):
	import glob
	from collections import Counter, OrderedDict

	def mostImporantWord(filePath):
		for file in glob.glob(filePath + '*.txt'):
			calcTimes(file)

	def calcTimes(fileName):
		cc = Counter()
		file = open(fileName)
		str = file.read()
		words = str.split('\n')
		for i in words:
			cc[i] = cc[i] + 1
		maxInDict(cc)

	def maxInDict(dict):
		max = 0
		for key, value in dict.items():
			if value > max:
				max = value
				goal = key
		print goal + " is featured " + str(max) + " times"

	if __name__ == '__main__':
		mostImporantWord('diaries/')
print(most_common_word(file))
