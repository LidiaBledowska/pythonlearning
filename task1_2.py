
from fun import get_meals_keys
from task1 import show_ingredients
from fun import is_key_exist 




meals_2 = {"spaghetti": ["makaron", "mięso", "sos"], "pomidorówka": ["makaron", "rosół_z_wczoraj"], "jajecznica": ["jajka", "masło"], "żurek": ["żur", "jajka", "kiełbasa"]} 
variable = True 
while variable == True:
    choice = input('Napisz:\n 1 jeśli chcesz wybrać potrawę wraz ze składnikami, \n 2 jeśli chcesz dodać swoją potrawę wraz ze składnikami, \n 3 jeśli program ma zakończyć działanie, \n 4 jeśli chcesz zmienić potrawy w słowniku, \n 5 jeśli chcesz usunąć potrawę ze słownika, \n 6 jeśli chcesz zobaczyć listę potraw po wprowadzonych zmianach \n: ')
    if choice == '1':
        show_ingredients(meals=meals_2)
    elif choice == '2':
        name_meal = input("Podaj nazwę potrawy: ")
        user_ingredients = input("Podaj składniki do podanej potrawy oddzielone spacją i przecinkiem np. mleko, jajka, mąka: ")
        user_ingredients = user_ingredients.split(', ')
        meals_2[name_meal] = user_ingredients
    elif choice == '4':
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
    elif choice == '5':
        print(get_meals_keys(meals_2))
        name_meal = input("Podaj nazwę potrawy, która ma zostać usunięta: ")
        if is_key_exist(meals_2, name_meal):
            del meals_2[name_meal]
        else: 
            print("Nie ma takiej potrawy, podaj inną")
    elif choice == '6':
        print(get_meals_keys(meals_2))
    elif choice == '3':
        variable = False
        print("Koniec programu")
    else:
        print("Nieprawidłowa cyfra. Podaj cyfrę 1 lub 2.")

