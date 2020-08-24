# grf-bg
### Python3 skripte za razne proracune elemenata iz betonskih i metalnih konstrukcija po EC
##### Dokumentacija o nacinu rada skripti iz betonskih konstrukcija je u pdf formatu na ovom [linku](https://github.com/nikolalakic/grf-bg/raw/branch/master/Wiki/detaljifunkcionisanja.pdf), detalji rada skripti iz metala ce biti objavljeni tokom vremena.
##### Demo rada skripti iz betonskih konstrukcija
![Alt Text](https://nikolal.keybase.pub/grfcartel_sajt/demo.gif)
#### _Instalacija:_

##### **Windows:**


1. Pokreni download klikom na [link](https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe) koji ce preuzeti Python3.8 i pokreni instalaciju. Kada se pokrene cekiraj "add to path" i idi na "Custom installation". U "Custom installation" cekiraj sve i nastavi sa instalacijom. Kada se zavrsi pitace te da produzis character limit, samo klikni na plavi tekst koji ti se pokaze.
To je to, instalacija je uspesna.
2. Nakon zavrsene instalacije pokreni powershell desnim klikom na start > WindowsPowerShell(admin). Potom ukucaj sledecu komandu:
`pip install numpy pandas matplotlib sympy`, verovatno ce traziti da azuriras `pip` pa samo ukucaj `python -m pip install --upgrade pip`.

To je to, spremno je sve za pokretanje skripti.

#### _Pokretanje skripti (brzi nacin, pogledaj dole za bolji nacin):_

1. Skini zip fajl sa ovog [linka](https://github.com/nikolalakic/grf-bg/archive/master.zip), kad se skine ekstraktuj arhivu (unzip) i udji u folder grf-bg-master.
2. Izaberi folder od interesa (BetonskeKonstrukcije ili MetalneKonstrukcije), otvori PowerShell kao malo pre, samo sto sad nije potrebna administrator privilegija, i samo prevuci skriptu koju zelis u PowerShell i skripta se sama pokrece.

Ovo je brzi nacin, ali se za svaku promenu koda ili dodavanja novih skripti mora ponoviti postupak _Pokretanje skripti_.

#### Bolji nacin preuzimanja skripti:

1. Uradi prvo korak _Instalacija da bi instalirao Python_, potom otvori PowerShell kao administrator i nalepi ovo (nalepis tako sto kliknes desnim klikom u PowerShell): `Set-ExecutionPolicy RemoteSigned -scope CurrentUser` i stisni enter, kad te pita nesto samo ukucaj `y` i stisni enter. Potom nalepi ovo `iwr -useb get.scoop.sh | iex` i restartuj PowerShell.
2. Scoop je instaliran, sad u PowerShell-u nalepi ovo: `scoop install curl git`
3. Folder sa skriptama skidas tako sto izaberes neki folder (bilo gde, moze i desktop), i drzis _shift_ i kliknes desni klik, i kliknes potom na "Open Powershell window here". Pokreces skidanje foldera sa `git clone https://codeberg.org/nikolal/grf-bg.git`
4. Primetices da se folder skinuo i velika prednost ovog nacina je to sto sve promene i najnovije skripte preuzimas pokretanjem PowerShell-a u skinutom folderu sa drzanjem _shift_-a u tom folderu i klikom na desni klik, pa potom "Open PowerShell window here", sve promene dobijas sa kucanjem `git pull` 
5. Skripte pokreces sa prevlacenjem zeljene skripte u PowerShell-u

#### **Linux/MacOS:**

1. Imas vec pajton, samo ti fale `numpy`,`pandas`, `matplotlib` i `sympy`, instaliras ih kucanjem sledeceg u terminalu: `sudo pip3 install numpy pandas matplotlib sympy`  
2. Instaliraj git ako vec nisi sa: `sudo apt install git -y`, za Arch Linux: `sudo pacman -S git`
3. Kloniraj riznicu sa: `git clone https://github.com/nikolalakic/grf-bg.git`
4. Promeni radni folder sa: `cd grf-bg`
5. Pokreces skripte sa: `python3 <ime zeljene skripte.py>`

Ove skripte sluze da olaksaju proracun, rezultate uvek gledaj kriticki jer su greske moguce. Testirane su BetonskeKonstrukcije na raznim zadacima ali molim korisnike da koriste svoju inzenjersku procenu valjanosti rezultata, jer skripte nisu svemoguce (npr, SlozenoSavijanje.py ne prepoznaje mali ekscentricitet niti je u mogucnosti da radi proracun kada je u pitanju mali ekscentricitet)

Za sugestije i ostale komentare imate kontakt: https://lakic.one
