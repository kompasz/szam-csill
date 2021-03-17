import numpy as np
import math
import locale
import datetime
import calendar

class Datum:
    def __init__(self):
        pass
    
    # Visszaterit egy tetszoleges idopontnak megfelelo Julian datumot.
    def JD(self, ev, honap, nap, ora):
        
        a = float(10000.0*ev + 100.0*honap + nap)
        if honap <= 2:
            honap += 12
            ev -= 1
        if a < 15821004.1:
            b = -2 + math.trunc(float((ev + 4716)/4)) - 1179
        else:
            b = math.trunc(float(ev/400)) - math.trunc(float(ev/100)) + math.trunc(float(ev/4))
        a = 365.0*ev - 679004.0
        return 2400000.5 + a + b + math.trunc(float(30.6001*(honap+1))) + nap + float(ora/24.0)

    # Visszaterit egy tetszoleges idopontnak megfelelo Modositott Julian datumot.
    def MJD(self, ev, honap, nap, ora):
        a = float(10000.0*ev + 100.0*honap + nap)
        if honap <= 2:
            honap += 12
            ev -= 1
        if a < 15821004.1:
            b = -2 + math.trunc(float((ev + 4716)/4)) - 1179
        else:
            b = math.trunc(float(ev/400)) - math.trunc(float(ev/100)) + math.trunc(float(ev/4))
        a = 365.0*ev - 679004.0
        return a + b + math.trunc(float(30.6001*(honap+1))) + nap + float(ora/24.0)

    # Visszaterit egy Julian datumnak megfelelo naptari idopontot
    def Datum(self, jd):
        jd = jd + 0.5
        
        F, I = math.modf(jd)
        I = int(I)
        
        A = math.trunc((I - 1867216.25)/36524.25)
        
        if I > 2299160:
            B = I + 1 + A - math.trunc(A / 4.)
        else:
            B = I
            
        C = B + 1524
        
        D = math.trunc((C - 122.1) / 365.25)
        
        E = math.trunc(365.25 * D)
        
        G = math.trunc((C - E) / 30.6001)
        
        day = C - E + F - math.trunc(30.6001 * G)
        
        if G < 13.5:
            month = G - 1
        else:
            month = G - 13
            
        if month > 2.5:
            year = D - 4716
        else:
            year = D - 4715
            
        return year, month, day

    def JD_2_MJD(self, jd):
        return jd - 2400000.5

    def MJD_2_JD(self, mjd):
        return mjd + 2400000.5

    # Ellenorzi, hogy egy datum valos-e
    def DatumEllenor(self, ev, honap, nap, ora=0):

        nap += math.trunc(ora/24.0)  
    
        try : 
            datetime.datetime(int(ev), int(honap), int(nap)) 
        except ValueError : 
            return False
            
        return True
    
    # Visszateriti, hogy az ev hanyadik napja es a het melyik napja
    def Nap(self, ev, honap, nap, ora=0):
        nap += math.trunc(ora/24.0)  
        no_nap = datetime.datetime(int(ev), int(honap), int(nap)).timetuple().tm_yday
        no_het = datetime.datetime(int(ev), int(honap), int(nap)).weekday()
        return no_nap, no_het+1

    def Szokoev(self, ev):
        return calendar.isleap(ev)


datum = Datum()
# print(datum.JD(2001, 10, 11, 23.74))
# print(datum.JD(1800, 1, 1, 0))
# print(datum.JD(1900, 1, 1, 0))
# print(datum.JD(2000, 1, 1, 0))
# print(datum.JD(2020, 3, 18, 6.5))
# print(datum.MJD(1234, 11, 15, 11.2))

# print(datum.JD_2_MJD(datum.JD(1700, 1, 1, 0)))
# print(datum.Datum(2456789.0))

# print(datum.DatumEllenor(1100, 2, 29))
# print(datum.DatumEllenor(1582, 10, 10))
# print(datum.DatumEllenor(2100, 2, 29))
# print(datum.DatumEllenor(1700, 2, 29))
# print(datum.DatumEllenor(1582, 10, 10))

# print(datum.Nap(2030, 4, 1))
# print(datum.Nap(2024, 9, 15))
# print(datum.Nap(1848, 3, 15))

# print(datum.Szokoev(3100))

# print(69*365 + 30 + 31 + 25 + 31 + 21)