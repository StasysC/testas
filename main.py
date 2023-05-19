class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = atlyginimas


    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, naujas_atlyginimas):
        if naujas_atlyginimas < 0:
            print("Atlyginimas negali buti neigiamas")
        else:
            self.__atlyginimas = naujas_atlyginimas





domas = Darbuotojas("Domas", "Adomaitis", 1200)


print(domas.Darbuotojas.__atlyginimas)
