import numpy as np
import math

class Alapok:
    def __init__(self):
        pass
    
    # deg_dms(123.12456789123) = (123.00, 7.00, 28.44);
    def deg_dms(self, deg):

        if deg < 0 and deg >= 360:
            raise ValueError('Bemenet nem megfelelo.')

        if deg > 0:
            d = math.floor(deg)
        else:
            d = math.ceil(deg)
        minimum = 60*(deg - d)
        m = math.floor(minimum)
        s = 60*(minimum - m)

        return (d, m, s)

    # dms_deg(11,22,33.4567) = 11.375960194444444; NICE
    def dms_deg(self, d, m, s):
        deg = d + float(m/60) + float(s/36000)
        return deg

    # deg_rad(345.678) = 6.033219251708959;
    def deg_rad(self, deg):

        if deg < 0 and deg >= 360:
            raise ValueError('Bemenet nem megfelelo.')

        rad = float(deg * math.pi / 180)
        
        if rad < 0 and rad >= 2*math.pi:
            raise ValueError('Szamolas eredmeny nem megfelelo.')

        return rad

    # rad_deg(6.033219251708959) = 345.678;
    def rad_deg(self, rad):

        if rad < 0 and rad >= 2*math.pi:
            raise ValueError('Bemenet nem megfelelo.')

        deg = float(rad * 180 / math.pi)

        if deg < 0 and deg >= 360:
            raise ValueError('Szamolas eredmeny nem megfelelo.')

        return deg

    def Rot_x(self, phi):
        forgatasi_matrix = [[1, 0, 0], [0, math.cos(phi), math.sin(phi)], [0, -math.sin(phi), math.cos(phi)]]
        return forgatasi_matrix
    
    def Rot_y(self, phi):
        forgatasi_matrix = [[math.cos(phi), 0, -math.sin(phi)], [0, 1, 0], [math.sin(phi), 0, math.cos(phi)]]
        return forgatasi_matrix
    
    def Rot_z(self, phi):
        forgatasi_matrix = np.around([[math.cos(phi), math.sin(phi), 0], [-math.sin(phi), math.cos(phi), 0], [0, 0, 1]])
        return forgatasi_matrix
    
    # rad_deg(sc_rad(-0.5,-sqrt(3)/2)) = 210.
    def sc_rad(self, sr, cr):

        if sr < -1 and sr > 1 and cr < -1 and cr > 1:
            raise ValueError('Bemenet nem megfelelo.')

        if sr >= 0:
            r = math.acos(cr)
        else:
            r = 2 * math.pi - math.acos(cr)

        if r < 0 and r >= 2*math.pi:
            raise ValueError('Szamolas eredmeny nem megfelelo.')

        return r

alapok = Alapok()
print(alapok.deg_dms(111.223344))
print(alapok.dms_deg(23,27,0))
print(alapok.deg_rad(alapok.dms_deg(23,27,0)))
print(alapok.rad_deg(3.1415))
print(np.around(alapok.rad_deg(alapok.sc_rad(-0.5,-math.sqrt(3)/2))))
print(alapok.Rot_x(alapok.deg_rad(alapok.dms_deg(23,27,0))))
print(alapok.deg_rad(55))
print(alapok.Rot_x(alapok.deg_rad(44)))

print(alapok.rad_deg(alapok.sc_rad(float(math.sqrt(2)/2), float(-1*math.sqrt(2)/2))))