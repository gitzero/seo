# -*- coding:utf-8 -*-
import re
def string_intersection(str_1, str_2):
	'''字符串最长交集'''
	for length in range(len(str_1),1,-1):
		for start in range(len(str_1)):
			if str_1[start:start+length] in str_2:
				return str_1[start:start+length]
	return False
def string_clear(string):
	'''去除标点符号'''
	return ''.join(re.findall(u'[\u4e00-\u9fa5]+', string))
