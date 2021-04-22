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

    # λ - be_szelesseg
    # φ - be_hosszusag
    # α - ra 
    # δ - dec
    def KN(self, be_ev, be_honap, be_nap, be_szelesseg, be_hosszusag, be_idozona):
        
        a = float(10000.0*be_ev + 100.0*be_honap + be_nap)
        if be_honap <= 2:
            be_honap += 12
            be_ev -= 1
        if a < 15821004.1:
            b = -2 + math.trunc(float((be_ev + 4716)/4)) - 1179
        else:
            b = math.trunc(float(be_ev/400)) - math.trunc(float(be_ev/100)) + math.trunc(float(be_ev/4))
        a = 365.0*be_ev - 679004.0
        JD = 2400000.5 + a + b + math.trunc(float(30.6001*(be_honap+1))) + be_nap
        print(JD)

        # alfa, beta = self.Nap_ekl(JD)
        # print(alfa, beta)
        ra, dec = self.Nap_equ(JD)
        print(ra, dec)

        t = math.acos((math.sin(math.radians(be_hosszusag)) - math.sin(math.radians(be_hosszusag)*math.sin(math.radians(dec)))) / (math.cos(math.radians(be_hosszusag))*math.cos(math.radians(dec))))
        print(t)
        s_kelte = ra - t
        s_nyugta = ra + t
        return (s_kelte, s_nyugta)

nap = Napkelte()
# print(nap.Nap_ekl(2458942.7850))
# print(nap.Nap_ekl(2458942.875))
# print(nap.Nap_equ(2458942.875))
# print(nap.kel_nyugszik(4.5, 15, 45, 0))
# print(nap.KN(2020, 4, 3, 46.770439, 23.591423, 2))

# print(nap.Nap_equ(2458948))
print(nap.Nap_equ(2458947.50))
print(nap.kel_nyugszik(1.145912754428465, 7.300275411264041, 25, 46))

# 2458849
# ev = 2458849
# for i in range(0, 12):
#     c = 0
#     for j in range(0, 30):
#         ev = ev + 1
#         a1, b1 = nap.Nap_ekl(ev)
#         a2, b2 = nap.Nap_ekl(ev+1)
#         c = c + a2 - a1
#     print(i, c%360)
#         c = c + b
# for i in range(2458849, 2459214):
#     print(nap.Nap_ekl(i))
# # 2459214

# a = 2458924
# b = 2459146

# a1, a2 = nap.Nap_ekl(a)
# b1, b2 = nap.Nap_ekl(b)
# print(b2 - a2)
# print(a1 - b1)

# print(nap.Nap_ekl(2458947.79167))
# print(nap.Nap_ekl(2458947.75))
# print(nap.Nap_ekl(2458947.93750))


print(nap.kel_nyugszik(15, 22, 46, 0))