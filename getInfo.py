import urllib.request
import re
from mysql.connector import  MySQLConnection,Error
from dbconfig import read_db_config
import insert_data

URL = 'https://plants.usda.gov/java/factSheet'
req = urllib.request.Request(URL)
html = urllib.request.urlopen(req)
doc = html.read().decode('utf8')

a = 4
res = r'<tr class="rowon">(.*?)</tr>'
n = re.findall(res,doc,re.S|re.M)
for line in n:

    symbol = r'<th (.*?)</th>'
    s = re.findall(symbol, line, re.S | re.M)
    for i in s:
        i = i.lstrip('align="left" valign="top" class="colnorm" scope="row">').lstrip('align="left" class="resultsind1" scope="row">')
        insert_data.insert_symbol(i,a)
        a = a+1
        print("symbol:",i)


    res2 = r'<td(.*?)</td>'
    m = re.findall(res2,line,re.S|re.M)
    for i in m:
        if m.index(i) % 4 == 0:
            dr = re.compile(r'<[^>]+>', re.S)
            i = dr.sub('', i)
            i = i.lstrip(' class="resultsind1">')
            i.lstrip('>')
            insert_data.insert_scientific(i,int(a / 4))
            print(int(a / 4))

        elif m.index(i) % 4 == 1:
            i = i.lstrip('>')
            insert_data.insert_common(i,int((a - 1) / 4))
            print(int((a - 1) / 4))

        elif m.index(i) % 4 == 2:
            if i == '>&nbsp;':
                i = 'None'
            else:
                res3 = r'(?<=href=\").+?(?=\")'
                i = re.findall(res3, i, re.I | re.S | re.M)
                i = i[1]
            insert_data.insert_factsheet(i,int((a - 2)/4))
            print(int((a - 2)/4))

        elif m.index(i) % 4 == 3:
            if i == '>&nbsp;':
                i = 'NULL'
            else:
                res3 = r'(?<=href=\").+?(?=\")'
                i = re.findall(res3, i, re.I | re.S | re.M)
                i = i[1]
            insert_data.insert_guide(i,int((a - 3) / 4))
            print(int((a - 3) / 4))

        print("td:", i)
        a = a + 1





