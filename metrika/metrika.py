# -*- coding: utf-8 -*-

m = list(open(ur'ru2015.csv'))

r =[]

for i in m[2:]:
	i = i.split(',')
	r.append([i[0].strip(' " '), int(float(i[1].strip(' " ')))])
	
def domain(url):
	summa = 0
	for i in r:
		if i[0].count(url):
			summa += i[1]
	return summa
	

print u'Количество заходов в месяц с домена resorts-krym.ru:'	
print domain('resorts-krym.ru')	
print u'Количество заходов в месяц с домена resorts-crimea.com:'	
print domain('resorts-crimea.com')
print  u'Количество заходов в месяц с домена 1crimea.com:'	
print domain('1crimea.com')


x = raw_input()
