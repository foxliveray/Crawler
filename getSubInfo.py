import urllib.request
import re
from mysql.connector import MySQLConnection,Error
from dbconfig import read_db_config
import select_data
import insert_data

result = select_data.query_symbol()
for i in result:
    url = "https://plants.usda.gov/core/profile?symbol=%s"%i
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req)
    doc = html.read().decode('utf8')

    res = r'<table class="bordered" border="0" cellspacing="0" cellpadding="0">(.*?)</table>'
    m = re.findall(res,doc,re.S|re.M)
    L = []

    for line in m:
        res2 = r'<td valign="top">(.*?)</td>'
        n = re.findall(res2,line,re.S|re.M)
        for i in n:
            if n.index(i)%2==1:
                dr = re.compile(r'<[^>]+>', re.S)
                i = dr.sub('', i)
                b = i.replace('\r', '').replace('\n', '').replace('\t', '').replace('&nbsp;','')
                L.append(b)
    if(len(L)!=0):
        print(L[0])
        insert_data.insert_profile(L[0],L[1],L[2],L[3],L[4],L[5])



