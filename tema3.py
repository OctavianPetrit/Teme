# '''Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.'''
#
# x = int(input("Valoarea lui x este: "))
#
# '''1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
# else.'''
#
# # if else - if este inceputul unei decizii care se executa atunci cand conditia este adevarata,
# # iar else se executa cand conditia este falsa
#
# '''2. Verifică și afișează dacă x este număr natural sau nu.'''
# if x > 0 and isinstance(x,int):
#     print("x este numar natural")
# else:
#     print("x nu este numar natural")
#
# """3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru."""
#
# if x < 0:
#     print("x este numar negativ")
# elif x == 0:
#     print("x este numar neutru")
# else:
#     print("x este numar pozitiv")
#
# """4. Verifică și afișează dacă x este între -2 și 13."""
#
# if x >= -2 and x <= 13:
#     print("x este un numar cuprins in inervalul -2 si 13")
# else:
#     print("x este nu un numar cuprins in inervalul -2 si 13")
#
# "5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5."
#
# y = int(input("Valoarea lui y este: "))
#
# if x - y < 5:
#     print("Diferenta dintre x și y este mai mica decat 5")
# else:
#     print("Diferenta dintre x și y este mai mare decat 5")
#
# "6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’."
#
# print(not(x >= 5 and x <= 27))
#
# """7.
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare."""
#
# if x == y:
#     print("x si y sunt egale")
# elif x > y:
#     print("x este mai mare decat y")
# else:
#     print("y este mai mare decat x")
#
# """8.
# x, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare."""
#
# z = int(input("Valoarea lui z este: "))
#
# if ((x == y != z) or (x != y == z) or (x == z != y)):
#     print("Triunghiul este isoscel")
#
# elif (x == y == z):
#     print("Triunghiul este echilateral")
# else:
#     print("Triunghiul este oarecare")

"""9. Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu"""

# litera = input("Litera este: ")
#
# if (litera == 'a' or litera == 'A') or (litera == 'e' or  litera == 'E') or (litera == 'i' or litera == 'I' ) or (litera == 'o' or litera == 'O') or (litera == 'u' or litera == 'U'):
#     print('Litera introdusa este vocala')
# else :
#     print('Litera introdusa este o consoana')

"""10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F"""
#
# nota = float(input("Nota este: "))
# if (nota >= 9) and (nota <= 10):
#     print("Calificativul este: A")
# if((nota >= 8) and (nota < 9)):
#     print("Calificativul este: B")
# if((nota >= 7) and (nota < 8)):
#     print("Calificativul este: C")
# if((nota >= 6) and (nota < 7)):
#     print("Calificativul este: D")
# if ((nota > 4) and (nota < 6)):
#     print("Calificativul este: E")
# elif (nota <= 4):
#     print("Calificativul este: F")

"""Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.

1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)"""

# numar_minim = 4
# if x >= (len(str(x) >= str(4)):
#     print("x are minim 4 cifre")
# else:
#     print("x are mai putin de 4 cifre")
#
# number_x = 123
# count = 0
# if (number_x == 0):
#     count = count + 1
# else:
#     while (number_x):
#         count = count + 1
#         number_x = number_x // 10
# if (count >= 4):
#     print(f'Numarul are minim 4 cifre')
# else:
#     print(f'Numarul nu are minim 4 cifre')
# '''
# 2.Verifică dacă x are exact 6 cifre.
# '''
# if (count == 6):
#     print(f'Numarul are {count} cifre')
# '''
# 3.Verifică dacă x este număr par sau impar (x e int).
# '''
# number_x2 = 5
# if (number_x2 % 2 == 0):
#     print(f'Numarul {number_x2} este par')
# else:
#     print(f'Numarul {number_x2} este impar')
#  '''4.
#   x, y, z (int)
#  Afișează care este cel mai mare dintre ele?'''

# x1 = 3
# y1 = 5
# z1 = 5
# if (x1 > y1 and x1 > z1):
#     print(f'{x1} este cel mai mare numar')
# elif (y1 > x1 and y1 > z1):
#     print(F'{y1} este cel mai mare numar')
# elif (z1 > x1 and z1 > y1):
#     print(f'{z1} este cel mai mare numar')
# else:
#     print("Cel putin 2 numere sunt egale")

'''5.
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.'''

# x = 177
# y = 1
# z = 0
# if (x > 0 and x < 180) and (y > 0 and y < 180) and (z > 0 and z < 180) and (x + y + z == 180):
#     print('Este un triunghi valid')
# else:
#     print('Nu este un triunghi valid')

"""2. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random.
Ne imaginam că dăm cu zarul și salvăm acest număr în dice_roll.
Ia un număr ghicit de la utilizator.
Verifică și afișază dacă utilizatorul a ghicit 3 opțiuni:
- Ai pierdut. Ai ales un număr mai mic. Ai ales x dar a fost y.
- Ai pierdut. Ai ales un număr mai mare. Ai ales x dar a fost y.
- Ai ghicit. Felicitări? Ai ales x și zarul a fost y."""
# import random
# a = []
# n = int(input("Enter number of elements: "))
# for i in range(n):
#     dice_roll = a.append(random.randint(0, 20))
#     while(input('Alege numar: ')):
#         print(f'Ai pierdut. Ai ales un număr mai mic. Ai ales {input()} dar a fost {a}')
#         break
