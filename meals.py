def get_separated_meals (meals):
    list_meals = []
    for key in meals:
        list_meals.append(key)
    return ', '.join(list_meals) 

def is_meal_exist (meals, meal):
    exist = False
    for key in meals:
        if key == meal:
            exist = True 
    return exist