import urllib.request
import re

url = "https://plants.usda.gov/java/charProfile?symbol=ABAM"
req = urllib.request.Request(url)
html = urllib.request.urlopen(req)
doc = html.read().decode('utf8')

res = r'<table cellpadding="3">(.*?)</table>'
m = re.findall(res,doc,re.S|re.M)
for line in m:
    res2 = r'<td valign="top" align="left">(.*?)</td>'
    n = re.findall(res2,line,re.S|re.M)

n.pop(4)
n.pop(3)
n.pop(2)
n.pop(1)
n.pop(0)
for i in n:
    print(i)