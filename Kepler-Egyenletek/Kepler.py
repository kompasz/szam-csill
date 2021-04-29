import math

# http://www.csun.edu/~hcmth017/master/node16.html

class Kepler:

    def __init__(self):
        pass

    def szamol_iterativ(self, e, hiba, M):
        E = M
        Ekov = M + e*math.sin(E) 
        while (abs(Ekov - E) > hiba):
            E = Ekov
            Ekov = M + e*math.sin(E)   

        return E

    def szamol_newton_method(self, e, hiba, M):

        E = M
        Ekov = E - (E - e*math.sin(E) - M) / (1 - e*math.cos(E))

        while (abs(Ekov - E) > hiba): 
            E = Ekov
            Ekov = E - (E - e*math.sin(E) - M) / (1 - e*math.cos(E))

        return E

    def szamol_mas(self, hiba, M):
        E = M
        Ekov = M + math.sin(E) 
        while (abs(Ekov - E) > hiba):
            E = Ekov
            Ekov = M + math.sin(E)   
            print(E)
        return E

kepler = Kepler()

# M= 0éstetsz®legeseeseténE= 0;
print(kepler.szamol_iterativ(10, pow(1/10, 14), 0))
print(kepler.szamol_newton_method(10, pow(1/10, 14), 0))
# M=πéstetsz®legeseeseténE=π,azaztizenkéttizedesrekerekítve3.141592653590;
print(kepler.szamol_iterativ(10, pow(1/10, 14), math.pi))
print(kepler.szamol_newton_method(10, pow(1/10, 14), math.pi))
# Kepler(0.98,1E-14,3.5)=3.323098922816507.1
print(kepler.szamol_iterativ(0.98, pow(1/10, 14), 3.5))
print(kepler.szamol_newton_method(0.98, pow(1/10, 14), 3.5))

# print(kepler.szamol_iterativ(0.01, pow(1/10, 10), 2))
# print(kepler.szamol_iterativ(0.1, pow(1/10, 10), 1))
# print(kepler.szamol_iterativ(0.99, pow(1/10, 14), 2))
print(kepler.szamol_iterativ(0.1, pow(1/10, 14), 1))
# print(kepler.szamol_mas(pow(1/10, 14), 2))
# print(kepler.szamol_iterativ(0.002, pow(1/10, 14), 0))
# print(math.degrees(kepler.szamol_iterativ(0.02, pow(1/10, 14), math.radians(2))))
# print(kepler.szamol_iterativ(0.99, pow(1/10, 14), math.radians(2)))
