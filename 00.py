# 1. Po wpisaniu nazwy potrawy, chcę widzieć listę składników potrzebnych do przygotowania danego posiłku.
# przykład:
# > Wybierz potrawę (spaghetti, pomidorówka, jajecznica)
# > spaghetti
# > Potrzebujesz: makaron, sos, mięso



# wybor_potrawy = str(input("Podaj nazwę potrawy, a wyświetli się lista potrzebnych składników: "))
# print(wybor_potrawy)
potrawy = {"spaghetti": ["makaron", "mięso", "sos"], "pomidorówka": ["makaron", "rosół_z_wczoraj"], "jajecznica": ["jajka", "masło"], "żurek": ["żur", "jajka", "kiełbasa"]} 
lista_potraw = []  
for klucz in potrawy:
    lista_potraw.append(klucz)
lista_potraw = ', '.join(lista_potraw)
print(lista_potraw)
potrawa = input('Podaj nazwę potrawy spośród ' + lista_potraw + ': ')
istnieje = False
for klucz in potrawy:
    if klucz == potrawa:
        istnieje = True 


if istnieje == True:
    skladniki = potrawy[potrawa]
    print(skladniki)
else:
    print("nie znam takiej potrawy")





# def moja_funkcja():
#     return 5
 
# wynik = moja_funkcja()
# print(wynik)

# lista = [a, b, c]
# krotka = (a, b ,c)
# słownik = {a: a1, b: b2, c: c3}
