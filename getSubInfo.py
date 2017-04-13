import urllib.request
import re

url = "https://plants.usda.gov/core/profile?symbol=ABAM"
req = urllib.request.Request(url)
html = urllib.request.urlopen(req)
doc = html.read().decode('utf8')

res = r'<table class="bordered" border="0" cellspacing="0" cellpadding="0">(.*?)</table>'
m = re.findall(res,doc,re.S|re.M)
for line in m:
    res2 = r'<td valign="top">(.*?)</td>'
    n = re.findall(res2,line,re.S|re.M)
    for i in n:
        if n.index(i)%2==1:
            dr = re.compile(r'<[^>]+>', re.S)
            i = dr.sub('', i)
            b = i.replace('\r', '').replace('\n', '').replace('\t', '').replace('&nbsp;','')
            print("tag:",b)

