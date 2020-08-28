import pandas as pd
import numpy as np
import sympy as sp
import math, os

x, y = sp.symbols('x y')
w_xy_niz_sym = np.array([1, x, y, sp.Pow(x, 2), x*y, sp.Pow(y, 2), sp.Pow(x, 3), sp.Pow(x, 2)*y, x*sp.Pow(y, 2), sp.Pow(y, 3), sp.Pow(x, 3)*y, x*sp.Pow(y, 3)])
w_xy_sym = sum(w_xy_niz_sym)
fi_x_sym = sp.diff(w_xy_sym, y)
fi_y_sym = sp.diff(-w_xy_sym, x)

if 'Q4SavijanjePodaci.csv' not in os.listdir():
 print('Fali fajl pod nazivom "Q4SavijanjePodaci.csv", ako je obrisan skini ga sa riznice https://github.com/nikolalakic/grf-bg/tree/master/MKE')
 exit()
df = pd.read_csv('Q4SavijanjePodaci.csv', delimiter=',', encoding='UTF-8', skipinitialspace=True)
x_koordinate = df['x [m]'].to_numpy()
y_koordinate = df['y [m]'].to_numpy()
a_dimenzija = df['a [m]'].to_numpy()
b_dimenzija = df['b [m]'].to_numpy()
E_lista = df['E [Gpa]'].to_numpy()*math.pow(10, 6) #KPa
ni_lista = df['ni'].to_numpy()
t_lista = df['t [m]'].to_numpy()
p_lista = df['q [kN/m^2]'].to_numpy()
nepoznata_pomeranja = df['Nepoznata pomeranja (sva)'].to_numpy()
nepoznata_pomeranja = nepoznata_pomeranja[np.logical_not(np.isnan(nepoznata_pomeranja))]
p = (p_lista[0])
t = (t_lista[0])
ni = (ni_lista[0])
a = (a_dimenzija[0])
b = (b_dimenzija[0])
E = (E_lista[0])
Ex = E*math.pow(t, 3)/(12*(1-math.pow(ni, 2)))
Ey = Ex
Exy = Ex*(1-ni)/2
E1 = ni*Ex

k1_1 = 2/5*(10*Ex*math.pow(b, 4) + 14*math.pow(a*b, 2)*Exy + 5*math.pow(a*b, 2)*E1 + 10*Ey*math.pow(a, 4))/math.pow(a, 3)/math.pow(b, 3)
k2_1 = 1/5/a*(5*E1*math.pow(b, 2) + 2*math.pow(b, 2)*Exy + 10*Ey*math.pow(a, 2))/math.pow(b, 2)
k3_1 = -1/5*(10*Ex*math.pow(b, 2) + 5*E1*math.pow(a, 2) + 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k4_1 = -2/5*(10*Ex*math.pow(b, 4) + 14*math.pow(a*b, 2)*Exy + 5*math.pow(a*b, 2)*E1 - 5*Ey*math.pow(a, 4))/(math.pow(a*b, 3))
k5_1 = -1/5/a*(5*E1*math.pow(b, 2) + 2*math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/math.pow(b, 2)
k6_1 = -2/5*(5*Ex*math.pow(b, 2) + math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k7_1 = -2/5*(5*Ex*math.pow(b, 4) - 14*math.pow(a*b, 2)*Exy - 5*math.pow(a*b, 2)*E1 + 5*Ey*math.pow(a, 4))/(math.pow(a, 3))/math.pow(b, 3)
k8_1 = -1/5*(2*Exy*math.pow(b, 2) - 5*Ey*math.pow(a, 2))/a/math.pow(b, 2)
k9_1 = -1/5*(5*Ex*math.pow(b, 2) - 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k10_1 = 2/5*(5*Ex*math.pow(b, 4) - 14*math.pow(a*b, 2)*Exy - 5*math.pow(a*b, 2)*E1 - 10*Ey*math.pow(a, 4))/math.pow(a*b, 3)
k11_1 = 2/5*(math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/math.pow(b, 2)
k12_1 = -1/5*(5*Ex*math.pow(b, 2) - 5*E1*math.pow(a, 2) - 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b

k1_2 = k2_1
k2_2 = 4/15*(2*math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/b
k3_2 = -E1
k4_2 = -1/5/a*(5*E1*math.pow(b, 2) + 2*math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/math.pow(b, 2)
k5_2 = -2/15*(4*math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/a/b
k6_2 = 0
k7_2 = 1/5*(2*math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/a/math.pow(b, 2)
k8_2 = 1/15*(2*math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/b
k9_2 = 0
k10_2 = -2/5*(math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/math.pow(b, 2)
k11_2 = -2/15*(math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/a/b
k12_2 = 0

k1_3 = k3_1
k2_3 = k3_2
k3_3 = 4/15*(5*Ex*math.pow(b, 2) + 2*math.pow(a, 2)*Exy)/a/b
k4_3 = 2/5*(5*Ex*math.pow(b, 2) + math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k5_3 = 0
k6_3 = 2/15*(5*Ex*math.pow(b, 2) - math.pow(a, 2)*Exy)/a/b
k7_3 = 1/5*(5*Ex*math.pow(b, 2) - 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k8_3 = 0
k9_3 = 1/15*(5*Ex*math.pow(b, 2) + 2*math.pow(a, 2)*Exy)/a/b
k10_3 = -1/5*(5*Ex*math.pow(b, 2) - 5*E1*math.pow(a, 2) - 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k11_3 = 0
k12_3 = 2/15*(5*Ex*math.pow(b, 2) - 4*math.pow(a, 2)*Exy)/a/b

k1_4 = k4_1
k2_4 = k4_2
k3_4 = k4_3
k4_4 = 2/5*(10*Ex*math.pow(b, 4) + 14*math.pow(a*b, 2)*Exy + 5*math.pow(a*b, 2)*E1 + 10*Ey*math.pow(a, 4))/math.pow(a*b, 3)
k5_4 = 1/5/a*(5*E1*math.pow(b, 2) + 2*math.pow(b, 2)*Exy + 10*Ey*math.pow(a, 2))/math.pow(b, 2)
k6_4 = 1/5*(10*Ex*math.pow(b, 2) + 5*E1*math.pow(a, 2) + 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k7_4 = 2/5*(5*Ex*math.pow(b, 4) - 14*math.pow(a*b, 2)*Exy - 5*math.pow(a*b, 2)*E1 - 10*Ey*math.pow(a, 4))/math.pow(a*b, 3)
k8_4 = 2/5*(math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/math.pow(b, 2)
k9_4 = 1/5*(5*Ex*math.pow(b, 2) - 5*E1*math.pow(a, 2) - 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k10_4 = -2/5*(5*Ex*math.pow(b, 4) - 14*math.pow(a*b, 2)*Exy - 5*math.pow(a*b, 2)*E1 + 5*Ey*math.pow(a, 4))/math.pow(a*b, 3)
k11_4 = -1/5*(2*math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/a/math.pow(b, 2)
k12_4 = 1/5*(5*Ex*math.pow(b, 2) - 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b

k1_5 = k5_1
k2_5 = k5_2
k3_5 = k5_3
k4_5 = k5_4
k5_5 = 4/15*(2*math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/b
k6_5 = E1
k7_5 = -2/5*(math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/math.pow(b, 2)
k8_5 = -2/15*(math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/a/b
k9_5 = 0
k10_5 = 1/5*(2*math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/a/math.pow(b, 2)
k11_5 = 1/15*(2*math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/b
k12_5 = 0

k1_6 = k6_1
k2_6 = k6_2
k3_6 = k6_3
k4_6 = k6_4
k5_6 = k6_5
k6_6 = 4/15*(5*Ex*math.pow(b, 2) + 2*math.pow(a, 2)*Exy)/a/b
k7_6 = 1/5*(5*Ex*math.pow(b, 2) - 5*E1*math.pow(a, 2) - 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k8_6 = 0
k9_6 = 2/15*(5*Ex*math.pow(b, 2) - 4*math.pow(a, 2)*Exy)/a/b
k10_6 = -1/5*(5*Ex*math.pow(b, 2) - 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k11_6 = 0
k12_6 = 1/15*(5*Ex*math.pow(b, 2) + 2*math.pow(a, 2)*Exy)/a/b

k1_7 = k7_1
k2_7 = k7_2
k3_7 = k7_3
k4_7 = k7_4
k5_7 = k7_5
k6_7 = k7_6
k7_7 = 2/5*(10*Ex*math.pow(b, 4) + 14*math.pow(a*b, 2)*Exy + 5*math.pow(a*b, 2)*E1 + 10*Ey*math.pow(a, 4))/math.pow(a*b, 3)
k8_7 = -1/5/a*(5*E1*math.pow(b, 2) + 2*math.pow(b, 2)*Exy + 10*Ey*math.pow(a, 2))/math.pow(b, 2)
k9_7 = 1/5*(10*Ex*math.pow(b, 2) + 5*E1*math.pow(a, 2) + 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k10_7 = -2/5*(10*Ex*math.pow(b, 4) + 14*math.pow(a*b, 2)*Exy + 5*math.pow(a*b, 2)*E1 - 5*Ey*math.pow(a, 4))/math.pow(a*b, 3)
k11_7 = 1/5/a*(5*E1*math.pow(b, 2) + 2*math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/math.pow(b, 2)
k12_7 = 2/5*(5*Ex*math.pow(b, 2) + math.pow(a, 2)*Exy)/math.pow(a, 2)/b

k1_8 = k8_1
k2_8 = k8_2
k3_8 = k8_3
k4_8 = k8_4
k5_8 = k8_5
k6_8 = k8_6
k7_8 = k8_7
k8_8 = 4/15*(2*math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/b
k9_8 = -E1
k10_8 = 1/5/a*(5*E1*math.pow(b, 2) + 2*math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/math.pow(b, 2)
k11_8 = -2/15*(4*math.pow(b, 2)*Exy - 5*Ey*math.pow(a, 2))/a/b
k12_8 = 0

k1_9 = k9_1
k2_9 = k9_2
k3_9 = k9_3
k4_9 = k9_4
k5_9 = k9_5
k6_9 = k9_6
k7_9 = k9_7
k8_9 = k9_8
k9_9 = 4/15*(5*Ex*math.pow(b, 2) + 2*math.pow(a, 2)*Exy)/a/b
k10_9 = -2/5*(5*Ex*math.pow(b, 2) + math.pow(a, 2)*Exy)/math.pow(a, 2)/b
k11_9 = 0
k12_9 = 2/15*(5*Ex*math.pow(b, 2) - math.pow(a, 2)*Exy)/a/b

k1_10 = k10_1
k2_10 = k10_2
k3_10 = k10_3
k4_10 = k10_4
k5_10 = k10_5
k6_10 = k10_6
k7_10 = k10_7
k8_10 = k10_8
k9_10 = k10_9
k10_10 = 2/5*(10*Ex*math.pow(b, 4) + 14*math.pow(a*b, 2)*Exy + 5*math.pow(a*b, 2)*E1 + 10*Ey*math.pow(a, 4))/math.pow(a*b, 3)
k11_10 = -1/5/a*(5*E1*math.pow(b, 2) + 2*math.pow(b, 2)*Exy + 10*Ey*math.pow(a, 2))/math.pow(b, 2)
k12_10 = -1/5*(10*Ex*math.pow(b, 2) + +5*E1*math.pow(a, 2) + 2*math.pow(a, 2)*Exy)/math.pow(a, 2)/b

k1_11 = k11_1
k2_11 = k11_2
k3_11 = k11_3
k4_11 = k11_4
k5_11 = k11_5
k6_11 = k11_6
k7_11 = k11_7
k8_11 = k11_8
k9_11 = k11_9
k10_11 = k11_10
k11_11 = 4/15*(2*math.pow(b, 2)*Exy + 5*Ey*math.pow(a, 2))/a/b
k12_11 = E1

k1_12 = k12_1
k2_12 = k12_2
k3_12 = k12_3
k4_12 = k12_4
k5_12 = k12_5
k6_12 = k12_6
k7_12 = k12_7
k8_12 = k12_8
k9_12 = k12_9
k10_12 = k12_10
k11_12 = k12_11
k12_12 = 4/15*(5*Ex*math.pow(b, 2) + 2*math.pow(a, 2)*Exy)/a/b

K = np.array([
 [k1_1, k1_2, k1_3, k1_4, k1_5, k1_6, k1_7,  k1_8, k1_9, k1_10, k1_11, k1_12],
 [k2_1, k2_2, k2_3, k2_4, k2_5, k2_6, k2_7, k2_8, k2_9, k2_10, k2_11, k2_12],
 [k3_1, k3_2, k3_3, k3_4, k3_5, k3_6, k3_7, k3_8, k3_9, k3_10, k3_11, k3_12],
 [k4_1, k4_2, k4_3, k4_4, k4_5, k4_6, k4_7, k4_8, k4_9, k4_10, k4_11, k4_12],
 [k5_1, k5_2, k5_3, k5_4, k5_5, k5_6, k5_7, k5_8, k5_9, k5_10, k5_11, k5_12],
 [k6_1, k6_2, k6_3, k6_4, k6_5, k6_6, k6_7, k6_8, k6_9, k6_10, k6_11, k6_12],
 [k7_1, k7_2, k7_3, k7_4, k7_5, k7_6, k7_7, k7_8, k7_9, k7_10, k7_11, k7_12],
 [k8_1, k8_2, k8_3, k8_4, k8_5, k8_6, k8_7, k8_8, k8_9, k8_10, k8_11, k8_12],
 [k9_1, k9_2, k9_3, k9_4, k9_5, k9_6, k9_7, k9_8, k9_9, k9_10, k9_11, k9_12],
 [k10_1, k10_2, k10_3, k10_4, k10_5, k10_6, k10_7, k10_8, k10_9, k10_10, k10_11, k10_12],
 [k11_1, k11_2, k11_3, k11_4, k11_5, k11_6, k11_7, k11_8, k11_9, k11_10, k11_11, k11_12],
 [k12_1, k12_2, k12_3, k12_4, k12_5, k12_6, k12_7, k12_8, k12_9, k12_10, k12_11, k12_12]
])

C = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, a, 0, math.pow(a, 2), 0, 0, math.pow(a, 3), 0, 0, 0, 0, 0],
              [0, 0, 1, 0, a, 0, 0, math.pow(a, 2), 0, 0, math.pow(a, 3), 0],
              [0, -1, 0, -2*a, 0, 0, -3*math.pow(a, 2), 0, 0, 0, 0, 0],
              [1, a, b, math.pow(a, 2), a*b, math.pow(b, 2), math.pow(a, 3), math.pow(a, 2)*b, a*math.pow(b, 2), math.pow(b, 3), math.pow(a, 3)*b, a*math.pow(b, 3)],
              [0, 0, 1, 0, a, 2*b, 0, math.pow(a, 2), 2*a*b, 3*math.pow(b, 2), math.pow(a, 3), 3*a*math.pow(b, 2)],
              [0, -1, 0, -2*a, -b, 0, -3*math.pow(a, 2), -2*a*b, -math.pow(b, 2), 0, -3*math.pow(a, 2)*b, -math.pow(b, 3)],
              [1, 0, b, 0, 0, math.pow(b, 2), 0, 0, 0, math.pow(b, 3), 0, 0],
              [0, 0, 1, 0, 0, 2*b, 0, 0, 0, 3*math.pow(b, 2), 0, 0],
              [0, -1, 0, 0, -b, 0, 0, 0, -math.pow(b, 2), 0, 0, -math.pow(b, 3)]],
             )
C_inv = np.linalg.inv(C)

p1 = 1/4*a*b
p2 = 1/24*a*math.pow(b, 2)
p3 = -1/24*math.pow(a, 2)*b
p4 = 1/4*a*b
p5 = 1/24*a*math.pow(b, 2)
p6 = 1/24*math.pow(a, 2)*b
p7 = 1/4*a*b
p8 = -1/24*a*math.pow(b, 2)
p9 = 1/24*math.pow(a, 2)*b
p10 = 1/4*a*b
p11 = -1/24*a*math.pow(b, 2)
p12 = -1/24*math.pow(a, 2)*b

P = p*np.array([[p1],
              [p2],
              [p3],
              [p4],
              [p5],
              [p6],
              [p7],
              [p8],
              [p9],
              [p10],
              [p11],
              [p12]
              ])
pomeranja = df['Generalisana pomeranja'].to_numpy()
if len(pomeranja) != 12:
 print('\nUkupan broj unetih pomeranja je razlicit od 12! Greska u unosu u Podaci.csv fajlu!')
 exit()

dfk = pd.DataFrame(K, columns=pomeranja)
dfk[''] = pomeranja
dfk['P'] = P
dfk.to_csv('Q4_K_matrica.csv', index=False)
indeksi = np.arange(0, len(nepoznata_pomeranja))
if 'K_nn.csv' in os.listdir():
    dfknn = pd.read_csv('Q4Knn.csv', skipinitialspace=True)
    Knn = dfknn.to_numpy()
    dfpn = pd.read_csv('Q4Pnn.csv', delimiter=',')
    Pn = dfpn['Pn'].to_numpy()
    inv_Knn = np.linalg.inv(Knn)
    qnn = np.dot(inv_Knn, Pn)
    dfqnn = pd.DataFrame(qnn)
    dfqnn[''] = nepoznata_pomeranja
    dfqnn.to_csv('Q4qnn.csv', header=['qnn [m]',''], index=False)
    #if 'qnn.csv' in os.listdir():
    #    os.remove('qnn.csv')
    #with open('qnn.csv', 'a') as file:
    #    file.write(f'qnn [m]\n')
    #    dfqnn.to_csv(file, header=False, index=False)
#else:
# pass
