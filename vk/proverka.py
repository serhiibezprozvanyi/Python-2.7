# -*- coding: utf-8 -*-# 
idvk = open('hoteleuropa_15.11.txt') # Список файлов всех участников в вк
a = open('hot15.11.2015.txt') # текст с страницы с ссылками
noreg = open('noreg.txt', 'a') #Список пользователей которые не выполнили задание или выполнили после того как был собран список всех участников 
b = list(a)
idvkk = []
vk = []
for i in b:
	if i.count('http') == True:
		idvkk.append(i)
	else:
		pass
re = '/'.join(idvkk)
spisok = list((set(re.split('/')) - set(['vk.com','https:','http:'])) - set(idvk))
for i in spisok:
	noreg.write(i)
a.close()
idvk.close()
noreg.close()