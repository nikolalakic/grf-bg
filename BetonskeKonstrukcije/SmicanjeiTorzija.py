import numpy as np
import pandas as pd
import math, os

def Geometrija(b, h, d1):
#Smicanje
    if VEd != 0:
        As1 = float(input('Unesi povrsinu poduzne armature od savijanja As1 u preseku ili rebru [cm^2]: '))
        ro = As1/(b*d*10000)
        if ro > 0.02:
            print('\u03C1 > 2%, usvaja se da je \u03C1 = 2% !')
            ro = 0.02
    else:
        As1 = 0
        ro = 0
    K = 1 + math.pow(200/(d*1000), 0.5)
    if K > 2:
        K=2
    ni1 = 0.6*(1-fckMPA/250)
    if fckMPA > 60:
        ni1 = max(0.9- fckMPA/200, 0.5)
    VRdMax = b*0.9*d*fcd*ni1*1000/2
    VMin = 0.035*(math.pow(fckMPA, 0.5))*(math.pow(K, 1.5))*b*d*1000
    VRDc = 0.12*K*math.pow(ro*100*fckMPA, 1/3)*b*d*1000
    if VRDc < VMin:
        VRDc = VMin
    rowmin = 0.08*math.sqrt(fckMPA)/500
    m2 = 2
    m4 = 4
    fi8 = fi_lista[0]/10
    fi10 = fi_lista[1]/10
    fi12 = fi_lista[2]/10
#Torzija
    tef = max(b*h/(2*(b+h)), 2*d1)
    bk = h -2*tef/2
    hk = b -2*tef/2
    Ak = hk*bk
    uk = 2*(bk+hk)
    TcRd = fctd*2*Ak*tef*1000
    TRdMAX = 2*0.6*(1-fckMPA/250)*fcd*Ak*0.5*tef
    a = np.array([VRDc, VRdMax, TcRd, TRdMAX, Ak, uk, rowmin, ro, As1, tef])
    return a

def maxrastV(VEd, VRDc, m2, fi8, rowmin, VRdMax):
    if VEd !=0 and TEd == 0:
        if VEd <= VRDc:
            s = round(m2*0.503/(rowmin*b*100), 1)
            rpop = min(0.75*d*100, 60)
        elif VEd <= 0.3*VRdMax:
            if fckMPA <= 50:
                s = min(0.75*d*100, 30)
                rpop = min(0.75*d*100, 60)
            elif fckMPA > 50:
                s = min(0.75*d*100, 20)
                rpop = min(0.75*d*100, 40)
        elif VEd >= 0.3*VRdMax and VEd <= 0.6*VRdMax:
            if fckMPA <= 50:
                s = min(0.55*d*100, 30)
                rpop = min(0.75*d*100, 60)
            elif fckMPA > 50:
                s = min(0.55*d*100, 20)
                rpop = min(0.75*d*100, 40)
        elif VEd > 0.6*VRdMax:
                s = min(0.3*d*100, 20)
                rpop = min(0.3*d*100, 30)
        print('\nMaksimalni poduzni razmak uzengija je: ','\u03A6' + str(int(fi8)), 'na', s,'[cm]')
        print('Maksimalno poprecno rastojanje nozica uzengija je: ', round(rpop, 1), '[cm]')
        print('\nSracunati dodatnu zategnutu armaturu kod oslonca!')

def maxrastT(TEd, TcRd, m2, fi8, rowmin, TRdMAX):
   if VEd ==0 and TEd != 0:
       if TEd <= 0.3*TRdMAX:
           if fckMPA <= 50:
               s = min(0.75*d*100, 30)
               rpop = min(0.75*d*100, 60)
           elif fckMPA > 50:
               s = min(0.75*d*100, 20)
               rpop = min(0.75*d*100, 40)
       elif TEd >= 0.3*TRdMAX and TEd <= 0.6*TRdMAX:
           if fckMPA <= 50:
               s = min(0.55*d*100, 30)
               rpop = min(0.75*d*100, 60)
           elif fckMPA > 50:
               s = min(0.55*d*100, 20)
               rpop = min(0.75*d*100, 40)
       elif TEd > 0.6*TRdMAX:
               s = min(0.3*d*100, 20)
               rpop = min(0.3*d*100, 30)
       print('\nMaksimalni poduzni razmak uzengija je: ','\u03A6' + str(int(fi8)), 'na', s,'[cm]')
       print('Maksimalno poprecno rastojanje nozica uzengija je: ', round(rpop, 1), '[cm]')

def maxrastVT(TEd, TcRd, m2, fi8, rowmin, TRdMAX, VEd, VRDc, VRdMax):
    if VEd !=0 and TEd != 0:
        uslov = TEd/TRdMAX + VEd/VRdMax
        if uslov <= 0.3:
            if fckMPA <= 50:
                s = min(0.75*d*100, 30)
                rpop = min(0.75*d*100, 60)
            elif fckMPA > 50:
                s = min(0.75*d*100, 20)
                rpop = min(0.75*d*100, 40)
        elif uslov >= 0.3 and uslov <= 0.6:
            if fckMPA <= 50:
                s = min(0.55*d*100, 30)
                rpop = min(0.75*d*100, 60)
            elif fckMPA > 50:
                s = min(0.55*d*100, 20)
                rpop = min(0.75*d*100, 40)
        elif uslov > 0.6:
            s = min(0.3*d*100, 20)
            rpop = min(0.3*d*100, 30)
        print('\nMaksimalni poduzni razmak spoljasnjih uzengija je: ', s, '[cm]')
        print('Maksimalno poprecno rastojanje nozica uzengija je: ', round(rpop, 1), '[cm]')

def Torzija(TEd):
    TcRd = podacigeometrija[2]
    TRdMAX = podacigeometrija[3]*1000
    Ak = podacigeometrija[4]
    uk =  podacigeometrija[5]
    tef = podacigeometrija[9]
    rowmin = podacigeometrija[6]
    Asl = TEd/(2*Ak*fyd*1000)*uk*math.pow(10, 4)
    m2 = m_niz[0]
    m4 = m_niz[1] 
    fi8 = fi_lista[0]
    odnosTEd = TEd/(2*Ak*fyd*1000)
    odnosTmin = rowmin*b
    if TEd > TRdMAX:
        print('\n>>>>>Prekoracen maksimalni napon u betonu! TRd, max = ', TRdMAX, '[KNm]')
    elif TEd <= TcRd: 
        print('\nMinimalni procenat armiranja!')
        for x in A_lista:
            s = x/odnosTmin
            if s >= 0.075:
                print(str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'na', s*100, '[cm]', '.....OK!' )
                break
            else:
                print(str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'je ispod 7.5 cm!' )
        print('Ukupna povrsina poduzne armature: Asl = ', Asl, '[cm^2]')
    elif TEd > TcRd and TEd <= TRdMAX:
        print('\n>>>>>Potrebna je racunska poprecna i poduzna armatura!')
        for x in A_lista:
            s = x/odnosTEd
            if s >= 0.075:
                print('Secnost je m = 2;',str(round(x*math.pow(10, 4), 3)),'[cm^2]', 'na', s*100, '[cm]', '.....OK!' )
                break
            else:
                print(str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'je ispod 7.5 cm!' )
        print('Povrsina poduzne armature od torzije je: Asl = ', Asl, '[cm^2]')
        maxrastT(TEd, TcRd, 1 , 8, rowmin, TRdMAX)

def Smicanje(VEd):
    VRDc = podacigeometrija[0]
    VRdMax = podacigeometrija[1]
    m2 = m_niz[0]
    m4 = m_niz[1] 
    fi8 = fi_lista[0]
    fi10 = fi_lista[1] 
    fi12 = fi_lista[2] 
    rowmin = podacigeometrija[6]
    ro = podacigeometrija[7]
    print('Za smicanje je pretpostavka da je \u03B1 = 45\N{DEGREE SIGN} i \u03B8 = 90\N{DEGREE SIGN}') 
    if VEd/VRdMax > 1:
        print('\n>>>>>Prekoracen maksimalni dozvoljeni napon u betonu!')
        print('VEd = ', VEd, '[KN]')
        print('VRdMax = ', VRdMax, '[KN]')
    elif VEd/VRDc <= 1:
        s = m2*fi8/(rowmin*b*100)
        print('\nMinimalni procenat armiranja!')
        maxrastV(VEd, VRDc, m2, fi8, rowmin, VRdMax)
        print('VRd,c = ', VRDc, '[KN]')
    elif VEd/VRDc > 1 and VEd <= VRdMax:
        print('\n>>>>>Potrebna je armatura za smicanje!')
        print('\nPotrebni razmaci za odredjenu secnost:\n')
        if b >= 0.25:
            for m in m_niz:
                for x in A_lista:
                    s = (m*x/(VEd)*ceta*d*fyd*1000)
                    if s >= 0.075:
                        print('Secnost = ', m, '; ' + str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'na', s*100, '[cm]', '.....OK!' )
                    else:
                        print('Secnost = ', m, 'za ' + str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'je ispod 7.5 [cm]!','.....Nedovoljno!')
        elif b < 0.25:
            m = 2
            for x in A_lista:
                s = (m*x/(VEd)*ceta*d*fyd*1000)
                if s >= 0.075:
                    print('Secnost = ', m, '; ' + str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'na', s*100, '[cm]', '.....OK!' )
                    break
                else:
                    print('Secnost = ', m, 'za ' + str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'je ispod 7.5 [cm]!','.....Nedovoljno!')
        maxrastV(VEd, VRDc, m2, fi8, rowmin, VRdMax)

def Kombinacija(VEd, TEd):
    VRDc = podacigeometrija[0]
    VRdMax = podacigeometrija[1]
    m2 = m_niz[0]
    m4 = m_niz[1] 
    fi8 = fi_lista[0]
    fi10 = fi_lista[1] 
    fi12 = fi_lista[2] 
    rowmin = podacigeometrija[6]
    ro = podacigeometrija[7]
    TcRd = podacigeometrija[2]
    TRdMAX = podacigeometrija[3]*1000
    Ak = podacigeometrija[4]
    uk =  podacigeometrija[5]
    tef = podacigeometrija[9]
    odnosTEd = TEd/(2*Ak*fyd*1000)
    odnosTmin = rowmin*b
    odnosVEd = VEd/(ceta*d*fyd*1000*4)
    Asl = TEd/(2*Ak*fyd*1000)*uk*math.pow(10, 4)
    if (VEd/VRDc + TEd/TcRd)  <= 1:
        print('\n>>>>>Minimalni procenat armiranja!')
        m = 2
        odnosVmin = (1/m)*rowmin*b
        for x in A_lista:
            sv = x/odnosVmin
            st = x/odnosTmin
            s = sv + st
            if s >= 0.075:
                print('Secnost = ', m, '; ' + str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'na', s*100, '[cm]', '.....OK!' )
            else:
                print('Secnost = ', m, '; ' + str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'je ispod 7.5 cm!' )
    if (VEd/VRDc + TEd/TcRd) > 1 and (VEd/VRdMax + TEd/TRdMAX) <= 1:
        print('\n>>>>>Potrebna je proracunska armatura za kombinaciju smicanja i torzije!')
    else:
        print('\nPrekoracena dozvoljena sila u pritisnutoj betonskoj dijagonali!')
        print('VEd/VRdMax + TEd/TRdMAX = ',VEd/VRdMax + TEd/TRdMAX)
        exit()
    if (VEd/VRDc) < 0.05:
        Torzija(TEd)
    elif (TEd/TcRd) < 0.05:
        Smicanje(VEd)
    else:
        print('\nPotrebni razmaci za odredjenu povrsinu sipke, secnost za smicanje je 4! ')
        for x in A_lista:
            ukupno = odnosVEd + odnosTEd
            sv = x/odnosVEd
            s = x/ukupno
            print('\nSpoljasnje uzengije: ', str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'na', s*100, '[cm]')
            print('Unutrasnje uzengije: ', str((round(x*math.pow(10, 4), 3))),'[cm^2]', 'na', sv*100, '[cm]')
        print('\nPotrebna poduzna armatura za prihvatanje torzije je: ', Asl,'[cm^2]')
        maxrastVT(TEd, TcRd, m2, fi8, rowmin, TRdMAX, VEd, VRDc, VRdMax)

VEd = abs(float(input('Unesi proracunsku silu smicanja VEd [KN]: ')))
TEd = abs(float(input('Unesi proracunsku silu torzije TEd [KNm]: ')))
fckMPA = int(input('Unesi karakteristicnu cvrstocu betona fck [MPa]: '))
b = float(input('Unesi sirinu rebra b [cm]: '))
b = b/100
h = float(input('Unesi visinu preseka h [cm]: '))
h = h/100
d1 = float(input('Unesi rastojanje od zategnute ivice do tezista armature d1 [cm]: '))
d1 = d1/100
d = h - d1

if 'BetonPodaci.csv' not in os.listdir():
    print('BetonPodaci.csv se ne nalazi u radnom folderu!')
    exit()
else:
    df = pd.read_csv('BetonPodaci.csv', delimiter = ';', encoding = 'UTF-8', skipinitialspace = True)
    fck_lista = df['fck [Mpa]'].to_list()
    fctm_lista = df['fctm [Mpa]'].to_numpy()
    Ecm_lista = df['Ecm [Gpa]'].to_numpy()
    fctk005_lista = df['fctk005 [Mpa]'].to_numpy()
    fi_lista = df['fi [mm]'].to_numpy()
    fi_lista = fi_lista[1:4]
    A_lista = df['A [cm2]']
    A_lista = A_lista[1:4]*math.pow(10, -4)
m_niz = [2, 4] 
if fckMPA in fck_lista:
    indeks = fck_lista.index(fckMPA)
    fctm = fctm_lista[indeks]
    Ecm = Ecm_lista[indeks]
    ceta = 0.9
    if ceta >= 0.9:
        ceta = 0.9
    fcd = 0.85*fckMPA/1.5
    fyd = 500/1.15
    fctk005 = fctk005_lista[indeks]
    fctd = fctk005/1.5
else:
    print(f'{fckMPA} nije standardna karakteristicna cvrstoca betona!')
    exit()

if TEd == 0 and VEd != 0:
    podacigeometrija = Geometrija(b, h ,d1)
    Smicanje(VEd)

if VEd == 0 and TEd != 0:
    podacigeometrija = Geometrija(b, h, d1)
    Torzija(TEd)

if VEd != 0 and TEd != 0:
    podacigeometrija = Geometrija(b, h, d1)
    Kombinacija(VEd, TEd)
