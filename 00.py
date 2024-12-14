from fun import get_meals_keys
from fun import is_key_exist
from fun import get_result

meals = {"spaghetti": ["makaron", "mięso", "sos"], "pomidorówka": ["makaron", "rosół_z_wczoraj"], "jajecznica": ["jajka", "masło"], "żurek": ["żur", "jajka", "kiełbasa"]} 
list_meals = get_meals_keys(meals)
list_meals = ', '.join(list_meals)
meal = input('Podaj nazwę potrawy spośród ' + list_meals + ': ')
exist = is_key_exist(meals, meal)
result = get_result(meals, meal, exist)
print(result)
