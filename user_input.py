from ingredients import show_ingredients
from ingredients import get_separated_meals
from ingredients import is_meal_exist
from crud_db import  delete_row_db
from crud_db import select_query_db

def add_meal_from_user_input(meals):
    name_meal = input("Podaj nazwę potrawy: ")
    user_ingredients = input("Podaj składniki do podanej potrawy oddzielone spacją i przecinkiem np. mleko, jajka, mąka: ")
    user_ingredients = user_ingredients.split(', ')
    meals[name_meal] = user_ingredients
    
def read_meals_from_db(meals):
    show_ingredients(meals)
    
def update_meal_from_user_input_db(meals_2):
    print(get_separated_meals(meals_2))
    name_meal = input("Podaj nazwę potrawy, którą chcesz zmienić: ")
    if is_meal_exist(meals_2, name_meal):
        name_change_meal = input("Podaj nową nazwę potrawy: ")
        user_ingredients = input("Podaj składniki do zaktuazliowanej potrawy oddzielone spacją i przecinkiem np. mleko, jajka, mąka: ")
        user_ingredients = user_ingredients.split(', ')
        del meals_2[name_meal]
        meals_2[name_change_meal] = user_ingredients
    else:
            print("Nie ma takiej potrawy.")

def delete_meal_from_user_input_db(meals_2):
    print(get_separated_meals(meals_2))
    name_meal_from_user = input("Podaj nazwę potrawy, która ma zostać usunięta: ")
    if is_meal_exist(meals_2, name_meal_from_user):
        del meals_2[name_meal_from_user]
        #todo: show whole table
        meals_from_db = select_query_db('id, name', 'meals')
        for row in meals_from_db:
             id  = row[0]
             if name_meal_from_user == row[1]:
                delete_row_db('meals', id)
    else: 
        print("Nie ma takiej potrawy, podaj inną")
