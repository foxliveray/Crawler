from mysql.connector import  MySQLConnection,Error
from dbconfig import read_db_config
import select_data

def insert_symbol(sy,_id):
    query = " insert into plant_usda(symbol,id) values(%s,%s)"
    args = (sy,_id)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query,args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
            conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_scientific(sc,_id):
    query = 'update plant_usda set scientific_name = %s WHERE id = %s'
    args = (sc, _id)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
            conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_common(co,_id):
    query = 'update plant_usda set common_name = %s WHERE id = %s'
    args = (co, _id)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
            conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_factsheet(fa,_id):
    query = 'update plant_usda set fact_sheet = %s WHERE id = %s'
    args = (fa, _id)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
            conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_guide(gu,_id):
    query = 'update plant_usda set plant_guide = %s WHERE id = %s'
    args = (gu, _id)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
            conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_profile(sy,gr,fa,du,ha,na):
    query = 'update plant_usda set _group = %s, family=%s, duration=%s, growth_habit=%s, native_status=%s WHERE symbol = %s'
    args = (gr,fa,du,ha,na,sy)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
            conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def alter_character(field):
    result = select_data.query_field()
    if field in result:
        print(field, "is in the list.")

    else:
        query = "alter table `plant_usda` add column %s VARCHAR(20) NULL"%field
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query)

        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()

def insert_chatacter(field,value,sy):
    query = 'update plant_usda set %s = \'%s\' WHERE symbol = \'%s\' '%(field,value,sy)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
            conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def alter_pdf_field(field):
    result = select_data.query_field()
    if field in result:
        print(field, "is in the list.")

    else:
        query = "alter table `plant_usda` add column %s TEXT NULL"%field
        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query)

        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()

def insert_pdf_data(field,value,sy):
    query = 'update plant_usda set %s = \'%s\' WHERE symbol = \'%s\''%(field,value,sy)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
            conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def test():
    string = "dfjhdlkfsldkjasldusoidasdjo"
    string = string[:-10]
    print(string)

if __name__ == '__main__':
    alter_pdf_pg_field("pg_uses")
    insert_pdf_pg_data("pg_uses", "3324fg", "ABAM")