import math

class IzvijanjeStuba:
    def __init__(self):
        print('Skripta radi za pravougaone stubove, izvijanje se vrsi oko ose upravne na sirinu stuba b0.\n')
        self.M0 = float(input('Unesi moment savijanja u stubu M0 [kNm]: '))
        self.N0 = float(input('Unesi aksijalnu silu u stubu N0 [kN]: ' ))
        self.l0 = float(input('Unesi duzinu izvijanja stuba l0 [m]: '))
        self.b0 = float(input('Unesi sirinu stuba za koju se kontrolise izvijanje b0 [m]: '))
        if self.b0 != None:
            self.d = self.b0 - 0.05
            print(f'Za staticku visinu d je uzeta vrednost: d = {self.d} [m]')
        self.h0 = float(input('Unesi visinu stuba h0 [m]: '))
        self.fck = float(input('Unesi karakteristicnu cvrstocu na pritisak betona fck [MPa]: '))
        self.A = self.h0*self.b0
        self.fcd = 0.85*self.fck*1000/1.5

    def moment_imperfekcije(self):
        e0 = max(0.02, self.b0/30, self.l0/400) # ei je ubacen kao l0/400
        M0_Ed = self.N0*e0
        return M0_Ed

    def kontrola_vitkosti(self):
        n = self.N0/(self.A * self.fcd)
        l_lim = 20/math.sqrt(n) # lambda_limit
        l_max = 70/math.sqrt(n) # lambda_max
        l = self.l0/math.sqrt((math.pow(self.b0, 3)*self.h0/12)/self.A) # lambda preseka

        if (l > l_lim) and (l < l_max):
            print('\n')
            print('Potrebno je uracunati efekte drugog reda prilikom izracunavanja momenta!\n\n'
                  f'\u03BB_lim = {round(l_lim,2)} < \u03BB = {round(l,2)} < \u03BB_max = {round(l_max,2)}')
        elif l <= l_lim:
            print('\n')
            print('Nije potrebno uracunati efekte drugog reda\n'
                  f'\u03BB {round(l,2)} <= \u03BB_lim = {round(l_lim)}')
            exit()
        else:
            print('\n')
            print(f'Vitkost \u03BB = {l} je veca od maksimalne vitkosti \u03BB_max = {l_max}, proveriti druge metode za proracun')
            exit()
        return l

    def k_fi_koeficijent(self):
        l = self.kontrola_vitkosti()
        beta = 0.35 + self.fck/200 - l/150
        k_fi = 1 + beta * 2 # fi efektivno je uzeto da je 2 sto je na strani sigurnosti
        return k_fi

    def moment_drugog_reda(self):
        k_fi = self.k_fi_koeficijent()
        M2 = self.N0*0.1*math.pow(self.l0, 2)*k_fi*0.002174/(0.45 * self.d)
        return M2

    def ukupni_moment(self):
        Kr = float(input('Unesi koeficijent nominalne krivine Kr (Kr < 1): '))
        M0_Ed = self.moment_imperfekcije()
        M2 = self.moment_drugog_reda()
        M_Ed = M0_Ed + M2*Kr
        mi_Ed = round(M_Ed/(math.pow(self.b0, 2)*self.h0*self.fcd), 3)
        print('\n')
        print('Vrednosti \u03BD_Ed i \u03BC_Ed su\n\n'
              f'\u03BD_Ed = {round(self.N0/(self.A * self.fcd), 3)}\n'
              f'\u03BC_Ed = {mi_Ed}')
    #TODO Odraditi da skripta pronadje Kr iz uslova ravnoteze


def main():
    klasa = IzvijanjeStuba()
    klasa.ukupni_moment()


if __name__ == "__main__":
    main()
