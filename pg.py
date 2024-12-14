import psycopg

def select_query(what_column, table):
    try:
        connection = psycopg.connect(
            dbname='meals_and_ingredients',
            user='postgres',
            password=1234,
            host='localhost',
            port=5432
        )
        cursor = connection.cursor()
        cursor.execute('select ' + what_column + ' from ' + table + ';')
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
    
def get_meals_from_db():
    list_meals = select_query('name, ingredients', 'meals')
    dict_meals = {}
    for meal in list_meals:
        key = meal[0]
        value = meal[1].split(', ')
        dict_meals[key] = value
    return dict_meals


