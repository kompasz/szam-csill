# import tkinter as tk

class Csillagido:

    def __init__(self):
        pass
    
    # be_MJD  - megfigyelesi ido (0h - nek megfelelo Julian-Datum) 
    # be_MJD0 - megfigyelesi datum (0h - nek megfelelo Julian-Datum)
    # be_UT   - tetszoleges valasztott idopont (viliagido)
    def GSTH(self, be_MJD, be_MJD0 = 0 , be_UT = 0):
        if be_MJD0 == 0:
            be_MJD0 = be_MJD
        JD = be_MJD + 2400000.5
        JD0 = be_MJD0 + 2400000.5
        T = (JD - 2451545) / 36525
        T0 = (JD0 - 2451545) / 36525
        return (24110.54841 + 8640184.812866 * T0 + 1.0027379093 * be_UT + 0.093104 * pow(T, 2) - 0.0000062 * pow(T, 3)) / 3600 % 24

    def csillagido(self, be_hosszusag):
        ki_ora = None
        ki_perc = None
        ki_masodperc = None
        
        for i in range(0, 24):
            print(i, self.GSTH(0, i, be_hosszusag))
    
        return ki_ora, ki_perc, ki_masodperc

    def EqvHor(self, be_JD, be_hosszusag, be_szelesseg, be_rektaszcenzio, be_deklinacio):
        ki_oraszog = None
        ki_deklinacio = None
        ki_azimut = None
        ki_magassag = None

        return ki_oraszog, ki_deklinacio, ki_azimut, ki_magassag

    def create_widget(self, name, text, data):
        pass

    def GUI(self):
        pass

cs = Csillagido()
# print(cs.GSTH(58940))
# print(cs.GSTH(58936.40449))

print(cs.csillagido(15.5))