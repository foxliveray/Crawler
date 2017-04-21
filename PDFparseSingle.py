from bs4 import BeautifulSoup
import re
import select_data
import insert_data

plant_guide = select_data.query_pdflink()

soup = BeautifulSoup(open("E:\pdf\p\cs_astr.html",encoding= 'utf-8'),"html.parser")
plant = 'ASTR'
print(plant)
#print(soup.prettify())

result = soup.find_all("span" )

sty =''
value = []
for i in result:
        if i.get_text().strip().lower()=="uses":
            sty = i['style']
        elif i.get_text().strip().lower()=="use":
            sty = i['style']
        elif i.get_text().strip().lower()=="status":
            sty = i['style']

        i = i.get_text().replace('\n','').replace('\r','')
        #i = i[:-1]
        value.append(i)

#print(value)

field0 = []
result2 = soup.find_all(style = sty)
for i in result2:
    i = i.get_text()
    if i!='\n':
        i = i.replace('\n','')
        if i != '' and i!=' ' and i != 'USDA IS AN EQUAL OPPORTUNITY PROVIDER AND EMPLOYER ' and i != 'Page: 1, 2, 3' and len(i)<100:
            field0.append(i)

print(field0)
string = ''
list = {}
for i in field0:
    if i =='':
        continue
    elif i!=field0[-1]:
        ind0=value.index(i)+1
        ind1=value.index(field0[field0.index(i)+1])
        if ind1==ind0:
            string = string + value[ind0]
            list[i] = string
        else:
            for j in range(ind0,ind1):
                string = string + value[j]
            list[i] = string

        string =''
    else:
        ind0 = value.index(i) + 1
        ind1 =value.index(value[-1])
        if ind1 == ind0:
            string = string + value[ind0]
            list[i] = string
        else:
            for j in range(ind0, ind1):
                string = string + value[j]
            list[i] = string

        string = ''

print(list)
prefix ="pg_"
value = ''
for i in list:
    value = list[i].replace("'", "_")
    if i[-1]==' ':
        i = i[:-1]
    i = i.replace(" ","_").replace(":","_").replace("/","_").replace("(","_").replace(")","_").replace(",","_").replace("°","_").replace("&","_").replace("__","_").replace('.','_').replace("-","_").replace("[","_").replace("]","_").lower()
    i =prefix + i
    if i[-1]=='_':
        i = i[:-1]
    if len(i)>=64:
        i = i[:40]
    insert_data.alter_pdf_pg_field(i)
    insert_data.insert_pdf_pg_data(i,value,plant)
    value = ''



