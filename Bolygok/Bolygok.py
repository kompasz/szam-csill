from enum import Enum
import numpy as np
import math

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
        Merkur_2000     = [ 0.38709927,      0.20563593,      7.00497902,      48.33076593,     252.25032350,     77.45779628     ]
        Venusz_2000     = [ 0.72333566,      0.00677672,      3.39467605,      76.67984255,     181.97909950,    131.60246718     ]
        Fold_2000       = [ 1.00000261,      0.01671123,     -0.00001531,      0.0,              100.46457166,    102.93768193    ]
        Mars_2000       = [ 1.52371034,      0.09339410,      1.84969142,      49.55953891,      -4.55343205,    -23.94362959     ]
        Jupiter_2000    = [ 5.20288700,      0.04838624,      1.30439695,      100.47390909,      34.39644051,     14.72847983    ]  
        Szaturnusz_2000 = [ 9.53667594,      0.05386179,      2.48599187,      113.66242448,      49.95424423,     92.59887831    ]  
        Uranusz_2000    = [ 19.18916464,      0.04725744,      0.77263783,    74.01692503,      313.23810451,    170.95427630     ]   
        Neptunusz_2000  = [ 30.06992276,      0.00859048,      1.77004347,    131.78422574,      -55.12002969,     44.96476227    ]
        Pluto           = [ 39.48211675,      0.24882730,     17.14001206,    110.30393684,      238.92903833,    224.06891629    ]

        # a
        # e 
        # I 
        # omega
        # w
        # L

        Merkur_kul       = [ 0.00000037,      0.00001906,     -0.00594749,  -0.12534081,        149472.67411175,      0.16047689  ]
        Venusz_kul       = [ 0.00000390,     -0.00004107,     -0.00078890,  -0.27769418,        58517.81538729,      0.00268329   ]
        Fold_kul         = [ 0.00000562,     -0.00004392,     -0.01294668,   0.0,               35999.37244981,      0.32327364   ]
        Mars_kul         = [ 0.00001847,      0.00007882,     -0.00813131,  -0.29257343,        19140.30268499,      0.44441088   ]
        Jupiter_kul      = [ -0.00011607,     -0.00013253,     -0.00183714,  0.20469106,        3034.74612775,      0.21252668    ]
        Szaturnusz_kul   = [ -0.00125060,     -0.00050991,      0.00193609, -0.28867794,        1222.49362201,     -0.41897216    ]
        Uranusz_kul      = [ -0.00196176,     -0.00004397,     -0.00242939,  0.04240589,         428.48202785,      0.40805281    ]
        Neptunusz_kul    = [  0.00026291,      0.00005105,      0.00035372, -0.00508664,         218.45945325,     -0.32241464    ]
        Pluto_kul        = [ -0.00031596,      0.00005170,      0.00004818, -0.01183482,         145.20780515,     -0.04062942    ]

        x = []
        if n == 1:
            x = np.add(Merkur_2000 , julian_evszazadok * Merkur_kul if len(julian_evszazadok * Merkur_kul) != 0 else np.empty(6) )
        elif n == 2:
            x = np.add(Venusz_2000 , julian_evszazadok * Venusz_kul if len(julian_evszazadok * Venusz_kul) != 0 else np.empty(6))
        elif n == 3:
            x = np.add(Fold_2000 , julian_evszazadok * Fold_kul if len(julian_evszazadok * Fold_kul) != 0 else np.empty(6))
        elif n == 4:
            x = np.add(Mars_2000 , julian_evszazadok * Mars_kul if len(julian_evszazadok * Mars_kul) != 0 else np.empty(6))
        elif n == 5:
            x = np.add(Jupiter_2000 , julian_evszazadok * Jupiter_kul if len(julian_evszazadok * Jupiter_kul) != 0 else np.empty(6))
        elif n == 6:
            x = np.add(Szaturnusz_2000 , julian_evszazadok * Szaturnusz_kul if len(julian_evszazadok * Szaturnusz_kul) != 0 else np.empty(6))
        elif n == 7:
            x = np.add(Uranusz_2000 , julian_evszazadok * Uranusz_kul if len(julian_evszazadok * Uranusz_kul) != 0 else np.empty(6))
        elif n == 8:
            x = np.add(Neptunusz_2000 , julian_evszazadok * Neptunusz_kul if len(julian_evszazadok * Neptunusz_kul) != 0 else np.empty(6))
        elif n == 9:
            x = np.add(Pluto_2000 , julian_evszazadok * Pluto_kul if len(julian_evszazadok * Pluto_kul) != 0 else np.empty(6))
        else: 
            raise 'Not supported'
        
        ered = x[:4]
        w = x[5]-x[3]
        ered = np.append(ered, w)
        M = x[4] - x[5]
        ered = np.append(ered, M)        
        return ered

    def szamol_iterativ(self, e, hiba, M):
        E = M
        Ekov = M + e*math.sin(E) 
        while (abs(Ekov - E) > hiba):
            E = Ekov
            Ekov = M + e*math.sin(E)   

        return E

    def Bolygo_ekl(self, n, julian_evszazadok):

        x = self.Palyaelemek(n, julian_evszazadok)
        E = self.szamol_iterativ(x[1], pow(1/10, 14), x[5])

        x_ = x[0] * (math.cos(E) - x[1])
        y_ = x[0] * math.sqrt(1 - pow(x[1], 2)) * math.sin(E)
        z_ = 0

    # TO DO 
    #  Rotate matrix 


bolygok  = Bolygok()
# n= 1, T= 0eseténakívántpályaelemek:
# 0.38709927  0.20563593  7.00497902  48.33076593 29.12703035     174.79252722
# print(bolygok.Palyaelemek(1, 0))
# n= 3, T= 1eseténakívántpályaelemek:
# 1.00000823  0.01666731  -0.01296199     0       103.26095557    356.5760659
# print(bolygok.Palyaelemek(3, 1))

# n= 1, T= 1eseténakívántko ordináták:
# 0.247511514559500   -0.347901498789926  -0.051119438302676
print(bolygok.Bolygo_ekl(1, 1))
# n= 5, T= 0.2eseténakívántko ordináták:
# 4.715437497290996   -1.635903557871500  -0.0981287957651891
# print(bolygok.Bolygo_ekl(5, 0.2))
