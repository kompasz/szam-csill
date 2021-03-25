# from ..alapok import Alapok 
import math
import numpy as np

class Koordinatak:

    def __init__(self):

        pass

    # be_JD - tetszoleges Julian-datum
    def JD_T(self, be_JD):
        return (be_JD - 2451545) / 36525

    # be_T - 2000.01.01.12h(UT)-tol eltelt Julián-évszázadok száma
    def Eps(self, be_T):
        ki_Eps = None

        return 23.43929111 - be_T * (46.8150 + be_T * (0.00059 - 0.001813 * be_T)) / 3600

    # be_RA  - ∈ [0,24) óra
    # be_Rec - ∈ [−90,90] ívfok
    # be_T   - 2000.01.01.12h(UT)-tol eltelt Julián-évszázadok száma
    def Ekv_Ekl(self, be_RA, be_Rec, be_T):
        if be_RA < 0 or be_RA >= 24:
            raise Exception('Bemenet nem megfelelo')
        if be_Rec < -90 or be_Rec > 90:
            raise Exception('Bemenet nem megfelelo')
        eps = self.Eps(be_T)
        be_RA = 360 * be_RA / 24 

        ered_beta = -1*math.sin(math.radians(eps))*math.cos(math.radians(be_Rec))*math.sin(math.radians(be_RA)) + math.cos(math.radians(eps))*math.sin(math.radians(be_Rec))
        ered_beta = math.degrees(math.asin(ered_beta))
        # ered_lambda = (math.cos(math.radians(be_Rec)) * math.cos(math.radians(be_RA))) / math.cos(math.radians(ered_beta))
        # ered_lambda = math.degrees(math.acos(ered_lambda))
        ered_lambda = (math.cos(math.radians(eps))*math.cos(math.radians(be_Rec))*math.sin(math.radians(be_RA)) + math.sin(math.radians(eps))*math.sin(math.radians(be_Rec))) / math.cos(math.radians(ered_beta))
        ered_lambda = math.degrees(math.asin(ered_lambda))
        return ered_lambda, ered_beta

    # be_lambda - 
    # be_beta   - 
    # be_T      - 2000.01.01.12h(UT)-tol eltelt Julián-évszázadok száma
    def Ekl_Ekv(self, be_lambda, be_beta, be_T):
        ered_Rec, ered_Dec = None 

        return ered_Rec, ered_Dec

kor = Koordinatak()

print(kor.JD_T(2531975.00000))
# print(kor.Eps(kor.JD_T(2458927.01042)))
# print(kor.Ekv_Ekl(23.955, -23.47, kor.JD_T(2488069.50000)))
# print(kor.Ekv_Ekl(6.456, 46.47, 1.23))
# print(kor.Eps(kor.JD_T(2462612.50000)))



