'''1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()'''
import math
#
# class Cerc:
#     raza = None
#     culoare = None
#     def __init__ (self, raza, culoare):
#         self.raza = raza
#         self.culoare = culoare
#     def descrie_cerc(self):
#         print(f'Cercul are raza de {self.raza} cm si culoarea {self.culoare}')
#
#     def aria(self):
#         return print(f'Aria cercului este: {self.raza ** 2 * math.pi} cm^2')
#
#     def diametrul(self):
#         return print(f'Diametrul cercului este {self.raza * 2} cm')
#
#     def circumferinta(self):
#         return print(f'Circumferinta cercului este: {self.raza * 2 * math.pi} cm')
#
# cerc1 = Cerc(raza=3, culoare='Verde')
# cerc2 = Cerc(raza=9, culoare='Negru')
# print('-----------------------Cerc 1------------------')
# cerc1.descrie_cerc()
# cerc1.aria()
# cerc1.diametrul()
# cerc1.circumferinta()
# print('-----------------------Cerc 2------------------')
# cerc2.descrie_cerc()
# cerc2.aria()
# cerc2.diametrul()
# cerc2.circumferinta()



'''2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul'''

# class Dreptunghi:
#     lungime = None
#     latime = None
#     culoare = None
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#     def descrie(self):
#         print(f'Dreptunghiul are lungimea de {self.lungime} cm, latimea de {self.latime} cm si culoarea {self.culoare}')
#
#     def aria(self):
#         return print(f'Aria dreptunghiului este: {self.lungime * self.latime} cm^2')
#
#     def perimetrul(self):
#         return print(f'Perimetrul dreptunghiului este: {2 * (self.lungime + self.latime)}')
#
#     def schimba_culoarea(self, culoare_noua):
#         self.culoare = culoare_noua
#
# dreptunghi1= Dreptunghi(lungime = 78, latime = 50, culoare = 'Portocaliu')
# dreptunghi2= Dreptunghi(lungime = 24, latime = 12, culoare = 'Galben')
# print('-----------------------Dreptunghi 1------------------')
# dreptunghi1.descrie()
# dreptunghi1.aria()
# dreptunghi1.perimetrul()
# dreptunghi1.schimba_culoarea(culoare_noua = 'Alb')
# dreptunghi1.descrie()
# print('-----------------------Dreptunghi 2------------------')
# dreptunghi2.descrie()
# dreptunghi2.aria()
# dreptunghi2.perimetrul()
# dreptunghi2.schimba_culoarea(culoare_noua = 'Rosu')
# dreptunghi2.descrie()

'''3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)'''

# class Angajat:
#     nume = None
#     prenume = None
#     salariu = None
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descrie(self):
#         print(f'Angajatul {self.nume} {self.prenume} are salariul de {self.salariu} RON')
#
#     def nume_complet(self):
#         return print(f'Numele complet al angajatului este: {self.nume} {self.prenume}')
#
#     def salariul_lunar(self):
#         return print(f'Angajatul are salariul lunat de {self.salariu} RON')
#
#     def salariu_anual(self):
#         print(f'Angajatul are salariul anual de {self.salariu * 12} RON')
#
#     def marire_salariu(self):
#         procent = 15 / 100 * self.salariu
#         return print(f'Salariul lunar dupa marire este: {self.salariu + procent}')
#
# angajat1 = Angajat(nume='Petrit', prenume='Octavian', salariu=6500)
# angajat2 = Angajat(nume='Mihalache', prenume='Alin', salariu=7900)
# print('-----------------------Angajat 1------------------')
# angajat1.descrie()
# angajat1.nume_complet()
# angajat1.salariul_lunar()
# angajat1.salariu_anual()
# angajat1.marire_salariu()
# print('-----------------------Angajat 2------------------')
# angajat2.descrie()
# angajat2.nume_complet()
# angajat2.salariul_lunar()
# angajat2.salariu_anual()
# angajat2.marire_salariu()

'''4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)'''

# class Cont:
#     iban = None
#     titular_cont = None
#     sold = None
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} RON')
#
#     def debitare_cont(self, suma_debitata):
#         self.sold = self.sold - suma_debitata
#         return print(f'Ati retras suma de {suma_debitata} RON si mai aveti in cont {self.sold} RON')
#
#     def creditare_cont(self, suma_creditata):
#         self.sold = self.sold + suma_creditata
#         return print(f'Suma creditata este de {suma_creditata} RON si aveti in cont {self.sold} RON')
#
# cont1 = Cont(iban = 'ROBTLR1947649305', titular_cont = 'Petrit Octavian', sold = 5673)
# cont2 = Cont(iban ='ROBTLR1323240076', titular_cont = 'Paduraru Alexandra', sold = 3000)
# print('-----------------------Cont 1------------------')
# cont1.afisare_sold()
# cont1.debitare_cont(suma_debitata = 50)
# cont1.creditare_cont(suma_creditata = 345)
# print('-----------------------Cont 2------------------')
# cont2.afisare_sold()
# cont2.debitare_cont(suma_debitata = 342)
# cont2.creditare_cont(suma_creditata = 4500)
'''Exerciții Opționale'''

'''1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs  |cantitate | preț bucată | Total
Telefon |     7    |      700    | 49000'''

# import datetime
#
# class Factura:
#     seria = 'TZ'
#     numar = None
#     nume_produs = None
#     cantitate = None
#     pret_buc = None
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitate(self, cantitate):
#         self.cantitate = cantitate
#
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#
#     def genereaza_factura(self):
#         print(f'Factura seria {self.seria} numar {self.numar} \n'
#               f'Data: {datetime.date.today()} \n'
#               f'PRODUS | CANTITATE | PRET BUCATA | TOTAL \n'
#               f' {self.nume_produs}  |      {self.cantitate}      |     {self.pret_buc}    |     {self.pret_buc * self.cantitate}     ')
# factura1 = Factura(843564, 'Caise', 342, 5)
# factura2 = Factura(843523, 'Telefon', 42, 5435)
# print('-----------------------Factura 1------------------')
# factura1.genereaza_factura()
# factura1.schimba_pretul(7)
# factura1.genereaza_factura()
# factura1.schimba_cantitate(320)
# factura1.genereaza_factura()
# factura1.schimba_nume_produs('Prune')
# factura1.genereaza_factura()
# print('-----------------------Factura 2------------------')
# factura2.genereaza_factura()
# factura2.schimba_pretul(4999)
# factura2.genereaza_factura()
# factura2.schimba_cantitate(49)
# factura2.genereaza_factura()
# factura2.schimba_nume_produs('Bicicleta')
# factura2.genereaza_factura()

'''2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0'''

# class Masina:
#     MARCA = 'Mazda'
#     model = None
#     viteza_maxima = None
#     viteza_actuala = 0
#     culoare = 'Alba'
#     culori_disponibile = ('Rosie', 'Verde', 'Galbena', 'Neagra', 'Gri', 'Albastra')
#     inmatriculata = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#     def descrie(self):
#         print(f'Masina {self.MARCA}, model {self.model}, are o viteza maxima de {self.viteza_maxima} \n'
#               f'Aceasta se deplaseaza acum cu viteza de {self.viteza_actuala} km/h \n'
#               f'Masina este de culoare {self.culoare}')
#
#     def inmatriculare(self, inmatriculata):
#         self.inmatriculata = inmatriculata
#
#     def vopseste(self, culoare):
#         if culoare in self.culori_disponibile:
#             self.culoare = culoare
#         else:
#             print('Aceasta culoare nu este diponibila')
#             pass
#
#     def accelereaza(self, viteza):
#         if viteza < self.viteza_maxima:
#             self.viteza_actuala = viteza
#         elif viteza < 0:
#             print('EROARE! Masina merge in marsarier')
#         else:
#             self.viteza_actuala = self.viteza_maxima
#
# masina1 = Masina('3 BK', 220,)
# masina2 = Masina('5', 180,)
# print('-----------------------Masina 1------------------')
# masina1.descrie()
# masina1.inmatriculare(True)
# masina1.vopseste('Neagra')
# masina1.accelereaza(199)
# masina1.descrie()
# print('-----------------------Masina 2------------------')
# masina2.descrie()
# masina2.inmatriculare(True)
# masina2.vopseste('Rosie')
# masina2.accelereaza(169)
# masina2.descrie()


