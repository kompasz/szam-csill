from enum import Enum

class Bolygok:

    class Bolygok(Enum):

        Merkúr = 1
        Vénusz = 2
        Föld_Hold_baricentruma = 3
        Mars = 4
        Jupiter = 5
        Szeturnusz = 6
        Uránusz = 7
        Neptunusz = 8
        Pluto = 9
        
    def __init__(self):
        
        pass

    def Palyaelemek(self, n, julian_evszazadok):

        pass

    def Bolygo_ekl(self, bolygo_sorszam, julian_evszazadok):

        pass

bolygok  = Bolygok()
# n= 1, T= 0eseténakívántpályaelemek:
# 0.38709927  0.20563593  7.00497902  48.33076593 29.12703035     174.79252722
# print(bolygok.Palyaelemek(1, 0))
# n= 3, T= 1eseténakívántpályaelemek:
# 1.00000823  0.01666731  -0.01296199     0       103.26095557    356.5760659
# print(bolygok.Palyaelemek(3, 1))

# n= 1, T= 1eseténakívántko ordináták:
# 0.247511514559500   -0.347901498789926  -0.051119438302676
# print(bolygok.Bolygo_ekl(1, 1))
# n= 5, T= 0.2eseténakívántko ordináták:
# 4.715437497290996   -1.635903557871500  -0.0981287957651891
# print(bolygok.Bolygo_ekl(5, 0.2))
