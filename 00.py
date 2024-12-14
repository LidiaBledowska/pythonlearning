# 1. Po wpisaniu nazwy potrawy, chcę widzieć listę składników potrzebnych do przygotowania danego posiłku.
# przykład:
# > Wybierz potrawę (spaghetti, pomidorówka, jajecznica)
# > spaghetti
# > Potrzebujesz: makaron, sos, mięso



# wybor_potrawy = str(input("Podaj nazwę potrawy, a wyświetli się lista potrzebnych składników: "))
# print(wybor_potrawy)

from fun import get_meals_keys
from fun import is_key_exist


meals = {"spaghetti": ["makaron", "mięso", "sos"], "pomidorówka": ["makaron", "rosół_z_wczoraj"], "jajecznica": ["jajka", "masło"], "żurek": ["żur", "jajka", "kiełbasa"]} 

lista_potraw = get_meals_keys(meals)
lista_potraw = ', '.join(lista_potraw)

meal = input('Podaj nazwę potrawy spośród ' + lista_potraw + ': ')


exist = is_key_exist(meals, meal)
if exist == True:
    ingredients = meals[meal]
    print(ingredients)
else:
    print("i don't know")


#1. przygotuj funkcje która zwróci liczbe kluczy w slowniku + musi przyjmowac jako argument def moja_funkcja(slownik) i ma zwrocic liste kluczy
#2. napisz funkcje ktora sprawdza czy klucz istnieje
#3. napisz funkcje ktora wypisuje skladniki potrawy jesli istnieje ale jesli nie to pisze ze nie istnieje
#4. uzyj tych funkcji aby progra zachowywal sie tak samo jak do tej pory 



# def moja_funkcja():
#     return 5
 
# wynik = moja_funkcja()
# print(wynik)

# lista = [a, b, c]
# krotka = (a, b ,c)
# słownik = {a: a1, b: b2, c: c3}
