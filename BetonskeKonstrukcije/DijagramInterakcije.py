import numpy as np
import matplotlib.pyplot as plt


class DijagramInterakcije:
    def __init__(self):
        self.fck = int(input('Unesi karakteristicnu cvrstocu betona na pritisak fck [MPa]: '))
        self.fcd = 0.85 * self.fck/1.5  # [MPa]
        self.b = float(input('Unesi sirinu preseka b [cm]: '))
        self.b = self.b/100
        self.h = float(input('Unesi visinu preseka h [cm]: '))
        self.h = self.h/100
        self.d1 = float(input('Unesi rastojanje od tezista zategnute armature do zategnute ivice d1 [cm]: '))
        self.d1 = self.d1/100  # [m]
        self.d = self.h - self.d1
        self.d2 = float(input('Unesi rastojanje od tezista pritisnute armature do pritisnute ivice d2 [cm]: '))
        self.d2 = self.d2/100  # [m]
        self.Es = 200  # [GPa]
        self.fyk = 500  # [MPa]
        self.fyd = 500/1.15  # [MPa]
        self.epsilon_yd = self.fyd/self.Es/1000
        # self.As1 = float(input('Unesi povrsinu zategnute armature As1 [cm^2]: '))
        # self.As1 = self.As1/10000
        # self.As2 = float(input('Unesi povrsinu pritisnute armature As2 [cm^2]: '))
        # self.As2 = self.As2 / 10000
        self.alfa_1 = self.d1/self.h
        self.alfa_2 = self.d2 / self.h
        # self.omega1 = (self.As1 * self.fyd)/(self.b * self.h * self.fcd)
        # self.omega2 = (self.As2 * self.fyd) / (self.b * self.h * self.fcd)
        # self.omega = self.omega1 + self.omega2

    def centricni_pritisak(self):
        # epsilon_s1 = self.epsilon_yd
        # epsilon_s2 = epsilon_s1
        # omega1 = (self.As1 * epsilon_s1 * self.Es * math.pow(10, 6)) / (self.b * self.h * self.fcd * 1000)
        # omega2 = (self.As2 * epsilon_s2 * self.Es * math.pow(10, 6)) / (self.b * self.h * self.fcd * 1000)
        # omega = omega1 + omega2
        niz_ni_Rd = np.array([])
        niz_mi_Rd = np.array([])
        omege = np.linspace(0, 0.5, num=2)
        for omega in omege:
            omega1 = 0.5 * omega
            omega2 = 0.5 * omega
            NRd = (1 + omega) * self.b * self.h * self.fcd * 1000
            MRd = (omega2 * (0.5 - self.alfa_2) - omega1 * (0.5 - self.alfa_1)) * self.b * self.h**2 * self.fcd * 1000
            ni_Rd = NRd/(self.fcd * 1000 * self.b * self.h)
            mi_Rd = MRd/(self.fcd * 1000 * self.b * self.h ** 2)
            niz_ni_Rd = np.append(niz_ni_Rd, ni_Rd)
            niz_mi_Rd = np.append(niz_mi_Rd, mi_Rd)
        return np.array([niz_ni_Rd, niz_mi_Rd])

    # TODO Odradi za ostale prave dijagrama interakcije

    def stampa(self):
        centricni_pritisak = self.centricni_pritisak()
        plt.xlabel('\u03BDRd')
        plt.ylabel('\u03BCRd')
        plt.title('Dijagram interakcije')
        plt.plot(centricni_pritisak[0], centricni_pritisak[1], marker='o', color='green', label='Line')
        plt.legend()

        plt.show()


def main():
    dijagram_interakcije = DijagramInterakcije()
    dijagram_interakcije.stampa()


if __name__ == "__main__":
    main()
