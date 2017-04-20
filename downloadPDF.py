import  urllib.request
import re
import select_data

result = select_data.query_pdflink()
result2 = select_data.query_pdflink2()
flag = False


for i in result:
    #if i=='/plantguide/pdf/pg_crin4.pdf':
    #if i == '/plantguide/pdf/pg_ecsa.pdf':
    #if i == '/plantguide/pdf/pg_hyov.pdf':
    if i == '/plantguide/pdf/pg_pran3.pdf':
        flag = True
        continue

    if flag == False:
        continue
    elif flag == True:
        if i!='NULL':
            url = "https://plants.usda.gov%s"%i
            print(url)
            i = i.replace('/plantguide/pdf/','')
            print(i)
            local = "E://allpdf/%s"%i
            urllib.request.urlretrieve(url,local)


for line in result2:
    if line!='None':
        url = 'https://plants.usda.gov%s'%line
        print(url)
        line = line.replace('/factsheet/pdf/','')
        print(line)
        local = "E://allpdf/fact_sheet/%s"%line
        urllib.request.urlretrieve(url,local)