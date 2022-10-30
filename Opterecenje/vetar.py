import math
import numpy as np

vb0 = float(input('Unesi osnovnu brzinu vetra vb,0 [m/s]: '))
K = 0.2
n = 0.5
p = 0.02 # povratni period vetra je 50 godina
cprob = math.pow((1 - K*np.log(-np.log(1 - p)))/(1 - K*np.log(-np.log(0.98))), n)
vb = vb0*cprob
Cdir = 1
Cseason = 1
z0_niz = np.array([0.003, 0.01, 0.05, 0.3, 1])
zmin_niz = np.array([1, 1, 2, 5, 10])
kr_niz = np.array([0.156, 0.17, 0.19, 0.215, 0.234])
cr_niz = np.array([0.906, 0.782, 0.701, 0.606, 0.54])
ki = 1
c0 = 1

kategorija = int(input('Unesi kategoriju terena (0, 1, 2, 3, 4): '))

z0 = z0_niz[kategorija]
zmin = zmin_niz[kategorija]
kr = kr_niz[kategorija]
cr_zmin = cr_niz[kategorija]

z = float(input('Unesi visinu objekta z [m]: '))
if z > 200:
    z = 200
    print('Uzeta je vrednost z = 200 [m]!')
if z < 0:
    print('z mora biti vece od 0!')
    exit()

if zmin < z and z <=200:
    cr = kr*np.log(z/z0)
else:
    cr = kr*np.log(zmin/z0)
vm = cr*c0*vb

if zmin < z and z <=200:
    Iv = ki/(c0*np.log(z/z0))
else:
    Iv = ki/(c0*np.log(zmin/z0))

qb = 1/2*1.25*math.pow(vb, 2)/1000
qp = (1 + 7*Iv)*0.5*1.25*math.pow(vm, 2)/1000

print('\nSrednja brzina vetra: vm =  ', vm, '[m/s]')
print('Osnovni pritisak vetra: qb = ',qb,'[kN/m^2]')
print('Udarni pritisak vetra: qp = ',qp,'[kN/m^2]')
