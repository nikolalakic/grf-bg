import math
import numpy as np
finiz = np.array([0.503, 0.785, 1.13], dtype=float)
sniz = np.array([20, 15, 12.5, 10, 7.5], dtype=float)
NEd = float(input('Unesi normalnu silu NEd [kN]: '))
b = float(input('Unesi sirinu preseka b [cm]: '))
h = float(input('Unesi visinu preseka h [cm]: '))
fckMPA = int(input('Unesi karakteristicnu cvrstocu betona na pritisak fck [MPa]: '))
fcd = 0.85*fckMPA/1.5
fyd = 500/1.15
esyd = fyd/200000
nied = NEd/(b*0.01*0.01*h*fcd*1000)
if nied > 0.65:
    print('Normalizovana sila \u03BD,Ed je veca od 0.65! Povecaj marku betona ili dimenzije stuba!')
else:
    q0 = float(input('Unesi osnovnu vrednost faktora ponasanja q0: '))
    if nied <= 0.2 and q0 <= 2:
        print('\nPrimenjuju se pravila iz EC2!')
        exit()
    if nied > 0.2:
        b0 = float(input('Unesi sirinu b0 utegnutog preseka (osno rastojanje uzengija u jednom pravcu) [cm]: '))
        h0 = float(input('Unesi visinu h0 utegnutog preseka (osno rastojanje uzengija u jednom pravcu) [cm]: '))
        T = float(input('Unesi period oscilovanja konstrukcije u posmatranom pravcu T [s]: '))
        Tc = float(input('Unesi period Tc [s]: '))
        n_niz = np.array([int(n) for n in input('Unesi redom broj pojedinacnih razmaka izmedju pridrzanih sipki n odvojenih razmakom (npr: 2 4 3): ').split()])
        bi_niz = np.array([float(bi) for bi in input('Unesi redom rastojanja bi [cm] uz postovanje prethodnog input-a odvojenih razmakom (npr: 14.4 17 19.2): ').split()])
        if len(n_niz) != len(bi_niz):
            print('\nBroj rastojanja ne odgovara unetim rastojanjima!')
            exit()
        bi_niz = math.pow(bi_niz, 2)
        proizvod = np.sum(n_niz*bi_niz)
        print(proizvod)
        a = int(input('Ako je armatura klase B unesi 1, ako je klase C unesi 0: '))
        ObimUzg = float(input('Unesi obim uzengija koje sluze za pridrzavanje [cm]: '))
        if a == 1 and T >= Tc:
            mfi = 1.5*(2*q0-1)
        elif (a == 1 and T < Tc):
            mfi = 1.5*(1 + 2*(q0-1)*Tc/T)
        elif ((a == 0) and (T >= Tc)):
            mfi = 2*q0-1
        else:
            mfi = 1 + 2 * (q0 - 1) * Tc / T
        alfan = 1 - proizvod/(6*b0*h0)
        for x in finiz:
            Vsw = x*ObimUzg
            for p in sniz:
                alfas = (1 - p / (2 * b0)) * (1 - p / (2 * h0))
                alfa = alfas * alfan
                Vco = b0 * h0 * p
                omegawdprov = (Vsw*fyd)/(Vco*fcd)
                omegawdreq = 30 * mfi * nied * esyd * b / b0 - 0.035
                omegawdreq = omegawdreq/alfa
                if (omegawdprov >= omegawdreq):
                    print('\nAs(1) = ', x,'[cm^2]', 'na s =', p,'[cm]'+ '............OK!')
                    break
                else:
                    print("\nAs(1) =", x,'[cm^2]', 'na s =', p,'[cm]'+ ' ne zadovoljava')
                    if x == 1.13 and p == 7.5:
                        print('\n>>>>>Nedovoljno utezanje stuba!')
