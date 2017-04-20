from mysql.connector import MySQLConnection,Error
from dbconfig import read_db_config

def query_symbol():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT symbol from plant_usda")
        rows = cursor.fetchall()

        #print('Total Row(s):',cursor.rowcount)
        #for row in rows:
            #print(row)
        L = []
        for i in rows:
            L.append(i[0])

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

    return L

def query_field():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("DESC plant_usda")
        rows = cursor.fetchall()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

    L = []
    for i in rows:
        L.append(i[0])

    return L

def query_pdflink():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT plant_guide from plant_usda")
        rows = cursor.fetchall()

        L = []
        for i in rows:
            L.append(i[0])

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

    return L

def query_pdflink2():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT fact_sheet from plant_usda")
        rows = cursor.fetchall()

        L = []
        for i in rows:
            L.append(i[0])

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

    return L


if __name__ == '__main__':
    result = query_pdflink2()
    for i in result:
        print(i)