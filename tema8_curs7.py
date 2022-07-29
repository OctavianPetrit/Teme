'''ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’'''

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14
    @abstractmethod
    def aria (self):
        pass

    @classmethod
    def descrie (self):
        print('Cel mai probabil am colturi')

'''INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură'''
'''ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)'''
class Patrat(FormaGeometrica):

    def __int__(self, latura):
        self.__latura = latura
    def aria(self):
        print(f'Aria patratului este {self.__latura ** 2}')
    def get_latura(self):
        return self.__latura
    def set_latura(self):
        self.__latura = lungime_latura
    def del_latura(self):
        self.__latura = None
    def descrie(self):
        print('Eu am 4 colturi identice')

'''Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)'''

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza
    def aria(self):
        print(f'Aria cercului este: {self.PI*self.__raza**2}')
    def get_raza(self):
        return self.__raza
    def set_raza(self,lungime_raza):
        self.__raza=lungime_raza
    def del_raza(self):
        self.__raza=None
    def descrie(self):
        print('Eu nu am colturi')

'''POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui'''

patrat1 = Patrat()

print(patrat1.get_latura())
patrat1.aria()
patrat1.set_latura()
patrat1.aria()
patrat1.descrie()
print(patrat1.get_latura())



cerc1 = Cerc()

cerc1.descrie()
print(c1.get_raza())
cerc11.aria()
cerc11.set_raza()
cerc11.aria()
print(cerc11.get_raza())
