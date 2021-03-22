import numpy as np

class Husvet:

    def __init__(self):
        
        pass

    # 1. Feladat
    def husvet_datum_gergely(self, ev):
        if ev < 1583:
            raise ValueError('Bemenet nem megfelelo.')
        a = int(ev % 19)
        b = int(ev / 100)
        c = int(ev % 100)
        d = int(b / 4)
        e = int(b % 4)
        f = int((b + 8) / 25)
        g = int((b - f  + 1) / 3)
        h = int((19 * a + b - d - g + 15) % 30)
        i = int(c / 4)
        k = int(c % 4)
        l = int((32 + 2 * e + 2 * i - h - k) % 7)
        m = int((a + 11 * h + 22 * l) / 451)
        n = int((h + l - 7 * m + 114) / 31)
        p = int((h + l - 7 * m + 114) % 31)
        return n, p + 1

    # 2. Feladat
    def husvetok_tablazat(self):
        husvetok = []
        for i in range(2019, 2100):
            husvetok.append(self.husvet_datum_gergely(i))

        return husvetok

    # 3. Feladat
    def husvet_legkorabbi_datum(self):
        elso_honap = 4
        elso_nap = 1

        for i in range(1583, 2999):
            honap, nap = self.husvet_datum_gergely(i)
            if honap * 31 + nap < elso_honap * 31 + elso_nap:
                elso_honap = honap
                elso_nap = nap 

        return elso_honap, elso_nap

    # 4. Feladat
    def husvet_legkesobbi_datum(self):
        utolso_honap = 4
        utolso_nap = 1

        for i in range(2101, 2200):
            honap, nap = self.husvet_datum_gergely(i)
            if honap * 31 + nap > utolso_honap * 31 + utolso_nap:
                utolso_honap = honap
                utolso_nap = nap 

        return utolso_honap, utolso_nap

    # 5. Feladat
    def husvet_leggyakoribb_datum(self, kezdeti_ev, zaro_ev):
        husvet_rel_gyakorisag = np.zeros((12, 32))
        leggyakoribb_datum = None

        for i in range(kezdeti_ev, zaro_ev):
            honap, nap = self.husvet_datum_gergely(i)
            husvet_rel_gyakorisag[honap][nap] += 1

        maximum = -1
        for i in range(0, 11):
            for j in range(0, 31):
                if maximum < husvet_rel_gyakorisag[i][j]:
                    maximum = husvet_rel_gyakorisag[i][j]
                    leggyakoribb_datum = i, j

        return husvet_rel_gyakorisag, leggyakoribb_datum

    # 6. Feladat
    def kov_husvet_biz_datumon(self, honap, nap):
        ev = 2019
        kereses_honap, kereses_nap = self.husvet_datum_gergely(ev)
        print(kereses_honap, kereses_nap)
        while not(kereses_honap == honap and kereses_nap == nap):
            ev += 1
            kereses_honap, kereses_nap = self.husvet_datum_gergely(ev)    

        return ev

    # BONUSZ

    # 7. Feladat
    def husvet_datum_julianus(self, ev):
        a = int(ev % 4)
        b = int(ev % 7)
        c = int(ev % 19)
        d = int((19 * c + 15) % 30)
        e = int((2 * a + 4 * b - d + 34) % 7)
        f = int((d + e + 114) / 31)
        g = int((d + e + 114) % 31)
        return f, g + 1

    # 8. Feladat
    def husvetok_egybeesnek(self):
        evek = []
        for i in range(2000, 2100):
            gergely_honap, gergely_nap = self.husvet_datum_gergely(i)
            julianus_honap, julianus_nap = self.husvet_datum_julianus(i)
            print(gergely_honap, gergely_nap, julianus_honap, julianus_nap)
            julianus_nap += 13
            julianus_honap += int(julianus_nap / 31)
            julianus_nap = int(julianus_nap % 31)
            print(gergely_honap, gergely_nap, julianus_honap, julianus_nap)
            if gergely_honap == julianus_honap and gergely_nap == julianus_nap:
                evek.append(i)
        return evek

husvet = Husvet()
# print(husvet.husvet_datum_gergely(1583))
# print(husvet.husvet_datum_gergely(1818))
# print(husvet.husvet_datum_gergely(1848))
# print(husvet.husvet_datum_gergely(1886))
# print(husvet.husvet_datum_gergely(1943))
# print(husvet.husvet_datum_gergely(1956))
# print(husvet.husvet_datum_gergely(1989))
# print(husvet.husvet_datum_gergely(2000))
# print(husvet.husvet_datum_gergely(2018))
# print(husvet.husvet_datum_gergely(2019))
# print(husvet.husvet_datum_gergely(2038))
# print(husvet.husvet_datum_gergely(2050))
# print(husvet.husvet_datum_gergely(2100))
# print(husvet.husvet_datum_gergely(2285))

# print(husvet.husvet_datum_julianus(179))
# print(husvet.husvet_datum_julianus(711))
# print(husvet.husvet_datum_julianus(1243))

# print(husvet.husvetok_tablazat())

h = husvet.husvetok_tablazat()
# print(len(h))
for i in range(len(h)):
    j = i + 1
    while h[i] != h[j] and j < len(h)-1:
        j+=1
        # print(j)
    print (j - i)

# print(husvet.husvet_legkorabbi_datum())

# print(husvet.husvet_legkesobbi_datum())

# h = husvet.husvet_leggyakoribb_datum(2001, 2100)
# print(h)
# print(h[3])

# print(husvet.kov_husvet_biz_datumon(4, 1))

# print(husvet.husvetok_egybeesnek())


# print(husvet.husvet_datum_gergely(2030))

# print(husvet.husvet_datum_gergely(2030))
# print(husvet.husvet_datum_gergely(2020))
