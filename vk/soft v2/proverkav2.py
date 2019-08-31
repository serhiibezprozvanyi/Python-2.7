# -*- coding: utf-8 -*-# 
from datetime import datetime, date, time
datafile = 'vk_{0}_.txt'.format(datetime.strftime(datetime.now(), "%Y_%m_%d"))
idvk = open('eurabota-uchasniki-24-03-2017.txt', 'r') # Список файлов всех участников в вк
a = open('seo.txt') # копипаст стр сеоспринта
noreg = open('noreg.txt', 'a') #Список пользователей которые не выполнили задание или выпонили после того как был собран список всех участников 
seospint = open(datafile, 'a') # Чистый список айпи участников
b = list(a)
bb = list(idvk)
bb = ''.join(bb)
idvkk = []
regvk = []
for i in b:
	if i.count('http') == True:
		idvkk.append(i)
	else:
		pass
re = ','.join(idvkk)
for i in re.split('\n'):
	regvk.append(i.split('/')[-1])
spisok = set(regvk) -  set(bb.split('\n'))

for i in spisok:
	noreg.write(i + '\n')
for i in regvk:
	seospint.write(i + '\n')
a.close()
idvk.close()
noreg.close()
seospint.close()


