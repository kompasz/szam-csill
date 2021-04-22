import math

class Napkelte:
    def __init__(self):
        
        pass

    def Nap_ekl(self, be_JD):
        T = (be_JD - 2451545) / 36525
        M = 0.993133 + 99.997361 * T
        Mfrac = M - math.floor(M)
        Mrad = 2 * math.pi * Mfrac

        L = 0.7859453 + Mrad / (2 * math.pi) + (6893 * math.sin(Mrad) + 72*math.sin(2 * Mrad) + 6191*T) / 1296000
        Lfrac = L - math.floor(L)
        Lrad = 2 * math.pi * Lfrac
        Lfok = Lrad * 180 / math.pi
        Bfok = 0

        return Lfok, Bfok
        
    # Nap_equ(2458942.875)=0.863906287503828 5.552314928465703
    def Nap_equ(self, be_JD):
        # ekliptikai koordinatak
        # λ - alfa
        # β - beta
        # egyenlitoi koordinatak
        # δ - ra
        # α - dec
        alfa, beta = self.Nap_ekl(be_JD)
        T = (be_JD - 2451545) / 36525
        eps = 23.43929111 - T * (46.8150 + T * (0.00059 - 0.001813 * T)) / 3600    
        eps = math.radians(eps)
        alfa = math.radians(alfa)
        beta = math.radians(beta)
        dec = math.asin(math.sin(eps)*math.cos(beta)*math.sin(alfa) + math.cos(eps)*math.sin(beta))

        ra = math.acos(math.cos(alfa)*math.cos(beta) / math.cos(dec))
        # 1 Radians ... 3.8197 Hour angles
        # n rad     ...  x    hours
        return ra * 3.8197, math.degrees(dec)

    # kel_nyugszik(4.5,15,45,0)=21.4638 248.5293 11.5362 111.4707
    # be_RA -           α
    # be_Dec -          δ
    # be_szelesseg -    φ
    # be_magassag -     h
    def kel_nyugszik(self, be_RA, be_Dec, be_szelesseg, be_magassag):
        t = math.acos(-math.tan(math.radians(be_szelesseg))*math.tan(math.radians(be_Dec)))

        A_nyugta = math.degrees(math.acos(-math.sin(math.radians(be_Dec))/math.cos(math.radians(be_szelesseg))))
        A_kelte = 360 - A_nyugta

        s_kelte = be_RA - math.acos(-math.tan(math.radians(be_szelesseg))*math.tan(math.radians(be_Dec)))*3.8197 + 24
        s_nyugta = (be_RA + math.acos(-math.tan(math.radians(be_szelesseg))*math.tan(math.radians(be_Dec)))*3.8197)%24

        return (s_kelte, A_kelte, s_nyugta, A_nyugta)


    def KN(self, be_ev, be_honap, be_nap, be_szelesseg, be_hosszusag, be_idozona):

        pass

nap = Napkelte()
# print(nap.Nap_ekl(2458942.7850))
# print(nap.Nap_ekl(2458942.875))
# print(nap.Nap_equ(2458942.875))
print(nap.kel_nyugszik(4.5, 15, 45, 0))