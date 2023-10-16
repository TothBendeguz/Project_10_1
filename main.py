import random
import time
import sys
import os
from helyszínek.pince import pince 

zseblampa = False
kabát = False
labirintusKod = False










os.system('cls')
def slowPrint(string, speed=0.05):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

#slowPrint('1925-ben, egy hideg téli este, a falu szélén magasodott az elhagyatott kastély. A vidék fehér hóval volt bevonva, és a kastély sötét, hátborzongató alakja feltűnt a horizonton. Az épület régóta lakatlan volt, és hosszú ideje tartották hírhedtnek a helyiek. A rémtörténetek egytől-egyig sötét eseményekről szóltak, amelyek itt zajlottak, és az emberek úgy érezték, hogy a kastély titokzatos erőket rejteget. Most, a hóesésben, az emberek újra hallották a kastély suttogásait, és az idő eljött, hogy felderítsék a múlt sötét rejtélyeit. Az elhagyatott kastély magasodott a téli éjszaka közepén, készen arra, hogy felfedezzék a titkait, mielőtt a borzalmak újra elszabadulnak, és bekebelezik az éjszakát. Az elhagyatott kastély falai tele vannak titkokkal, és most a te feladatod felfedezni ezt a sötét és rejtélyes helyet.', 0.03)

input("\nHa készen álasz nyomd meg az entert!")
os.system('cls')

print('Beértél az ajtón')

def foBejarat():
    print('1..Jobbra látsz egy pincét')
    print('2..Ha előre nézel látsz egy folyosót')
    print('3..Balra látsz egy nagy csarnokot')
    v = input('Merre folytatod az utad?: ')
    return v
v = foBejarat()

match v:
    case '1':
        pince()
        

