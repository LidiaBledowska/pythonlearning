from fun import get_meals_keys
from fun import is_key_exist
from fun import get_result

def show_ingredients(meals={}):
    list_meals = get_meals_keys(meals)
    meal = input('Podaj nazwę potrawy spośród ' + list_meals + ': ')
    exist = is_key_exist(meals, meal)
    result = get_result(meals, meal, exist)
    print(result)

