def get_meals_keys (meals):
    list_meals = []
    for key in meals:
        list_meals.append(key)
    return ', '.join(list_meals) 




def is_key_exist (meals, meal):
    exist = False
    for key in meals:
        if key == meal:
            exist = True 
    return exist

def get_result (meals, meal, exist):
    if exist == True:
        ingredients = str(meals[meal])
        return ingredients
    else:
        return "i don't know"