import numpy as np
import pandas as pd
import math, gc

gc.disable()

fy = int(input('Unesi granicu razvlacenja celika fy [MPa]: '))
epsilon = math.sqrt(235/fy)
E = 210*math.pow(10, 6) #KPa
#TODO unesi niz i za fu
def Sile():
    global NEd, MEd
    NEd = float(input('Unesi aksijalnu silu NEd [kN], (pritisak je pozitivan): '))
    MEd = float(input('Unesi momenat savijanja MEd [kNm], momenat pritiska ivicu 1 a zateze ivicu 2: '))
Sile()
profil = str(input('Unesi ime profila (npr ipe 300, ipn400), ukoliko je profil zavaren kucaj "zavaren": ')).upper()
profil = profil.replace(' ','')
if profil == 'ZAVAREN':
    h = float(input('Unesi visinu profila h [mm]: '))
    h = h/1000 # [m]
    tw = float(input('Unesi debljinu rebra tw [mm]: '))
    tw = 8
    tw = tw/1000
    b1 = float(input('Unesi sirinu pritisnute (gornje) nozice b1 [mm]: '))
    b1 = 300
    b1 = b1/1000 # [m]
    tf1 = float(input('Unesi debljinu pritisnute (gornje) nozice tf1 [mm]: '))
    tf1 = 10
    tf1 = tf1/1000
    b2 = float(input('Unesi sirinu zategnute (donje) nozice b2 [mm]: '))
    b2 = 300
    b2 = b2/1000 # [m]
    tf2 = float(input('Unesi debljinu zategnute (donje) nozice tf2 [mm]: '))
    tf2 = 10 
    tf2 = tf2/1000
    aw = float(input('Unesi debljinu vara a [mm]: '))
    aw = 4
    aw = aw/1000
    #Geometrijiske karakteristike
    cf1 = (b1 - 2*aw*math.sqrt(2)-tw)/2
    cf2 = (b2 - 2*aw*math.sqrt(2)-tw)/2
    cw = h - tf1 - tf2 - 2*aw*math.sqrt(2)
    d = h-tf1-tf2
    Af1 = tf1*b1
    Af2 = tf2*b2
    Aw = tw*d
    A = Af1 + Af2 + Aw
    zt1 = ((Af1*tf1/2) + Aw*(d/2+tf1) + Af2*(tf2/2+d+tf1))/A
    #def teziztebruto():
    #    zt1 = ((Af1*tf1/2) + Aw*(d/2+tf1) + Af2*(tf2/2+d+tf1))/A
    #    return zt1
    zt2 = h - zt1
    Iy = b1*math.pow(tf1, 3)/12 + Af1*math.pow(zt1 - tf1/2, 2) + tw*math.pow(d, 3)/12 + Aw*math.pow(h/2-zt1,2) + b2*math.pow(tf2, 3)/12 + Af2*math.pow(zt2-tf2/2,2)
    Iz = tf1*math.pow(b1, 3)/12 + tf2*math.pow(b2, 3)/12 + (h-tf1-tf2)*math.pow(tw, 3)
    iy = math.sqrt(Iy/A)
    iz = math.sqrt(Iz/A)
    alfa = ((Af2 - Af1 + Aw)/(2*tw))/d
    Avz = (h-tf1-tf2)*tw
    Wely = Iy/(max(zt1, zt2))
    Welz = Iz/(max(b1, b2)/2)
    It = 1/3*(b1*math.pow(tf1, 3) + b2*math.pow(tf2, 3) + (h-tf1-tf2)*math.pow(tw, 3))
    def povrsina():
        A = Af1 + Af2 + Aw
        return A
else:
    df = pd.read_csv('VruceValjani.csv', delimiter=',', skipinitialspace = True, encoding = 'UTF-8')
    lista_profila = df['Profil'].to_list()
    if profil in lista_profila:
        indeks = lista_profila.index(profil)
        #Geometrija
        h_niz = df['h [mm]'].to_numpy()*math.pow(10, -3) # [m]
        h = h_niz[indeks]
        b_niz = df['b [mm]'].to_numpy()*math.pow(10, -3) # [m]
        b = b_niz[indeks]
        b1 = b
        b2 = b
        tw_niz = df['tw [mm]'].to_numpy()*math.pow(10, -3) # [m]
        tw = tw_niz[indeks]
        tf_niz = df['tf [mm]'].to_numpy()*math.pow(10, -3) # [m]
        tf = tf_niz[indeks]
        tf1 = tf
        tf2 = tf
        r1_niz = df['r1 [mm]'].to_numpy()*math.pow(10, -3) # [m]
        r1 = r1_niz[indeks]
        r2_niz = df['r2 [mm]'].to_numpy()*math.pow(10, -3) # [m]
        r2 = r2_niz[indeks]
        #>>>>>>>Nesto nije u redu, u ulasku u funckiju AksijalnaNosivostBrutoNeto A ne postoji a trebalo bi jer je globalna promenljiva, sve ostale vrednosti postoje
        def povrsina():
            A_niz = df['A [mm^2]'].to_numpy()*math.pow(10, -4) # [m^2]
            A = A_niz[indeks]
            return A
        hi_niz = df['hi [mm]'].to_numpy()*math.pow(10, -3) # [m]
        hi = hi_niz[indeks]
        #Geometrjiske karakteristike
        Iy_niz = df['Iy [mm^4]'].to_numpy()*math.pow(10, -8) # [m^4]
        Iy = Iy_niz[indeks]
        Wely_niz = df['Wely [mm^3]'].to_numpy()*math.pow(10, -6) # [m^3]
        Wely = Wely_niz[indeks]
        #>>>>>>>Nesto nije u redu, u ulasku u funckiju MomentNosivosti Wply ne postoji a trebalo bi jer je globalna promenljiva, sve ostale vrednosti postoje
        def wply():
            Wply_niz = df['Wply [mm^3]'].to_numpy()*math.pow(10, -6) # [m^3]
            Wply = Wply_niz[indeks]
            return Wply
        iy_niz = df['iy [mm]'].to_numpy()*math.pow(10, -2) # [m]
        iy = iy_niz[indeks]
        Avz_niz = df['Avz [mm^2]'].to_numpy()*math.pow(10, -4) # [m^2]
        Avz = Avz_niz[indeks]
        Iz_niz = df['Iz [mm^4]'].to_numpy()*math.pow(10, -8) # [m^4]
        Iz = Iz_niz[indeks]
        Welz_niz = df['Welz [mm^3]'].to_numpy()*math.pow(10, -6) # [m^3]
        Welz = Welz_niz[indeks]
        Wplz_niz = df['Wplz [mm^3]'].to_numpy()*math.pow(10, -6) # [m^3]
        Wplz = Wplz_niz[indeks]
        iz_niz = df['iz [mm]'].to_numpy()*math.pow(10, -2) # [m]
        iz = iz_niz[indeks]
        ss_niz = df['ss [mm]'].to_numpy()*math.pow(10, -2) # [m]
        ss = ss_niz[indeks]
        It_niz = df['It [mm^4]'].to_numpy()*math.pow(10, -8) # [m^4]
        It = It_niz[indeks]
        Iw_niz = df['Iw [mm^6]'].to_numpy()*math.pow(10, -12) # [m^6]
        Iw = Iw_niz[indeks]
        cf1 = (b1 - 2*r1-tw)/2
        cf2 = (b2 - 2*r2-tw)/2
        cw = h - tf1 - tf2 - r1 - r2
        Af1 = tf1*b1
        Af2 = tf2*b2
        Aw = tw*hi
        d = hi
        zt1 = h/2
        zt2 = h/2
        alfa = ((Af2 - Af1 + Aw)/(2*tw))/hi
    else:
        print(f'\nProfil {profil} nije u listi profila! Ako postoji ovakva vrsta profila kontaktiraj Nikolu na nikola@lakic.one da je ubaci u bazu profila.')
        exit()

#Napon na ivici 1    
A = povrsina()
sigmas1 = MEd/Iy*(zt1 - tf1) + NEd/A # [kPa]
#Napon na ivici 2
sigmas2 = -MEd/Iy*(zt2 - tf2) + NEd/A # [kPa]
psi = round(sigmas2/sigmas1, 5)

def KlasaPreseka(alfa):
    if sigmas1 > 0:
    #Nozica 1 (gornja)
        if cf1/tf1 <= 9*epsilon:
            klasa_nozice_1 = 1
        elif cf1/tf1 > 9*epsilon and cf1/tf1 <= 10*epsilon:
            klasa_nozice_1 = 2
        elif cf1/tf1 > 10*epsilon and cf1/tf1 <= 14*epsilon:
            klasa_nozice_1 = 3
        elif cf1/tf1 > 14*epsilon:
            klasa_nozice_1 = 4
    else:
        klasa_nozice_1 = 1

    if sigmas2 > 0:
    #Nozica 2 (donja)
        if cf2/tf2 <= 9*epsilon:
            klasa_nozice_2 = 1
        elif cf2/tf2 > 9*epsilon and cf1/tf1 <= 10*epsilon:
            klasa_nozice_2 = 2
        elif cf2/tf2 > 10*epsilon and cf1/tf1 <= 14*epsilon:
            klasa_nozice_2 = 3
        elif cf2/tf2 > 14*epsilon:
            klasa_nozice_2 = 4
    else:
        klasa_nozice_2 = 1
    #Rebro
    if psi < 0 or (psi > 0 and sigmas2 > 0) and MEd != 0:
        if alfa > 0.5:
            if cw/tw <= (396*epsilon/(13*alfa - 1)):
                klasa_rebra = 1
            elif cw/tw > (396*epsilon/(13*alfa - 1)) and cw/tw <= 456*epsilon/(13*alfa - 1):
                klasa_rebra = 2
            elif cw/tw > (456*(epsilon)/(13*alfa - 1)):
                if psi == 1:
                    if cw/tw <= 42*epsilon:
                        klasa_rebra = 3
                    elif cw/tw > 42*epsilon:
                        klasa_rebra = 4
                if psi >= -1 and psi < 0:
                    if cw/tw <= 42*epsilon/(0.67 + 0.33*psi):
                        klasa_rebra = 3
                    elif cw/tw > 42*epsilon/(0.67 + 0.33*psi):
                        klasa_rebra = 4
        elif alfa <= 0.5:
            if cw/tw <= 36*epsilon/alfa:
                klasa_rebra = 1
            elif cw/tw > (36*epsilon/alfa) and cw/tw <= (41.5*epsilon/alfa):
                klasa_rebra = 2
            elif cw/tw > (41.5*epsilon/alfa) and cw/tw <= (62*epsilon*(1-psi)*math.sqrt(-psi)):
                    klasa_rebra = 3
            elif cw/tw > 62*epsilon*(1-psi)*math.sqrt(-psi):
                klasa_rebra = 4
    elif MEd == 0 and NEd > 0:
            if cw/tw <= 33*epsilon:
                klasa_rebra = 1
            elif cw/tw > 33*epsilon and cw/tw <= 38*epsilon:
                klasa_rebra = 2
            elif cw/tw > 38*epsilon and cw/tw <= 42*epsilon:
                    klasa_rebra = 3
            elif cw/tw > 42*epsilon:
                klasa_rebra = 4

    else:
        klasa_rebra = 1 
    klasa_preseka = max(klasa_nozice_1, klasa_nozice_2, klasa_rebra)
    a = np.array([klasa_nozice_1, klasa_nozice_2, klasa_rebra, klasa_preseka])
    return a

def EfektivniPresek():
    if klasa_nozice_1 == 4:
        ksigma = 0.426
        b_nadvuceno = (b1 - 2*aw*math.sqrt(2)-tw)/2
        lambdap = b_nadvuceno/tf1/(28.4*epsilon*math.sqrt(ksigma))
        if lambdap > 0.748:
            ro = (lambdap - 0.188)/math.pow(lambdap, 2)
            if ro > 1:
                ro = 1
            bf_eff = ro*b_nadvuceno
            beff1 = 2*bf_eff+tw+2*aw*math.sqrt(2)
        elif lambdap <= 0.748:
            beff1 = b1
        Af1 = beff1*tf1
    else:
        beff1 = b1
    Af1 = beff1*tf1

    if klasa_nozice_2 == 4:
        ksigma = 0.426
        b_nadvuceno = (b1 - 2*aw*math.sqrt(2)-tw)/2
        lambdap = b_nadvuceno/tf2/(28.4*epsilon*math.sqrt(ksigma))
        if lambdap > 0.748:
            ro = (lambdap - 0.188)/math.pow(lambdap, 2)
            if ro > 1:
                ro = 1
            bf_eff = ro*b_nadvuceno
            beff2 = 2*bf_eff+tw+2*aw*math.sqrt(2)
        elif lambdap <= 0.748:
            beff2 = b2
        Af2 = beff2*tf2
    else:
        beff2 = b2
    Af2 = beff2*tf2

    if klasa_rebra == 4:
        Aw = tw*(h - tf1 - tf2)
        A = Af1 + Af2 + Aw
        zt1 = 1/A*(Af1*tf1/2 + Aw*((h - tf1 - tf2)/2 + tf1) + Af2*(h - tf2/2))
        zt2 = h - zt1
        z1_ivica_rebra = zt1 - tf1
        z2_ivica_rebra = zt2 - tf2
        Iy = beff1*math.pow(tf1, 3)/12 + Af1*math.pow(zt1 - tf1/2, 2) + tw*math.pow(h - tf1 - tf2, 3)/12 + Aw*math.pow(h/2-zt1,2) + beff2*math.pow(tf2, 3)/12 + Af2*math.pow(zt2-tf2/2,2)
        sigma1 = MEd/Iy*z1_ivica_rebra + NEd/A
        sigma2 = -MEd/Iy*z2_ivica_rebra + NEd/A
        psi = sigma2/sigma1
        if psi == 1:
            psi2 = 1
            ksigma = 8.2/(1.05 + psi)
            b_nadvuceno = (h - tf1 - tf2 - 2*aw*math.sqrt(2)) 
            lambdap = b_nadvuceno/tw/(28.4*epsilon*math.sqrt(ksigma))
            if lambdap > 0.5 + math.sqrt(0.085-0.055*psi):
                ro = (lambdap - 0.055*(3 + psi))/math.pow(lambdap, 2)
                if ro > 1:
                    ro = 1
            elif lambdap <= 0.5 + math.sqrt(0.085-0.055*psi):
                ro = 1
            beff = ro*b_nadvuceno
            be1 = (2/(5 - psi))*b_nadvuceno
            be2 = beff - be1 + aw*math.sqrt(2)
            be1 = (2/(5 - psi))*b_nadvuceno + aw*math.sqrt(2)
            bt = 0
            bc = b_nadvuceno + 2*aw*math.sqrt(2)
            Aw = be1*tw + be2*tw + bt*tw 
            A = Aw + Af1 + Af2
            zt1 = 1/A*(Af1*tf1/2 + be1*tw*(be1/2 + tf1) + be2*tw*(bc - be2/2 + tf1) + bt*tw*(bt/2 + bc + tf1) + Af2*(h-tf2/2))
            zt2 = h - zt1
            z1_ivica_rebra = zt1 - tf1
            z2_ivica_rebra = zt2 - tf2
            Iy = beff1*math.pow(tf1, 3)/12 + Af1*math.pow(zt1 - tf1/2, 2) + tw*math.pow(be1, 3)/12 + tw*be1*math.pow(zt1 - tf1 - be1/2, 2) + tw*math.pow(bt + be2, 3)/12 + tw*(be2 + bt)*math.pow((bt + be2)/2 -zt2, 2) + beff2*math.pow(tf2, 3)/12 + Af2*math.pow(zt2-tf2/2,2)
            #MEd = MEd + (zt1 - zt1_bruto)*NEd
        else:
            while abs(psi2 - psi) > 0.001:
                psi2 = psi
                if psi <= 1 and psi >= 0:
                    ksigma = 8.2/(1.05 + psi)
                    b_nadvuceno = (h - tf1 - tf2 - 2*aw*math.sqrt(2)) 
                    lambdap = b_nadvuceno/tw/(28.4*epsilon*math.sqrt(ksigma))
                    if lambdap > 0.5 + math.sqrt(0.085-0.055*psi):
                        ro = (lambdap - 0.055*(3 + psi))/math.pow(lambdap, 2)
                        if ro > 1:
                            ro = 1
                    elif lambdap <= 0.5 + math.sqrt(0.085-0.055*psi):
                        ro = 1
                    beff = ro*b_nadvuceno
                    be1 = (2/(5 - psi))*b_nadvuceno
                    be2 = beff - be1 + aw*math.sqrt(2)
                    be1 = (2/(5 - psi))*b_nadvuceno + aw*math.sqrt(2)
                    bt = 0
                    bc = b_nadvuceno + 2*aw*math.sqrt(2)
                elif psi < 0 and psi >= -1:
                    ksigma = 7.81 - 6.29*psi + 9.78*math.pow(psi, 2)
                    b_nadvuceno = (h - tf1 - tf2 - 2*aw*math.sqrt(2)) 
                    lambdap = b_nadvuceno/tw/(28.4*epsilon*math.sqrt(ksigma))
                    uslov = 0.5 + math.sqrt(0.085-0.055*psi)
                    if lambdap > uslov:
                        ro = (lambdap - 0.055*(3 + psi))/math.pow(lambdap, 2)
                        if ro > 1:
                            ro = 1
                    elif lambdap <= uslov:
                        ro = 1
                    bc = b_nadvuceno/(1 - psi)
                    beff = ro*bc
                    be1 = 0.4*beff + aw*math.sqrt(2)
                    be2 = 0.6*beff + aw*math.sqrt(2)
                    bc = bc + 2*math.sqrt(2)*aw
                    bt = h - tf1 -tf2 - bc
                elif psi < -1 and psi >= -3:
                    ksigma = 5.98/math.pow(1-psi, 2)
                    b_nadvuceno = (h - tf1 - tf2 - 2*aw*math.sqrt(2)) 
                    lambdap = b_nadvuceno/tw/(28.4*epsilon*math.sqrt(ksigma))
                    if lambdap > 0.5 + math.sqrt(0.085-0.055*psi):
                        ro = (lambdap - 0.055*(3 + psi))/math.pow(lambdap, 2)
                        if ro > 1:
                            ro = 1
                    elif lambdap <= 0.5 + math.sqrt(0.085-0.055*psi):
                        ro = 1
                    bc = b_nadvuceno/(1 - psi)
                    beff = ro*bc
                    be1 = 0.4*beff + aw*math.sqrt(2)
                    be2 = 0.6*beff + aw*math.sqrt(2)
                    bc = bc + 2*math.sqrt(2)*aw
                    bt = h - tf1 -tf2 - bc
                Aw = be1*tw + be2*tw + bt*tw 
                A = Aw + Af1 + Af2
                zt1 = 1/A*(Af1*tf1/2 + be1*tw*(be1/2 + tf1) + be2*tw*(bc - be2/2 + tf1) + bt*tw*(bt/2 + bc + tf1) + Af2*(h-tf2/2))
                zt2 = h - zt1
                z1_ivica_rebra = zt1 - tf1
                z2_ivica_rebra = zt2 - tf2
                Iy = beff1*math.pow(tf1, 3)/12 + Af1*math.pow(zt1 - tf1/2, 2) + tw*math.pow(be1, 3)/12 + tw*be1*math.pow(zt1 - tf1 - be1/2, 2) + tw*math.pow(bt + be2, 3)/12 + tw*(be2 + bt)*math.pow((bt + be2)/2 -zt2, 2) + beff2*math.pow(tf2, 3)/12 + Af2*math.pow(zt2-tf2/2,2)
                #zt1_bruto = teziztebruto()
                #MEd = MEd + (zt1 - zt1_bruto)*NEd
                sigma1 = MEd/Iy*z1_ivica_rebra + NEd/A
                sigma2 = -MEd/Iy*z2_ivica_rebra + NEd/A
                psi = sigma2/sigma1

        MRd = Iy/max(zt1, zt2)*fy*math.pow(10, 3)
        niz = np.array([A, Iy, MRd, psi, MEd])
        return niz
    else:
        pass

def MomentAksijalna():
    A = povrsina()
    NRdbruto = A*fy*math.pow(10, 3)
    if abs(NEd)/NRdbruto > 1:
        print(f'\nNEd = {NEd} [kN] je veca od nosivosti bruto preseka NRd = {NRdbruto} [kN]!')
        exit()
    hn = NEd/(fy*math.pow(10, 3)*tw)
    if hn > h - tf1 - tf2:
        print('>>>>>Plasticna neutralna osa je u nozici!')
        exit()
    else:
        dpritisnuto = cw/2 + hn/2
        alfa = round(dpritisnuto/cw, 3)
        klase_elemenata = KlasaPreseka(alfa)
        klasa_nozice_1 = klase_elemenata[0]
        klasa_nozice_2 = klase_elemenata[1]
        klasa_rebra= klase_elemenata[2]
        klasa_preseka = klase_elemenata[3]
    niz = np.array([klasa_nozice_1, klasa_nozice_2, klasa_rebra, klasa_preseka])
    return niz

if NEd > 0:
    a = MomentAksijalna()
else:
    a = KlasaPreseka(alfa)

def AksijalnaNosivostBrutoNeto():
    A = povrsina()
    if klasa_preseka == 4:
        a = EfektivniPresek()
        A = a[0]
    NRd = A*fy*math.pow(10, 3)
    niz = np.array([A, NRd])
    return niz

klasa_nozice_1 = a[0]
klasa_nozice_2 = a[1]
klasa_rebra = a[2]
klasa_preseka = a[3]

print('\nKlasa nozice 1:', klasa_nozice_1)
print('Klasa nozice 2:', klasa_nozice_2)
print('Klasa rebra:', klasa_rebra)
print('\n>>>>Klasa preseka:', klasa_preseka)

def FleksionoIzvijanje():
    niz = AksijalnaNosivostBrutoNeto()
    A = niz[0]
    NRd = niz[1]
    #ly = float(input('Unesi duzinu izvijanja oko y ose [m]: '))
    ly = 12
    #lz = float(input('Unesi duzinu izvijanja oko z ose [m]: '))
    lz = 6
    #alfay = float(input('Unesi koeficijent krive izvijanja \u03B1,y: '))
    alfay = 0.34
    lambday = ly/iy
    lambdaz = lz/iz
    lambda1 = 93.9*epsilon
    #alfaz = float(input('Unesi koeficijent krive izvijanja \u03B1,z: '))
    alfaz = 0.49
    lambdan_y = lambday/lambda1
    lambdan_z = lambdaz/lambda1
    Fiy = 0.5*(1 + alfay*(lambdan_y - 0.2) + math.pow(lambdan_y, 2))
    Fiz = 0.5*(1 + alfaz*(lambdan_z - 0.2) + math.pow(lambdan_z, 2))
    kapay = 1/(Fiy + math.sqrt(math.pow(Fiy, 2) - math.pow(lambdan_y, 2)))
    kapaz = 1/(Fiz + math.sqrt(math.pow(Fiz, 2) - math.pow(lambdan_z, 2)))
    kapa = min(kapay, kapaz, 1)
    print('kapay = ', kapay)
    print('kapaz = ', kapaz)
    NRd = kapa*NRd
    return NRd

#TODO torziono izvijanje
#TODO bocno torziono
#TODO smicanje i savijanje

def MomentNosivosti():
    niz = AksijalnaNosivostBrutoNeto()
    A = niz[0]
    NRd = niz[1]
    if klasa_preseka in [1, 2] and profil == 'ZAVAREN':
        #Plasticni moment nosivosti
        zt1 = (Af1*tf1/2 + alfa*d*tw*(alfa*d/2 + tf1))/(Af1 + alfa*d*tw)
        d1 = alfa*d +tf1 - zt1
        zt2 = (Af2*tf2/2 + (d-alfa*d)*tw*((d-alfa*d)/2 + tf2))/(Af2 + (d-alfa*d)*tw)
        d2 = (d-alfa*d)-zt2+tf2
        Wply = 0.5*A*(d1+d2)
        MRdply = Wply*fy*math.pow(10, 3)
        MRdely = Wely*fy*math.pow(10, 3)
        MRdeff = 'Puna nosivost preseka!'
    elif klasa_preseka == 3 and b1 == b2 and tf1 == tf2:
        deltadw = d - 80*tw*epsilon
        F1 = Af1*fy*math.pow(10, 3)
        F2 = 20*fy*math.pow(tw, 2)*epsilon*math.pow(10, 3)
        F3 = F2
        F4 = 2*F2
        F5 = Af2*fy*math.pow(10, 3)
        z1 = 40*tw*epsilon + deltadw + tf1/2
        z2 = 30*tw*epsilon + deltadw
        z3 = 10*tw*epsilon
        z4 = 20*tw*epsilon
        z5 = 40*tw*epsilon + tf2/2
        MRdely = Wely*fy*math.pow(10, 3)
        MRdply = F1*z1 + F2*z2 + F3*z3 + F4*z4 + F5*z5
        MRdeff = 'Puna nosivost preseka!'
    elif klasa_preseka == 3 and b1 != b2 or tf1 != tf2:
        d1 = (h - tf1 - tf2)/2 - (Af1 - Af2)/(2*tw)
        F1 = Af1*fy*math.pow(10, 3)
        F2 = d1*tw*fy/2*math.pow(10, 3)
        F3 = d1*tw*fy/2*math.pow(10, 3)
        F4 = (d - 2*d1)*tw*fy*math.pow(10, 3)
        F5 = Af2*fy*math.pow(10, 3)
        z1 = d1 + tf1/2
        z2 = 2/3*d1
        z3 = 2/3*d1
        z4 = d/2
        z5 = d - d1 + tf2/2 
        MRdply = F1*z1 + F2*z2 + F3*z3 + F4*z4 + F5*z5
        MRdely = Wely*fy*math.pow(10, 3)
        MRdeff = 'Puna nosivost preseka!'
    elif klasa_preseka in [1, 2] and profil != 'ZAVAREN':
        Wply = wply()
        MRdply = Wply*fy*math.pow(10, 3)
        MRdely = Wely*fy*math.pow(10, 3)
        MRdeff = 'Puna nosivost preseka!'
    elif klasa_preseka == 4:
        print('\n>>>>Efektivni poprecni presek!')
        niz = EfektivniPresek()
        Iy = niz[1]
        A = niz[0]
        MEd = niz[4]
        MRdeff = niz[2]
        psi = niz[3]
        print('Iy, eff =', Iy*math.pow(10, 12), '[mm^4]')
        print('A, eff =', A*math.pow(10, 6), '[mm^2]')
        print('\u03C8 =', psi, '(iterativno sa greskom od 0.001)')
        MRdely = 'Efektivna sirina!'
        MRdply = 'Efektivna sirina!'

#MomentAksijalna
    n = NEd/NRd
    a = min((A - b1*tf1 - b2*tf2)/A, 0.5)
    if klasa_preseka < 4:
        if NEd/NRd > 0.25 or NEd/(0.5*(tw*(h-tf1-tf2)*fy*math.pow(10, 3))) > 1:
            print('\n>>>>Redukcija nosivosti momenta savijanja zbog aksijalne sile pritiska!')
            MRdmn = MRdply*(1-n)/(1-0.5*a)
        else:
            MRdmn = MRdply
    elif klasa_preseka == 4:
        MRdmn = MRdeff*(1-n)/(1-0.5*a)
        if MRdmn > MRdeff:
            MRdmn = MRdeff
    print('\n>>>>Nosivost preseka na savijanje:') 
    print('MRd,el,y =', MRdely, '[kNm]')
    print('MRd,pl,y =', MRdply, '[kNm]')
    print('Interakcija M i N: MRd, MN =', MRdmn, '[kNm]')
    print('MRd, eff =', MRdeff, '[kNm]')

    if klasa_preseka < 4:
        MRd = min(MRdply, MRdmn)
    else:
        MRd = min(MRdmn, MRdeff)
    print('\nKonacna nosivost: MRd =', MRd ,'[kNm]')

if NEd > 0:
    query = str(input('Raditi kontrolu fleksionog izvijanja (da|ne)?: ')).upper()
    if query == 'DA':
        NbRd = FleksionoIzvijanje()
    else:
        NbRd = 'Nije zatrazen proracun!'
else:
    NbRd = 'Nema izvijanja!'

print('\n>>>>Aksijalna nosivost:')
A = povrsina()
NRd = A*fy*math.pow(10, 3)
print('NRd, bruto =', NRd, '[kN]')
Nnosivost = AksijalnaNosivostBrutoNeto()
print('NRd, eff =', Nnosivost[1], '[kN]')
print('Nb,Rd,fleksiono = ', NbRd, '[kN]')

    
MomentNosivosti()
