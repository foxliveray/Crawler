import urllib.request
import re
URL = 'https://plants.usda.gov/java/factSheet'
req = urllib.request.Request(URL)
html = urllib.request.urlopen(req)
doc = html.read().decode('utf8')

res = r'<tr class="rowon">(.*?)</tr>'
n = re.findall(res,doc,re.S|re.M)
res2 = r'<td(.*?)</td>'
for line in n:
    m = re.findall(res2,line,re.S|re.M)
    for i in m:
        if m.index(i) % 4 == 0:
            dr = re.compile(r'<[^>]+>', re.S)
            i = dr.sub('', i)
            i = i.lstrip(' class="resultsind1">')
            i.lstrip('>')

        elif m.index(i) % 4 == 1:
            i = i.lstrip('>')

        elif m.index(i) % 4 == 2:
            if i == '>&nbsp;':
                i = 'None'
            else:
                res3 = r'(?<=href=\").+?(?=\")'
                i = re.findall(res3, i, re.I | re.S | re.M)
                i = i[1]

        elif m.index(i) % 4 == 3:
            if i == '>&nbsp;':
                i = 'NULL'
            else:
                res3 = r'(?<=href=\").+?(?=\")'
                i = re.findall(res3, i, re.I | re.S | re.M)
                i = i[1]

        print("td:", i)

'''
    res2 = r'<th align="left" valign="top" class="colnorm" scope="row">(.*?)</th>'
    m = re.findall(res2, line, re.S | re.M)
    for i in m:
        print('symbol:', i)
'''
