# -*- coding: utf-8 -*-
import lxml.html, urllib
page = open(ur'SEO sprint_24.11.html').read()
doc = lxml.html.document_fromstring(page)
all_tags = doc.cssselect('span.job-reply')
re = []
for text in all_tags:
	print text.text_content()
	#re = text.replace(text.text_content(), '')
"""for garbage in all_tags[0].iterchildren():
 print text
 print garbage
 text = text.replace(garbage.text_content(), '')
"""