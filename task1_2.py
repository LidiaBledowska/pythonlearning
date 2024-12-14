from fun import *
from task1 import show_ingredients 
from fun2 import *

meals_2 = {"spaghetti": ["makaron", "mięso", "sos"], "pomidorówka": ["makaron", "rosół_z_wczoraj"], "jajecznica": ["jajka", "masło"], "żurek": ["żur", "jajka", "kiełbasa"]} 
variable = True 
while variable == True:
    choice = input('Napisz:\n 1 jeśli chcesz wybrać potrawę wraz ze składnikami, \n 2 jeśli chcesz dodać swoją potrawę wraz ze składnikami, \n 3 jeśli program ma zakończyć działanie, \n 4 jeśli chcesz zmienić potrawy w słowniku, \n 5 jeśli chcesz usunąć potrawę ze słownika, \n 6 jeśli chcesz zobaczyć listę potraw po wprowadzonych zmianach \n: ')
    if choice == '1':
        show_ingredients(meals_2)
    elif choice == '2':
        create_meal(meals_2)
    elif choice == '4':
        update_meal(meals_2)
    elif choice == '5':
        delete_meal(meals_2)
    elif choice == '6':
        print(get_meals_keys(meals_2))
    elif choice == '3':
        variable = False
        print("Koniec programu")
    else:
        print("Nieprawidłowa cyfra. Podaj cyfrę 1 lub 2.")

