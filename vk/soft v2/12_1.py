# -*- coding: utf-8 -*-#

def myfunc(slovo):
	s = {}
	delsim = ["...", "!!!", "???", ".", ",", "(", ")", ".", '"', "?", "!", ":", ";", "#", "@", "$", "№", "-", "*", "&", "%"]
	nosim = slovo
	for i in delsim:
		nosim = nosim.replace(i, '')
	for i in nosim.split(' '):
		if nosim.split(' ').count(i) > 1:
			s[i] = nosim.split(' ').count(i)
	for i in s:
		print u'слово: {0}|	{1} раз повторяеться'.format(i, s[i])