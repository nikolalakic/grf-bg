import pandas as pd
import numpy as np
import math
import os

if 'CSTRavanskiPodaci.csv' not in os.listdir():
    print('Fali fajl pod nazivom "Q4SavijanjePodaci.csv", ako je obrisan skini ga sa riznice https://github.com/nikolalakic/grf-bg/tree/master/MKE')
    exit()

df = pd.read_csv('CSTRavanskiPodaci.csv', skipinitialspace=True, )
x_koordinate = df['x [m]'].to_numpy()
y_koordinate = df['y [m]'].to_numpy()


def kontrolatacaka(niz_koordinata):
    if len(niz_koordinata) != 3:
        indeksi_nan = np.argwhere(np.isnan(niz_koordinata))
        indeks = int(min(indeksi_nan))
        niz_koordinata = niz_koordinata[0:indeks]
        return niz_koordinata


x_koordinate = kontrolatacaka(x_koordinate)
y_koordinate = kontrolatacaka(y_koordinate)

if len(x_koordinate) and len(y_koordinate) != 3:
    print('Broj unetih tacaka je manji od 3, ili nije uneta vrednost koordinate tacke za x ili y pravac!')
    exit()

E = df['E [GPa]'].to_numpy()*math.pow(10, 6) #KPa
E = E[0]
ni = df['ni'].to_numpy()
n = ni[0]
n1 = (1-n)/2
t = df['t [m]'].to_numpy()
t = t[0]
pomeranja = df['Generalisana pomeranja'].to_numpy()
if len(pomeranja) != 6:
    print('Broj unetih generalisanih pomeranja je razlicit od 6!')
    exit()

A = np.array([[1, x_koordinate[0], y_koordinate[0]],
             [1, x_koordinate[1], y_koordinate[1]],
              [1, x_koordinate[2], y_koordinate[2]]
              ])
A = np.linalg.det(A)
A = A/2
f = (E*t)/(4*A*(1 - math.pow(n, 2)))

a1 = x_koordinate[1]*y_koordinate[2] - x_koordinate[2]*y_koordinate[0]
a2 = x_koordinate[2]*y_koordinate[0] - x_koordinate[0]*y_koordinate[2]
a3 = x_koordinate[0]*y_koordinate[1] - x_koordinate[1]*y_koordinate[0]
b1 = y_koordinate[1] - y_koordinate[2]
b2 = y_koordinate[2] - y_koordinate[0]
b3 = y_koordinate[0] - y_koordinate[1]
c1 = x_koordinate[2] - x_koordinate[1]
c2 = x_koordinate[0] - x_koordinate[2]
c3 = x_koordinate[1] - x_koordinate[0]

k11 = math.pow(b1, 2) + math.pow(c1, 2)*n1
k12 = b1*n*c1 + c1*n1*b1
k13 = b1*b2 + c1*n1*c2
k14 = b1*n*c2 + c1*n1*b2
k15 = b1*b3 + c1*n1*c3
k16 = b1*n*c3 + c1*n1*b3

k21 = k12
k22 = math.pow(c1, 2) + math.pow(b1, 2)*n1
k23 = c1*n*b2 + b1*n1*c2
k24 = c1*c2 + b1*n1*b2
k25 = c1*n*b3 + b1*n1*c3
k26 = c1*c3 + b1*n1*b3

k31 = k13
k32 = k23
k33 = math.pow(b2, 2) + math.pow(c2, 2)*n1
k34 = b2*n*c2 + c2*n1*b2
k35 = b2*b3 + c2*n1*c3
k36 = b2*n*c3 + c2*n1*b3

k41 = k14
k42 = k24
k43 = k34
k44 = math.pow(c2, 2) + math.pow(b2, 2)*n1
k45 = c2*n*b3 + b2*n1*c3
k46 = c2*c3 + b2*n1*b3

k51 = k15
k52 = k25
k53 = k35
k54 = k45
k55 = math.pow(b3, 2) + math.pow(c3, 2)*n1
k56 = b3*n*c3 + c3*n1*b3

k61 = k16
k62 = k26
k63 = k36
k64 = k46
k65 = k56
k66 = math.pow(c3, 2) + math.pow(b3, 2)*n1

K = np.array([[k11, k12, k13, k14, k15, k16],
                [k21, k22, k23, k24, k25, k26],
                [k31, k32, k33, k34, k35, k36],
                [k41, k42, k43, k44, k45, k46],
                [k51, k52, k53, k54, k55, k56],
                [k61, k62, k63, k64, k65, k66]
                ])

dfk = pd.DataFrame(K, columns=pomeranja)
dfk[''] = pomeranja
dfk.to_csv('K_CST.csv', index=False)
