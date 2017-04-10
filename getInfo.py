import urllib.request
import re
URL = 'https://plants.usda.gov/java/factSheet'
req = urllib.request.Request(URL)
html = urllib.request.urlopen(req)
doc = html.read().decode('utf8')

res = r'<tr class="rowon">(.*?)</tr>'
n = re.findall(res,doc,re.S|re.M)
res2 = r'<td>(.*?)</td>'
for line in n:
    m = re.findall(res2,line,re.S|re.M)
    for i in m:
        if m.index(i)%4 ==0:
            i = re.compile(r'<[^>]+>',re.S|re.M)
            i = i.sub('',i)
        elif m.index(i)%4==2 or m.index(i)%4==3:

        print('td标签内容:',i)
'''
    res2 = r'<th align="left" valign="top" class="colnorm" scope="row">(.*?)</th>'
    m = re.findall(res2, line, re.S | re.M)
    for i in m:
        print('symbol:', i)
'''
