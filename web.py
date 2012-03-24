# -*- coding:utf-8 -*-
import pycurl
import StringIO
import urllib

def curl(url, **kwargs):
	'''pycurl的简化使用函数'''
	s = StringIO.StringIO()
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, url)
	curl.setopt(pycurl.WRITEFUNCTION, s.write)
	curl.setopt(pycurl.NOSIGNAL, True) #防止多线程运行时可能抛出的错误

	if 'FOLLOWLOCATION' not in kwargs: #是否随着HTTP头指定的Location进行跳转
		curl.setopt(pycurl.FOLLOWLOCATION, True)
	else:
		curl.setopt(pycurl.FOLLOWLOCATION, kwargs['FOLLOWLOCATION'])
	if 'REFERER' not in kwargs:
		curl.setopt(pycurl.REFERER, url)
	else:
		curl.setopt(pycurl.REFERER, kwargs['REFERER'])
	
	curl.perform()
	curl.close()
	return s.getvalue()

def urlencode(url):
	return urllib.quote_plus(url)
