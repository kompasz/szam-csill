from enum import Enum
import numpy as np

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
        Merkur_2000     =[ 0.38709893,   0.20563069,  7.00487,  48.33167,  77.45645,  252.25084]
        Venusz_2000     =[ 0.72333199,   0.00677323,  3.39471,  76.68069,  131.53298,  181.97973]
        Fold_2000       =[ 1.00000011,   0.01671022,  0.00005,  -11.26064,  102.94719,  100.46435]
        Mars_2000       =[ 1.52366231,   0.09341233,  1.85061,  49.57854,  336.04084,  355.45332]
        Jupiter_2000    =[ 5.20336301,   0.04839266,  1.30530,  100.55615,  14.75385,  34.40438]  
        Szaturnusz_2000 =[ 9.53707032,   0.05415060,  2.48446,  113.71504,  92.43194,  49.94432]  
        Uranusz_2000    =[ 19.19126393,    0.04716771,   0.76986,   74.22988,   170.96424,   313.23218]   
        Neptunusz_2000  =[ 30.06896348,  0.00858587, 1.76917, 131.72169, 44.97135, 304.88003]

        Merkur_kul = [ 0.00000066, 0.00002527, -23.51, -446.30,  573.57, 538101628.29]
        Venusz_kul = [ 0.00000092, -0.00004938, -2.86, -996.89,  -108.80, 210664136.06]
        Fold_kul = [ -0.00000005, -0.00003804, -46.94, -18228.25,  1198.28, 129597740.63]
        Mars_kul = [ -0.00007221, 0.00011902, -25.47, -1020.19,  1560.78, 68905103.78]
        Jupiter_kul = [ 0.00060737, -0.00012880, -4.15, 1217.17,  839.93, 10925078.35]
        Szaturnusz_kul = [ -0.00301530, -0.00036762, 6.11, -1591.05,  -1948.89, 4401052.95]
        Uranusz_kul = [ 0.00152025, -0.00019150, -2.09, -1681.40,  1312.56, 1542547.79]
        Neptunusz_kul = [  -0.00125196,  0.0000251,  -3.64,  -151.25,   -844.43,  786449.21]

        if n == 1:
            return np.add(Merkur_2000 , julian_evszazadok * Merkur_kul if len(julian_evszazadok * Merkur_kul) != 0 else np.empty(6) )
        elif n == 2:
            return np.add(Venusz_2000 , julian_evszazadok * Venusz_kul if len(julian_evszazadok * Venusz_kul) != 0 else np.empty(6))
        elif n == 3:
            return np.add(Fold_2000 , julian_evszazadok * Fold_kul if len(julian_evszazadok * Fold_kul) != 0 else np.empty(6))
        elif n == 4:
            return np.add(Mars_2000 , julian_evszazadok * Mars_kul if len(julian_evszazadok * Mars_kul) != 0 else np.empty(6))
        elif n == 5:
            return np.add(Jupiter_2000 , julian_evszazadok * Jupiter_kul if len(julian_evszazadok * Jupiter_kul) != 0 else np.empty(6))
        elif n == 6:
            return np.add(Szaturnusz_2000 , julian_evszazadok * Szaturnusz_kul if len(julian_evszazadok * Szaturnusz_kul) != 0 else np.empty(6))
        elif n == 7:
            return np.add(Uranusz_2000 , julian_evszazadok * Uranusz_kul if len(julian_evszazadok * Uranusz_kul) != 0 else np.empty(6))
        elif n == 8:
            return np.add(Neptunusz_2000 , julian_evszazadok * Neptunusz_kul if len(julian_evszazadok * Neptunusz_kul) != 0 else np.empty(6))
        elif n == 9:
            return 'Pluto not a planet.'
        else: 
            raise 'Not supported'
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
