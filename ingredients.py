from meals import get_separated_meals, is_meal_exist

def get_ingredients_or_idk (meals, meal, exist):
    if exist == True:
        ingredients = str(meals[meal])
        return ingredients
    else:
        return "i don't know"
    
def show_ingredients(meals={}):
    list_meals = get_separated_meals(meals)
    meal = input('Podaj nazwę potrawy spośród ' + list_meals + ': ')
    exist = is_meal_exist(meals, meal)
    result = get_ingredients_or_idk(meals, meal, exist)
    print(result)