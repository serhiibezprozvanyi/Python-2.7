#-*- coding:utf-8 -*-
import os
def clears(path, files):
	file = [i[:-1] if i[-1] == '\n' else i for i in open(files)]
	filedisk = os.listdir(path)
	d = []
	s = -1
	l_file = len(file)
	for i in file:
		s += 1
		if i != filedisk[s]:
			d.append(i)
		else:
			pass
	rr =  list(set(filedisk) - set(d))
	for i in rr:
		os.remove(path + i)
		print u'Файл удален: ', i
clears(path = raw_input(u'Введите полный путь к папке в фото пример:(e:\images\)'.encode("cp866")), files = raw_input(u'Введите название файла Пример(file.txt)'.encode("cp866")))
print u'Все лишние файлы удалены...'