from bs4 import BeautifulSoup
import re
import select_data
import insert_data

plant_guide = select_data.query_pdflink()

soup = BeautifulSoup(open("E:\pdf\p\pg_abco.html",encoding= 'utf-8'),"html.parser")
plant = 'ABCO'
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
field = []
result2 = soup.find_all(style = sty)
for i in result2:
    i = i.get_text()
    if i!='\n':
        i = i.replace('\n','')
        field0.append(i)
        '''
        i = i[:-1]
        i = i.replace(" ","_").replace(":","_").replace("/","_").replace("(","_").replace(")","_").replace(",","_").replace("°","_")
        field.append(i)
        '''

print(field0)
string = ''
list = []
for i in field0:
    if i!=field0[-1]:
        ind0=value.index(i)+1
        ind1=value.index(field0[field0.index(i)+1])
        if ind1==ind0:
            string = string + value[ind0]
            list.append(i)
            list.append(string)
        else:
            for j in range(ind0,ind1):
                string = string + value[j]
            list.append(i)
            list.append(string)

        string =''
    else:
        ind0 = value.index(i) + 1
        ind1 =value.index(value[-1])
        if ind1 == ind0:
            string = string + value[ind0]
            list.append(i)
            list.append(string)
        else:
            for j in range(ind0, ind1):
                string = string + value[j]
            list.append(i)
            list.append(string)

        string = ''

data =[]
prefix ="pg_"
field =''
for i in list:
    if list.index(i)%2==0:
        i = i[:-1]
        i = i.replace(" ","_").replace(":","_").replace("/","_").replace("(","_").replace(")","_").replace(",","_").replace("°","_").replace("&","_").replace("__","_")
        i =prefix + i
        if i[-1]=='_':
            i = i[:-1]
        if len(i)>=64:
            i = i[:-20]
        #insert_data.alter_pdf_pg_field(i)
        field = i
        data.append(i)

    elif list.index(i)%2==1:
        i = i.replace("'","_")
        #insert_data.insert_pdf_pg_data(field,i,plant)
        data.append(i)

print(data)

