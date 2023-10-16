import random
import time
import sys
import os
#from helyszínek.pince import pince 
#from helyszínek.csarnok import csarnok

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

def foBejarat():
    print('A főbejáratban vagy')
    print('1 >> Jobbra látsz egy pincét')
    print('2 >> előtted van egy hosszú folyosó')
    print('3 >> Balra Egy nagy csarnokba nyíl egy ajtó')

    v = input()
    match v:
        case '1':
            return 'pince'
        case '2':
            return 'folyoso'
        case '3':
            return 'csarnok'

def pince():
    print('A pince bejáratábn vagy')
    print('1 >> Jobbra látsz egy pincét')
    print('2 >> előtted van egy hosszú folyosó')
    print('3 >> Balra Egy nagy csarnokba nyíl egy ajtó')
    print('4 >> Vissza a főbejárathoz')

    v = input()
    match v:
        case '1':
            return '#'
        case '2':
            return '#'
        case '3':
            return '#'
        case '4':
            return 'fobejarat'
        



hely = foBejarat()
while hely != 'asd':
    match hely:
        case 'fobejarat':
            hely = foBejarat()
        case 'asd':
            hely = ()
        case 'pince':
            hely = pince()