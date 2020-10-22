import pandas as pd
import numpy as np
import math


class Profil:
    def __init__(self):
        ime_profila = str(input('Unesi ime profila, ako je zavaren kucaj "zavaren" (bez navodnika): ')).replace(' ', '')
        ime_profila = ime_profila.upper()
        self.ime_profila = ime_profila
        print(f'\nUcitani profil je: {ime_profila}')
        df = pd.read_csv('VruceValjani.csv', delimiter=',', skipinitialspace=True, encoding='UTF-8')
        self.df = df
        lista_profila = df['Profil'].to_list()
        self.lista_profila = lista_profila
        if ime_profila in lista_profila:
            indeks = lista_profila.index(ime_profila)
            self.indeks = indeks
            self.lista_profila = lista_profila
        elif ime_profila == 'ZAVAREN':
            h = float(input('Unesi visinu profila h [mm]: '))
            h = h/1000  # [m]
            self.h = h
            b1 = float(input('Unesi sirinu pritisnute nozice b1 [mm]: '))
            b1 = b1/1000  # [m]
            b2 = float(input('Unesi sirinu zategnute nozice b2 [mm]: '))
            b2 = b2/1000
            self.b1 = b1
            self.b2 = b2
            tf1 = float(input('Unesi debljinu pritisnute nozice tf1 [mm]: '))
            tf1 = tf1/1000  # [m]
            tf2 = float(input('Unesi debljinu zategnute nozice tf2 [mm]: '))
            tf2 = tf2/1000
            self.tf1 = tf1
            self.tf2 = tf2
            tw = float(input('Unesi debljinu rebra tw [mm]: '))
            tw = tw/1000
            self.tw = tw
            aw = float(input('Unesi debljinu vara izmedju nozice i rebra aw [mm]: '))
            aw = aw/1000
            self.aw = aw
            hi = h - tf1 - tf2 - 2*aw*math.sqrt(2)
            self.hi = hi
        else:
            print('\nIme profila mora biti iz kolone profili ili "zavaren"!')
            exit()

    def h(self):
        if self.ime_profila in self.lista_profila:
            h_niz = self.df['h [mm]'].to_numpy()*math.pow(10, -3)  # [m]
            h = h_niz[self.indeks]
        return h

    def b(self):
        if self.ime_profila in self.lista_profila:
            b_niz = self.df['b [mm]'].to_numpy()*math.pow(10, -3)  # [m]
            b = b_niz[self.indeks]
            b1 = b
            b2 = b
        b_niz = np.array([b1, b2])
        return b_niz

    def tf(self):
        if self.ime_profila in self.lista_profila:
            tf_niz = self.df['tf [mm]'].to_numpy()*math.pow(10, -3)  # [m]
            tf = tf_niz[self.indeks]
            tf1 = tf
            tf2 = tf
        tf_niz = np.array([tf1, tf2])
        return tf_niz

    def tw(self):
        if self.ime_profila in self.lista_profila:
            tw_niz = self.df['tw [mm]'].to_numpy() * math.pow(10, -3)  # [m]
            tw = tw_niz[self.indeks]
        return tw

    def hi(self):
        if self.ime_profila in self.lista_profila:
            hi_niz = self.df['hi [mm]'].to_numpy() * math.pow(10, -3)  # [m]
            hi = hi_niz[self.indeks]
            return hi

dimenzija = Profil()
