# 1. Po wpisaniu nazwy potrawy, chcę widzieć listę składników potrzebnych do przygotowania danego posiłku.
# przykład:
# > Wybierz potrawę (spaghetti, pomidorówka, jajecznica)
# > spaghetti
# > Potrzebujesz: makaron, sos, mięso



# wybor_potrawy = str(input("Podaj nazwę potrawy, a wyświetli się lista potrzebnych składników: "))
# print(wybor_potrawy)
potrawy = {"spaghetti": ["makaron", "mięso", "sos"], "pomidorówka": ["makaron", "rosół_z_wczoraj"]}

potrawa = input("Podaj nazwę potrawy: ")
spaghetti = potrawy[potrawa]
print(spaghetti)



# def moja_funkcja():
#     return 5
 
# wynik = moja_funkcja()
# print(wynik)

# lista = [a, b, c]
# krotka = (a, b ,c)
# słownik = {a: a1, b: b2, c: c3}
