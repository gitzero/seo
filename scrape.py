import web
import re

def baidu_serp(keyword):
	serp = web.curl('http://www.baidu.com/s?wd=%s&rn=100' % (web.urlencode(keyword)))
	return re.findall('<h3 class="t".*?href="(.*?)"', serp)
