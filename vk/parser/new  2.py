#-*- coding:utf-8 -*-
import lxml.html, urllib
page = open(ur'SEO sprint.html').read()
doc = lxml.html.document_fromstring(page)
all_tags = doc.cssselect('span.job-reply')


for garbage in all_tags[0].iterchildren():
 print text
 print garbage.text_content()
 text = text.replace(garbage.text_content(), '')