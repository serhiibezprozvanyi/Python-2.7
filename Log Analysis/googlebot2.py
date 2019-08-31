# -*- coding: utf-8 -*-
#Скрипт чистит все логи в папке и сохраняет id объявления 
import os

#logfile = open(ur'id/log-2018-02-25-nginx.txt', 'a') # Список файлов всех 
#log = list(open(ur'log/log-2018-02-25-nginx.log'))
path = os.getcwd()
googlebot = []  # лог гугл
job_id_googlebot = [] # id урлов
os.chdir(os.getcwd() + '/log')
logdir = os.getcwd()
allfile = os.listdir(logdir) # Список названий всех файлов

# функция проверки числа
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

		
for file in allfile:
	log = list(open(file))
	logfile = open(path + '\\id\\' + file + '.txt', 'a')
	
	for i in log:
		if i.count('Googlebot') == True:
			googlebot.append(i)
		else:
			pass

	for id in googlebot:
		if isint(id.split('/')[4]) == True:
			job_id_googlebot.append(id.split('/')[4])
		else:
			pass
	lenfile = len(job_id_googlebot)  		
	print "-"*35
	print file
	print u'всего id'
	print lenfile
	print u'Уникальных id'
	print  len(set(job_id_googlebot)) 
	
	for i in job_id_googlebot:
		logfile.write(i + '\n')
	logfile.close()
	job_id_googlebot = []
	googlebot = []