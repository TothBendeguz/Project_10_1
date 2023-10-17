import random
import time
import sys
import os
#from helyszínek.pince import pince 
#from helyszínek.csarnok import csarnok

zseblampa = False
kabat = False
labirintusKod = False
hp = 100
jozansag = 100









os.system('cls')
def slowPrint(string, speed=0.05):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

slowPrint('1925-ben, egy hideg téli este, a falu szélén magasodott az elhagyatott kastély. A vidék fehér hóval volt bevonva, és a kastély sötét, hátborzongató alakja feltűnt a horizonton. Az épület régóta lakatlan volt, és hosszú ideje tartották hírhedtnek a helyiek. A rémtörténetek egytől-egyig sötét eseményekről szóltak, amelyek itt zajlottak, és az emberek úgy érezték, hogy a kastély titokzatos erőket rejteget. Most, a hóesésben, az emberek újra hallották a kastély suttogásait, és az idő eljött, hogy felderítsék a múlt sötét rejtélyeit. Az elhagyatott kastély magasodott a téli éjszaka közepén, készen arra, hogy felfedezzék a titkait, mielőtt a borzalmak újra elszabadulnak, és bekebelezik az éjszakát. Az elhagyatott kastély falai tele vannak titkokkal, és most a te feladatod felfedezni ezt a sötét és rejtélyes helyet. Amint belépsz a főbejáraton az ajtó mögötted örökre becsukódik.', 0.001)

input("\n\nHa készen álasz nyomd meg az entert!")
os.system('cls')

def foBejarat():
    os.system('cls')
    print('A főbejáratnál vagy')
    print('1 >> Jobbra látsz egy pincét')
    print('2 >> Előtted van egy hosszú folyosó')
    print('3 >> Balra Egy nagy csarnokba nyílik egy ajtó')

    v = input('Merre haladsz tovább?: >> ')
    match v:
        case '1':
            return 'pince'
        case '2':
            return 'folyoso'
        case '3':
            return 'csarnok'

def pince():
    global kabat
    os.system('cls')
    print('A pince bejáratánál vagy')
    print('1 >> Egy raktár ajtaja nyílik meg előtted ')
    print('2 >> Egyenesen nézve látsz egy kriptát ami elég félelmetes és sötét')
    print('3 >> A harmadik hely egy titkos labort rejt')
    print('4 >> Vissza a főbejárathoz')

    v = input('Merre haladsz tovább?: >> ')
    match v:
        case '1':
            global kabat
            os.system('cls')
            print('A raktárban megtalálod az eldugott kabátot')
            kabat = True
            input("\nHa készen álasz nyomd meg az entert!")
            return 'pince'
        case '2':
            return 'pince'
        case '3':
            return 'pince'
        case '4':
            return 'fobejarat'

def folyoso():
    os.system('cls')
    print('A hosszú folyosón sétálsz')
    print('1 >> Jobb kezednél meglátsz egy ajtót ami kintre vezet')
    print('2 >> Tovább haladva egy konyhát látsz')
    print('3 >> A konyha mellett egyből találsz egy étkezőt')
    print('4 >> Vissza szaladsz a főbejárathoz')

    v = input('Merre haladsz tovább?: >> ')
    match v:
        case '1':
            if kabat == True:
                os.system('cls')
                print('Mivel volt kabátot sikeresen kitudtál menni az udvarra!')
                input("\nHa készen álasz nyomd meg az entert!")
                return 'udvar'
            if kabat == False:
                os.system('cls')
                print('Kimentél de egyből vissza jöttél hiszen kabát nélkül fáztál. Keresgélj tovább!')
                input("\nHa készen álasz nyomd meg az entert!")
                return 'folyoso'
        case '2':
            return 'folyoso'
        case '3':
            return 'csarnok'
        case '4':
            return 'fobejarat'
        
def udvar():
    os.system('cls')
    print('Kiértél az udvarra.')
    print('Rettentő sötét van és nem látsz a távolba.')
    print('Csak 3 utat látsz.')
    print('1 >> Jobbra')
    print('2 >> Egyenesen')
    print('3 >> Balra')
    print('4 >> Inkább vissza megyek a folyosóra és vissza jövök később')

    v = input('Merre haladsz tovább?: >> ')
    match v:
        case '1':
            os.system('cls')
            print('Találtál egy gyönyörű szikláskertet amelyben nincsen semmi ilyesztő. Végre egy nyugodt helyen vagy.')
            print('Amikor készen állsz haladj tovább!')
            print('De vigyázz ne maradj itt sokáig!')
            input("\nHa készen álasz nyomd meg az entert!")            
            return 'udvar'
        case '2':
            os.system('cls')
            print('Egy köddel fedett tóhoz érkeztél.')
            print('Nagyon ilyesztő hely!')
            print('Itt ne maradj sokáig!')
            input("\nHa készen álasz nyomd meg az entert!")              
            return 'udvar'
        case '3':
            print('Egy labirintushoz érkezel mely egy kódót vár el tőled!')
            kodell = int(input('Mi a kód?: >> '))
            if kodell == 972 and labirintusKod == True:
                os.system('cls')
                print('Gratulálok, sikeresen túlélted és kijutottál a kastélyból')
                input("\nHa készen álasz nyomd meg az entert!")                    
                return 'kijarat'
            if kodell != 972:
                os.system('cls')
                print('Nem jó kód!')
                print('Keresgélj tovább!')
                input("\nHa készen álasz nyomd meg az entert!")
                return 'udvar'        
        case '4':
            return 'fobejarat'

"""
def csarnok():
    os.system('cls')
    print('A csarnokban vagy')
    print('1 >> A csarnok elje')
    print('2 >> A csarnok közepe')
    print('3 >> A csarnok vége')

    v = input('Merre haladsz tovább?: >> ')
    match v:
        case '1':
            return 'cseleje'
        case '2':
            return ''
        case '3':
            return 'csarnok'
"""

hely = foBejarat()
while hely != 'kijarat':
    match hely:
        case 'fobejarat':
            hely = foBejarat()
        case 'csarnok':
            pass
        case 'pince':
            hely = pince()
        case 'folyoso':
            hely = folyoso()
        case 'udvar':
            hely = udvar()