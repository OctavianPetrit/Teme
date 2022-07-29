'''1.Funcție care să calculeze și să returneze suma a două numere'''

# def adder(*num):
#     sum = 0
#     for n in num:
#         sum = sum + n
#     print(f"Suma celor doua numere este : {sum}")
#
# adder(int(input('Primul numar este: ')) + int(input('Al doilea numar este: ')))

'''2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar'''

# def par_impar(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
# print(par_impar(1))

'''3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)'''

# def numar_caractere(nume):
#     return len(nume)-len(' ')
# print(numar_caractere('Petrit Octavian Adrian'))

'''4. Funcție care returnează aria dreptunghiului'''
# def aria_dreptunghi(latime, lungime):
#     A = latime*lungime
#     return A
# print(aria_dreptunghi(2,7))

'''5. Funcție care returnează aria cercului'''

# import math
# def arie_cerc(raza):
#     A = math.pi*raza**2
#     return A
# print(arie_cerc(7))

'''6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.'''


def caracter(sir):
    for x in sir:
        if sir[sir.index(x)] == '?':
            return True
    return False
print(caracter('Este un x in acest sir?'))

'''7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y'''

# def caractere_lower(sir):
#     count_lower = 0
#     count_upper = 0
#     for c in sir:
#         if c.islower():
#             count_lower += 1
#         elif c.isupper():
#             count_upper += 1
#     print('Nr de caractere lower case este', count_lower)
#     print('Nr de caractere upper case este', count_upper)
#
# caractere_lower('Ana ARE mere si pere')

'''8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive'''

# pozitive = []
# def lista_numere(lista):
#     for n in lista:
#         if lista[lista.index(n)] > 0:
#             pozitive.append(n)
#         else:
#             pass
#     return pozitive
# print(lista_numere(lista=[7,-2,3,6,-1,-3]))

'''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.'''

# def comparatie(x,y):
#     if x>y:
#         print(f'Primul numar {x} este mai mare decat {y}')
#     elif x<y:
#         print(f'Al doilea numar {y} este mai mare decat {x}')
#     else:
#         print('Numerele sunt egale')
# comparatie(1,2)

'''10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False'''


# def numere(n,set):
#     if n not in set:
#         set.add(n)
#         print('Am adaugat numarul nou in set',set)
#         return True
#     elif n in set:
#         print('Numarul exista deja in set', set)
#         return False
# print(numere(7,{2,3}))
