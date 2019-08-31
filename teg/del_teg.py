# -*- coding: cp1251 -*-
import os

logfile = open(ur'rezult-foto.txt', 'a') # Список файлов всех 
log = list(open(ur'foto-site.txt'))
linkimg = []

for i in log:
		if i.count('src') == True:
			linkimg.append(i)
		else:
			pass

for i in linkimg:
		logfile.write(i + '\n')
logfile.close()