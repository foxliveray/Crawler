import urllib.request
import re
from mysql.connector import MySQLConnection,Error
from dbconfig import read_db_config
import select_data
import insert_data

result = select_data.query_symbol()
fieldList = select_data.query_field()
L =[]

for i in result:
    url = "https://plants.usda.gov/java/charProfile?symbol=%s"%i
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    doc = html.read().decode('utf8')

    res = r'<table cellpadding="3">(.*?)</table>'
    m = re.findall(res,doc,re.S|re.M)
    for line in m:
        res2 = r'<td valign="top" align="left">(.*?)</td>'
        n = re.findall(res2,line,re.S|re.M)
    if 'n' in locals().keys():
        print(i,len(n))
        n.pop(4)
        n.pop(3)
        n.pop(2)
        n.pop(1)
        n.pop(0)

        key = ''
        for line in n:
            if n.index(line)%2==0:
                line=line.replace(" ","_").replace(":","_").replace("/","_").replace("(","_").replace(")","_").replace(",","_").replace("°","_")
                insert_data.alter_character(line)
                '''
                if line in fieldList:
                    print(line, "is in the list.")
                    key = line
                    continue
                else:
                    insert_data.alter_character(line)
                    key = line
                '''
                key = line

            elif n.index(line) % 2 == 1:
                insert_data.insert_chatacter(key, line, i)

        del n
    else:
        print("n is not defined.")
        continue



