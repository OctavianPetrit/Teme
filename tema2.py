# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# variabilele sunt niste date / valori tinute in zona de memorie

''''2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.'''
# string
# import math
#
# marca = 'Mazda'
# print(marca)
# # int
# an_fabricatie = 2009
# print(an_fabricatie)
# # float
# consum = 5.8
# print(consum)
# # boolean
# status_inmatriculare = True
# print(status_inmatriculare)
#
'''3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.'''
# print(type(marca))
# print(type(an_fabricatie))
# print(type(consum))
# print(type(status_inmatriculare))

'''4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.'''
# consum = round(consum)
# print('Are consumul de: ' + str(consum) + ' %')
#
'''5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile'''
# print('Marca masina: ' + marca)
# print('Anul de fabricatie: ' + str(an_fabricatie))
# print('Are consumul de: ' + str(consum) + ' %')
# print(f'Masina este inmatriculata? ' + str(status_inmatriculare))

'''Rezolvă nepotrivirile de tip prin ce modalitate dorești.

6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.'''
# nume = input('Va rugam sa va introduceti numele: ')
# print(nume)
# prenume = input('Va rugam sa va introduceti prenumele: ')
# print(prenume)
# print('Numele complet are ' + str(len(nume)) + ' caractere')

'''7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.'''
# lungime = int(input('Lungimea dreptunghiului este: '))
# print(lungime)
# latime = int(input('Latimea dreptunghiului este: '))
# print(latime)
# aria = lungime * latime
# print(f'Aria triunghiului este:  {aria}')

'''8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- citește de la tastatură un int x;
- afișează stringul fără ultimele x caractere.
ex: Dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'.'''

# fraza = 'Coral is either the stupidest animal or the smartest rock'
# print(f'Fraza data este: {fraza}')
# numar_caractere_taiate = int(input('Numar de caractere taiate: ' ))
# print(f'Taiem ultimele {numar_caractere_taiate} caractere din fraza de mai sus')
# print(fraza[0 : len(fraza) - (numar_caractere_taiate + 1)])

'''9. Același string:
a. declară un string nou care să fie format din primele 5 caractere + ultimele
5;
b. afișează de câte ori apare cuvântul 'the';
c. înlocuiește ‘the’ cu ‘THE’ peste tot - printează rezultatul;
d. salvează într-o variabilă și afișează indexul de start al cuvântului ‘rock’;
- hint: este o funcție care te ajută să faci asta;
folosind această variabilă + slicing, afișează tot stringul până la acest
cuvânt.
Output: 'Coral is either the stupidest animal or the smartest'''''
# string_nou = fraza[0:6] + (fraza[len(fraza) - 5 : len(fraza) : 1])
# print(f'a. {string_nou}')
# print(f'b. "the" apare de {fraza.count("the")} ori in fraza.')
# print(f'c. Inlocuim "the" cu "THE" si avem: {fraza.replace("the", "THE")} ')
# rock = 'rock'
# print(f'd. Indexul de inceput al cuvantului "rock" este: {fraza.find(rock)}')
# print(f'd. {fraza[0:53]}')

'''10. Exercițiu:
- citește de la tastatură un string;
- verifică dacă primul și ultimul caracter sunt la fel.
Observație: se va folosi un assert.
Atenție: se dorește că programul să fie case insensitive - 'apA' e acceptat.'''
#varianta cand sunt diferite:
# str1 = 'Apa este rece.'
# print(str1)
#
# #varianta cand sunt identice:
# str2 = str1.lower()
# str2 = str2[0:3]
# print(str2)
#
# #cazul cand nu sunt la fel:
# # assert str1[0] == str1[len(str1) - 1], 'nu sunt la fel'
#
# #cazul cand sunt la fel:
# assert str2[0] == str2[len(str2) - 1], 'nu sunt la fel'

'''11. Având stringul '0123456789':
- Afișează doar numerele pare;
- Afișează doar numerele impare;
- hint: folosește slicing, controlează din pas.'''
# sir_numere = '0123456789'
# print(f'Din sirul de numere {sir_numere}: ')
# print(f'Numerele pare sunt: {sir_numere[0::2]}')
# print(f'Numerele impare sunt: {sir_numere[1::2]}')

'''12. Utilizand stringul de la 9.d.
- folosește un assert că să verifici dacă acest string conține doar numere;
- hint: merge cu slicing? Probabil că nu... Ce mai știi atunci legat de
string? Poate găsești o funcție ajutătoare.'''
# str9d = 'Coral is either the stupidest animal or the smartest'
# assert any(char.isdigit() for char in str9d), 'Nu contine numere'
# print('Contine numere')
