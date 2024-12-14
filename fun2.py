from task1 import show_ingredients
from fun import get_meals_keys
from fun import is_key_exist

def create_meal(meals):
    name_meal = input("Podaj nazwę potrawy: ")
    user_ingredients = input("Podaj składniki do podanej potrawy oddzielone spacją i przecinkiem np. mleko, jajka, mąka: ")
    user_ingredients = user_ingredients.split(', ')
    meals[name_meal] = user_ingredients
    
def read_fun(meals):
    show_ingredients(meals)
    
def update_meal(meals_2):
    print(get_meals_keys(meals_2))
    name_meal = input("Podaj nazwę potrawy, którą chcesz zmienić: ")
    if is_key_exist(meals_2, name_meal):
        name_change_meal = input("Podaj nową nazwę potrawy: ")
        user_ingredients = input("Podaj składniki do zaktuazliowanej potrawy oddzielone spacją i przecinkiem np. mleko, jajka, mąka: ")
        user_ingredients = user_ingredients.split(', ')
        del meals_2[name_meal]
        meals_2[name_change_meal] = user_ingredients
    else:
            print("Nie ma takiej potrawy.")

def delete_meal(meals_2):
    print(get_meals_keys(meals_2))
    name_meal = input("Podaj nazwę potrawy, która ma zostać usunięta: ")
    if is_key_exist(meals_2, name_meal):
        del meals_2[name_meal]
    else: 
        print("Nie ma takiej potrawy, podaj inną")