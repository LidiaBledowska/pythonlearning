
from fun import get_meals_keys
from task1 import show_ingredients



meals_2 = {"spaghetti": ["makaron", "mięso", "sos"], "pomidorówka": ["makaron", "rosół_z_wczoraj"], "jajecznica": ["jajka", "masło"], "żurek": ["żur", "jajka", "kiełbasa"]} 
variable = True 
while variable == True:
    choice = input('Napisz 1 jeśli chcesz wybrać potrawę wraz ze składnikami, 2 jeśli chcesz dodać swoją potrawę wraz ze składnikami lub 3 jeśli program ma zakończyć działanie. ')
    if choice == '1':
        show_ingredients(meals=meals_2)
    elif choice == '2':
        name_meal = input("Podaj nazwę potrawy: ")
        user_ingredients = input("Podaj składniki do podanej potrawy oddzielone spacją i przecinkiem np. mleko, jajka, mąka: ")
        user_ingredients = user_ingredients.split(', ')
        meals_2[name_meal] = user_ingredients
    elif choice == '3':
        variable = False
        print("Koniec programu")
    else:
        print("Nieprawidłowa cyfra. Podaj cyfrę 1 lub 2.")

