import psycopg

def select_query_db(what_columns, table):
    try:
        connection = psycopg.connect(
            dbname='meals_and_ingredients',
            user='postgres',
            password=1234,
            host='localhost',
            port=5432)
        cursor = connection.cursor()
        cursor.execute('select ' + what_columns + ' from ' + table + ';')
        records = cursor.fetchall()
        print(records)
        print("Połączenie udane!")
        return records
    except:
        print("It doesn't work")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Połączenie zamknięte.")

def delete_row_db(table, id):
    try:
        connection = psycopg.connect(
        dbname='meals_and_ingredients',
        user='postgres',
        password='1234',
        host='localhost',
        port=5432)
        cursor = connection.cursor()
        query = 'delete from ' + table + ' where id = ' + str(id) + ';'
        cursor.execute(query)
        connection.commit()  
        print("Wiersz został usunięty pomyślnie!")
    except: 
        print("Wystąpił błąd podczas usuwania wiersza: error")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Połączenie zostało zamknięte.")

def get_ingredients_from_db():
    list_meals = select_query_db('name, ingredients', 'meals')
    dict_meals = {}
    for meal in list_meals:
        key = meal[0]
        value = meal[1].split(', ')
        dict_meals[key] = value
    return dict_meals


def delete_meals_from_db():
    list_meals = select_query_db