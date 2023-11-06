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
kard = False
konyvtarBoss = False
ehseg = 100
kaja = False
labirintusSzamkod = random.randint(100,999)




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
    v = 0
    while v != 1 and 2 and 3:
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
    global hp
    v = 0
    while v != 1 and 2 and 3 and 4:
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
                if kabat == False:
                    print('A raktárban megtalálod az eldugott kabátot')
                    kabat = True
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'pince'
                else:
                    print('Már megtaláltad a kabátot.')
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'pince'
            case '2':
                os.system('cls')
                print('Beértél a kriptába.')
                time.sleep(1.5)
                print('Nagy zajt keltesz, ezzel felébresztettél egy szellemet.')
                time.sleep(1.5)
                print('1 >> Megálsz vele harcolni')
                time.sleep(1.5)
                print('2 >> Megpróbálsz elfutni.')
                cselekves = 0
                while cselekves != 1 and 2:
                    cselekves = input('Mit csinálsz?: >> ')
                    match cselekves:
                        case '1':
                            if kard == True:
                                os.system('cls')
                                print('Most mivel volt kardod szerencsével jártál és legyőzted a szellemet.')
                                input("\nHa készen álasz nyomd meg az entert!")                        
                                return 'pince'
                            else:
                                os.system('cls')
                                print('Mivel akartad legyőzni a szellemet?')
                                time.sleep(1.5)
                                print('Meghaltál, a játéknak vége')
                                time.sleep(1.5)
                                return 'kijarat'
                        case '2':
                            os.system('cls')
                            print('Gyorsan elkezdesz futni vissza a pincéhez.')
                            time.sleep(1.5)
                            print('A szellem elkapja a lábad és megsebez.')
                            time.sleep(1.5)
                            print('Ezek után te sikeresen vissza érsz viszont vesztettél -10 hp-t.')
                            time.sleep(1.5)
                            hp -= 10
                            if hp > 0:
                                pass
                            else:
                                print('Meghaltál')
                                return 'kijarat'
                            input("\nHa készen álasz nyomd meg az entert!")
                            return 'pince'
            case '3':
                os.system('cls')
                print('Megérkeztél a laborba ahol egy kis üvegcsét találsz.')
                time.sleep(1.5)
                print('Meg tudod kockáztatni, hogy megiszod vagy sem.')
                time.sleep(1.5)
                print('1 >> Beleiszol.')
                time.sleep(1.5)
                print('2 >> Inkább mész máshova!')
                cselekves = 0
                while cselekves != 1 and 2:
                    cselekves = input('Mit csinálsz?: >> ')
                    match cselekves:
                        case '1':
                            esely = random.randint(1,2)
                            if esely == 1:
                                print('Kinyitod az üveget')
                                time.sleep(1.5)
                                print('Belekortyolsz')
                                time.sleep(1.5)
                                print('Jobban érzed magad.')
                                time.sleep(1.5)
                                print('A hp-d növekedett 5-el')
                                time.sleep(1.5)
                                if hp < 95:
                                    hp += 5
                                else:
                                    hp += 0
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'pince'
                            if esely == 2:
                                print('Kinyitod az üveget')
                                time.sleep(1.5)
                                print('Belekortyolsz')
                                time.sleep(1.5)
                                print('Rossz érzést érzel majd, hánysz egyet.')
                                time.sleep(1.5)
                                print('A hp-d csökkent 10-el')
                                time.sleep(1.5)
                                hp -= 10
                                if hp > 0:
                                    pass
                                else:
                                    print('Meghaltál')
                                    return 'kijarat'
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'pince'
                        case '2':
                            return 'pince'
            case '4':
                return 'fobejarat'

def folyoso():
    v = 0
    while v != 1 and 2 and 3 and 4 and 5:
        os.system('cls')
        print('A hosszú folyosón sétálsz')
        print('1 >> Jobb kezednél meglátsz egy ajtót ami kintre vezet')
        print('2 >> Tovább haladva egy konyhát látsz')
        print('3 >> A konyha mellett egyből találsz egy étkezőt')
        print('4 >> Észre veszel egy könyvtárba nyíló ajtót is')
        print('5 >> Vissza szaladsz a főbejárathoz')

        v = input('Merre haladsz tovább?: >> ')
        match v:
            case '1':
                if kabat == True:
                    os.system('cls')
                    print('Mivel volt kabátot sikeresen kitudtál menni az udvarra!')
                    time.sleep(1.5)
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'udvar'
                if kabat == False:
                    os.system('cls')
                    print('Kimentél de egyből vissza jöttél hiszen kabát nélkül fáztál. Keresgélj tovább!')
                    time.sleep(1.5)
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'folyoso'
            case '2':
                return 'konyha'
            case '3':
                return 'etkezo'
            case '4':
                return 'konyvtar'
            case '5':
                return 'fobejarat'
        
def udvar():
    os.system('cls')
    print('Kiértél az udvarra.')
    time.sleep(1.5)
    print('Rettentő sötét van és nem látsz a távolba.')
    time.sleep(1.5)
    print('Csak 3 utat látsz.')
    time.sleep(1.5)
    print('1 >> Jobbra')
    #time.sleep(1.5)
    print('2 >> Egyenesen')
    #time.sleep(1.5)
    print('3 >> Balra')
    #time.sleep(1.5)
    print('4 >> Inkább vissza megyek a folyosóra és vissza jövök később')
    #time.sleep(1.5)
    v = 0
    while v != 1 and 2 and 3 and 4:
        v = input('Merre haladsz tovább?: >> ')
        match v:
            case '1':
                os.system('cls')
                print('Találtál egy gyönyörű szikláskertet amelyben nincsen semmi ilyesztő. Végre egy nyugodt helyen vagy.')
                time.sleep(1.5)
                print('Amikor készen állsz haladj tovább!')
                time.sleep(1.5)
                print('De vigyázz ne maradj itt sokáig!')
                time.sleep(1.5)
                input("\nHa készen álasz nyomd meg az entert!")            
                return 'udvar'
            case '2':
                os.system('cls')
                print('Egy köddel fedett tóhoz érkeztél.')
                time.sleep(1.5)
                print('Nagyon ilyesztő hely!')
                time.sleep(1.5)
                print('Itt ne maradj sokáig!')
                time.sleep(1.5)
                input("\nHa készen álasz nyomd meg az entert!")              
                return 'udvar'
            case '3':
                os.system('cls')
                print('Egy labirintushoz érkezel mely egy kódót vár el tőled!')
                time.sleep(1.5)
                kodell = int(input('Mi a kód?: >> '))
                if kodell == labirintusSzamkod and labirintusKod == True:
                    os.system('cls')
                    print('Gratulálok, sikeresen túlélted és kijutottál a kastélyból')
                    time.sleep(1.5)
                    input("\nHa készen álasz nyomd meg az entert!")                    
                    return 'kijarat'
                else:
                    os.system('cls')
                    time.sleep(1.5)
                    print('Nem jó kód!')
                    time.sleep(1.5)
                    print('Keresgélj tovább!')
                    time.sleep(1.5)
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'udvar'        
            case '4':
                return 'folyoso'

def csarnok():
    global kard
    v = 0
    while v != 1 and 2 and 3 and 4:
        os.system('cls')
        print('A csarnokban vagy')
        print('1 >> A csarnok eleje')
        print('2 >> A csarnok közepe')
        print('3 >> A csarnok vége')
        print('4 >> Vissza a főbejárathoz')
        v = input('Merre haladsz tovább?: >> ')
        match v:
            case '1':
                os.system('cls')
                print('Találsz egy papírt.')
                time.sleep(1.5)
                print('A papírra az van írva, hogy:')
                time.sleep(1.5)
                print("\x1B[3m" + 'Sajtos - Gyengeség: Italian' + "\x1B[0m")
                time.sleep(1.5)
                input("\nHa készen álasz nyomd meg az entert!")
                return 'csarnok'
            case '2':
                os.system('cls')
                print('A közepéről belátod a csarnok elejét meg a végét')
                time.sleep(1.5)
                print('Az elején látsz valamit ami nem tudod micsoda.')
                time.sleep(1.5)
                print('A végén látsz egy dobozt')
                time.sleep(1.5)
                input("\nHa készen álasz nyomd meg az entert!")
                return 'csarnok'
            case '3':
                os.system('cls')
                print('A csarnok végében találsz egy dobozt.')
                time.sleep(1.5)
                print('Ki akarod nyitni?:')
                time.sleep(1.5)
                print('1 >> igen')
                time.sleep(1.5)
                print('2 >> nem')
                time.sleep(1.5)
                cselekves = 0
                while cselekves != 1 and 2:
                    cselekves = input('Mit csinálsz?: >> ')
                    match cselekves:
                        case '1':
                            os.system('cls')
                            if kard == False:
                                print('Találsz egy kardot.')
                                print('Ez még jó lehet harcoknál.')
                                kard = True
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'csarnok'
                            else:
                                print('Már nálad van a kard.')
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'csarnok'
                        case '2':
                            return 'csarnok'
            case '4':
                return 'fobejarat'

def konyvtar():
    global hp
    global konyvtarBoss
    os.system('cls')
    print('A könyvtárban vagy.')
    time.sleep(1.5)
    print('A könyvtár a tudás bölcsője.')
    time.sleep(1.5)
    if konyvtarBoss == False:
        print('Megállít egy barátságosnak tűnő szellem.')
        time.sleep(1.5)
        print('1 >> Le állsz vele beszélni?')
        time.sleep(1.5)
        print('2 >> Vissza mész a folyosóra')
        time.sleep(1.5)
        mitCsinalsz = 0
        while mitCsinalsz != 1 and 2:
            mitCsinalsz = input('Mit csinálsz?: >> ')
            match mitCsinalsz:
                case '1':
                    os.system('cls')
                    print('Bemutatkozik neked:')
                    time.sleep(1.5)
                    print("\x1B[3m" + 'A nevem Sajtos Bálint.' + "\x1B[0m")
                    time.sleep(1.5)
                    print("\x1B[3m" + 'Ahhoz, hogy tovább haladj le kell győznöd egy sakk mérközésben.' + "\x1B[0m")
                    time.sleep(1.5)
                    print("\x1B[3m" + 'Vágjunk is bele.' + "\x1B[0m")
                    time.sleep(1.5)
                    print('1 >> Ruy lopez')
                    time.sleep(1.5)
                    print('2 >> Four knights')
                    time.sleep(1.5)
                    print('3 >> Italian game')
                    time.sleep(1.5)
                    megnyitas = 0
                    while megnyitas != 1 and 2 and 3:
                        megnyitas = input('Melyik megnyitást hozod?: >> ')
                        match megnyitas:
                            case '1':
                                os.system('cls')
                                print('A Játszma döntetlennel végződik, nem ér semmi baj, de nem haladhatsz tovább sem.')
                                time.sleep(1.5)
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'konyvtar'
                            case '2':
                                os.system('cls')
                                print('Ez Sajtos kedvenc megnyitása.')
                                time.sleep(1.5)
                                print('Vesztettél!')
                                time.sleep(1.5)
                                print('Mivel csúnyán el alázott ezért -20 hp')
                                time.sleep(1.5)
                                hp -= 20
                                if hp > 0:
                                    pass
                                else:
                                    print('Meghaltál')
                                    return 'kijarat'
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'konyvtar'
                            case '3':
                                os.system('cls')
                                print('Jól választottál, megnyerted a játékot')
                                time.sleep(1.5)
                                print('A nyereményed + 5 hp')
                                time.sleep(1.5)
                                if hp < 96:
                                    hp += 5
                                else:
                                    hp += 0
                                input("\nHa készen álasz nyomd meg az entert!")
                                konyvtarBoss = True
                                os.system('cls')
                                return 'konyvtarTeljesitett'
                case '2':
                    return 'folyoso'
    if konyvtarBoss == True:
        return 'konyvtarTeljesitett'
    
def etkezo():
    global kaja
    global ehseg
    v = 0
    while v != 1 and 2 and 3:
        os.system('cls')
        print('Megérkeztél az étkezőbe.')
        print('1 >> Jobb kezednél látsz egy asztalt ahová le tudsz ülni.')
        print('2 >> Balra van egy kiszolgáló hely.')
        print('3 >> Vissza a folyosóra')
        v = input('Merre haladsz tovább?: >> ')
        match v:
            case '1':
                if kaja == False:
                    os.system('cls')
                    print('Leültél az asztalhoz viszont nincs mit megenned.')
                    print('Menj a konyhába ha éhes vagy és készíts magadnak ételt.')
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'etkezo'
                if kaja == True:
                    os.system('cls')
                    print('Mivel csináltál kaját, van mit enned')
                    print('Elkezdesz enni.')
                    print('Végeztél, jól laktál, ezért ez +5 kaja.')
                    if ehseg < 96:
                        ehseg += 5
                    else:
                        ehseg += 0
                    input("\nHa készen álasz nyomd meg az entert!")
                    kaja = False
                    return 'etkezo'
            case '2':
                os.system('cls')
                print('Megérkezel a kiszolgáló helyhez.')
                print('A kiszolgáló, egy szellem, akit Tóth Szalmának hívnak.')
                print('Arról volt híres, hogy mindig változatosan oszt ételt.')
                print('1 >> Szeretnéd kockáztatni az ételt?')
                print('2 >> Inkább vissza mész az étkezőhez.')
                cselekves = 0
                while cselekves != 1 and 2:
                    cselekves = input('Mit csinálsz?: >> ')
                    match cselekves:
                        case '1':
                            esely = random.randint(1,3)
                            if esely == 1:
                                os.system('cls')
                                print('Elveszed az ételt.')
                                time.sleep(1.5)
                                print('Beleharapsz')
                                time.sleep(1.5)
                                print('Jobban érzed magad.')
                                time.sleep(1.5)
                                print('A kajád növekedett 5-el')
                                time.sleep(1.5)
                                if ehseg < 96:
                                    ehseg += 5
                                else:
                                    ehseg += 0
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'etkezo'
                            if esely == 2:
                                os.system('cls')
                                print('Elveszed az ételt.')
                                time.sleep(1.5)
                                print('Beleharapsz')
                                time.sleep(1.5)
                                print('Rossz érzést érzel majd, hánysz egyet.')
                                time.sleep(1.5)
                                print('A kajád csökkent 10-el')
                                time.sleep(1.5)
                                ehseg -= 10
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'etkezo'
                            if esely == 3:
                                os.system('cls')
                                print('Elveszed az ételt.')
                                time.sleep(1.5)
                                print('Beleharapsz')
                                time.sleep(1.5)
                                print('Rettentő rosszul érzed magad.')
                                time.sleep(1.5)
                                print('Összeesel, majd meghalsz')
                                time.sleep(1.5)
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'kijarat'
                        case '2':
                            return 'etkezo'
            case '3':
                return 'folyoso'

def konyha():
    global kaja
    v = 0
    while v != 1 and 2:
        os.system('cls')
        print('Megérkeztél a konyhába')
        print('1 >> Nekiálsz ételt csinálni.')
        print('2 >> Inkább haladok tovább, vissza a folyosóra')
        v = input('Merre haladsz tovább?: >> ')
        match v:
            case '1':
                if kaja == True:
                    os.system('cls')
                    print('Már csináltál ételt.')
                    print('Egyszerre csak egy étel lehet nálad')
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'konyha'
                if kaja == False:
                    os.system('cls')
                    print('Elkezdesz ételt készíteni.')
                    for i in range(10, 0, -1):
                        print(i)
                        time.sleep(1) 
                    print('Megcsináltad az ételt')
                    kaja = True
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'konyha'
            case '2':
                return 'folyoso'

def konyvtarTeljesitett():
    v = 0
    while v != 1 and 2 and 3:
        os.system('cls')
        print('Mivel Sajtost már elverted, ezért tovább haladhatsz.')
        print('Merre haladsz tovább?')
        print('1 >> galéria')
        print('2 >> iroda')
        print('3 >> Vissza a folyosóra')

        v = input('Merre haladsz tovább?: >> ')
        match v:
            case '1':
                return 'galeria'
            case '2':
                return 'iroda'
            case '3':
                return 'folyoso'
        
def galeria():
    v = 0
    while v != 1 and 2 and 3:
        os.system('cls')
        print('Megérkeztél a galériába.')
        print('3 fele haladhatsz tovább.')
        print('1 >> Lépcsőházba')
        print('2 >> Melletted lévő irodába')
        print('3 >> Vissza a könyvtárba')
        v = input('Merre haladsz tovább?: >> ')
        match v:
            case '1':
                return 'lepcsohaz'
            case '2':
                return 'iroda'
            case '3':
                return 'konyvtarTeljesitett'

def iroda():
    global zseblampa
    v = 0
    while v != 1 and 2 and 3:
        os.system('cls')
        print('Megérkeztél az irodába ')
        if zseblampa == False:
            print('Az irodába való megérkezéskor találsz egy zseblámpát.')
            print('Ez még hasznos lehet sötét helyeken.')
            zseblampa = True
            input("\nHa készen álasz nyomd meg az entert!")
            return 'iroda'
        else:
            print('1 >> Könyvtár')
            print('2 >> Galéria')
            print('3 >> Lépcsőház')
            v = input('Merre haladsz tovább?: >> ')
            match v:
                case '1':
                    return 'konyvtarTeljesitett'
                case '2':
                    return 'galeria'
                case '3':
                    return 'lepcsohaz'
        
def lepcsohaz():
    v = 0
    while v != 1 and 2 and 3 and 4:
        os.system('cls')
        print('Megérkeztél a lépcsőházba')
        print('1 >> Innen mehetsz felfele az 1. emeletre')
        print('2 >> Padlás')
        print('3 >> Iroda')
        print('4 >> Galéria')
        v = input('Merre haladsz tovább?: >> ')
        match v:
            case '1':
                return 'elsoEmelet'
            case '2':
                return 'padlas'
            case '3':
                return 'iroda'
            case '4':
                return 'galeria'

def elsoEmelet():
    v = 0
    while 1 and 2 and 3:
        os.system('cls')
        print('Megérkeztél az első emeletre.')
        print('Egy folyosóval álsz újra szemben ahol további két ajtó van.')
        print('1 >> Jobb kezednél egy háloszobába vezető ajtót látsz.')
        print('2 >> Bal kezednél van egy mosdóba vezető ajtót látsz.')
        print('3 >> Vissza megyek e lépcsőházba.')
        v = input('Merre haladsz tovább?: >> ')
        match v:
            case '1':
                return 'haloszoba'
            case '2':
                return 'mosdo'
            case '3':
                return 'lepcsohaz'

def padlas():
    global hp
    global zseblampa
    global jozansag
    global labirintusKod
    if zseblampa == False:
        os.system('cls')
        print('Elkezdesz fálmászni a létrán.')
        time.sleep(1.5)
        print('Felértél.')
        time.sleep(1.5)
        print('Rettentő sötét van, ezért elkezdesz lámpát keresni.')
        time.sleep(1.5)
        print('Miközben keresed a lámpát megbotlasz egy dobozban és leesel.')
        time.sleep(1.5)
        print('Nagyon megütöd magad alig bírsz újra lábra állni, ezért ez -75 hp.')
        time.sleep(1.5)
        hp -= 75
        if hp > 0:
            pass
        else:
            print('Meghaltál')
            return 'kijarat'
        input("\nHa készen álasz nyomd meg az entert!")
        return 'lepcsohaz'
    else:
        os.system('cls')
        print('Elkezdesz fálmászni a létrán.')
        print('Felértél.')
        print('Rettentő sötét van, de mivel volt lámpád felkapcsolod azt.')
        print('1 >> Jobboldalon látsz egy könyvespolcot')
        print('2 >> Előtted a pince végébe elhagyatott cuccokat látsz')
        print('3 >> Bal kéznél egy törött tükröt')
        print('4 >> Inkább vissza megyek a lépcsőházba')
        v = 0
        while v != 1 and 2 and 3 and 4:
            v = input('Merre haladsz tovább?: >> ')
            match v:
                case '1':
                    os.system('cls')
                    print('Elkezdesz kutatni és találsz egy könyvet.')
                    print('Ki akarod nyitni a könyvet?')
                    print('1 >> Beleolvasol')
                    print('2 >> Hagyod inkább')
                    cselekves = 0
                    while cselekves != 1 and 2:
                        cselekves = input('Mit csinálsz?: >> ')
                        match cselekves:
                            case '1':
                                os.system('cls')
                                print('Elkezdesz beleolvasni.')
                                time.sleep(1.5)
                                print('Ezt találod benne: ')
                                time.sleep(1.5)
                                print("\x1B[3m" + 'A kitartó munka meghozza gyümölcsét!' + "\x1B[0m")
                                time.sleep(1.5)
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'padlas'
                            case '2':
                                return 'padlas'
                case '2':
                    os.system('cls')
                    print('Rengeteg cuccot látsz')
                    print('1 >> Neki állsz kotorni')
                    print('2 >> Inkább hagyod')
                    cselekves = 0
                    while cselekves != 1 and 2:
                        cselekves = input('Mit csinálsz?: >> ')
                        match cselekves:
                            case '1':
                                os.system('cls')
                                print('Elkezdesz kotorni.')
                                time.sleep(1.5)
                                print('Egy patkány fut el előtted.')
                                time.sleep(1.5)
                                print('Nagyon megijedsz.')
                                time.sleep(1.5)
                                print('Ezért csökken a józanságod, 30-al.')
                                jozansag -= 30
                                if jozansag > 0:
                                    pass
                                else:
                                    print('Meghaltál')
                                    return 'kijarat'
                                time.sleep(1.5)
                                input("\nHa készen álasz nyomd meg az entert!")
                                os.system('cls')
                                print('Bejebb még több cuccot látsz.')
                                print('1 >> Neki állsz tovább kotorni')
                                print('2 >> Inkább vissza mész a legelejére')
                                cselekves = 0
                                while cselekves != 1 and 2:
                                    cselekves = input('Mit csinálsz?: >> ')
                                    match cselekves:
                                        case '1':
                                            os.system('cls')
                                            print('Tovább kotorva egy újabb patkányt talász.')
                                            time.sleep(1.5)
                                            print('Hirtelen megharap.')
                                            time.sleep(1.5)
                                            print('Majd elfut.')
                                            time.sleep(1.5)
                                            print('A hp-d csökkent 15-el')
                                            hp -= 15
                                            if hp > 0:
                                                pass
                                            else:
                                                print('Meghaltál')
                                                return 'kijarat'
                                            input("\nHa készen álasz nyomd meg az entert!")
                                            os.system('cls')
                                            print('Bejebb még több cuccot látsz.')
                                            print('1 >> Neki állsz tovább kotorni')
                                            print('2 >> Inkább vissza mész a legelejére')
                                            cselekves = 0
                                            while cselekves != 1 and 2:
                                                cselekves = input('Mit csinálsz?: >> ')
                                                match cselekves:
                                                    case '1':
                                                        os.system('cls')
                                                        print('Találsz egy dobozt.')
                                                        print('1 >> Kinyitod')
                                                        print('2 >> Inkább vissza mész a padlás legelejére')
                                                        cselekves = 0
                                                        while cselekves != 1 and 2:
                                                            cselekves = input('Mit csinálsz?: >> ')
                                                            match cselekves:
                                                                case '1':
                                                                    os.system('cls')
                                                                    print('Elkezded kinyitni a dobozt')
                                                                    time.sleep(1.5)
                                                                    print('Találsz egy papírt.')
                                                                    time.sleep(1.5)
                                                                    print('A papíron egy kódot látsz:')
                                                                    time.sleep(1.5)
                                                                    print(f'A kód: {labirintusSzamkod}')
                                                                    labirintusKod = True
                                                                    time.sleep(1.5)
                                                                    input("\nHa készen álasz nyomd meg az entert!")
                                                                    return 'padlas'
                                                                case '2':
                                                                    return 'padlas'
                                                    case '2':
                                                        return 'padlas'
                                        case '2':
                                            return 'padlas'
                            case '2':
                                return 'padlas'
                case '3':
                    print('Oda érsz a törött tükörhöz.')
                    time.sleep(1.5)
                    print('1 >> Belenézel')
                    time.sleep(1.5)
                    print('2 >> Vissza mész a padlás legelejéhez')
                    cselekves = 0
                    while cselekves != 1 and 2:
                        cselekves = input('Mit csinálsz?: >> ')
                        match cselekves:
                            case '1':
                                print('Rávilá')
                            case '2':
                                return 'padlas'
                case '4':
                    os.system('cls')
                    print('Épp mászol lefelé és kialszik a zseblámpád fénye.')
                    time.sleep(3)
                    zseblampa = False
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'lepcsohaz'
                    """print('1 >> Megvizsgálod(értsd: kiszeded az elemet, vissza rakod stb...).')
                    print('2 >> Beletörődsz.')
                    cselekves = input('Mit csinálsz?: >> ')
                    match cselekves:
                        case '1':
                            os.system('cls')
                            if elem == False:
                                print('Elkezded kiszedni az elemet.')
                                print('Miközben szeded ki, megráz és vesztesz 50 hp-t')
                                hp -= 50
                                if hp > 0:
                                    pass
                                else:
                                    print('Meghaltál')
                                    return 'kijarat'
                                input("\nHa készen álasz nyomd meg az entert!")
                            else:
                                print('Elkezded kiszedni az elemet.')
                                print('Mivel volt elem nálad, ezért azt kicseréled a régivel.')
                                print('Később ezért újra tudod majd használni a lámpád')
                                zseblampa = True
                                elem = False
                                input("\nHa készen álasz nyomd meg az entert!")
                                return 'lepcsohaz'
                        case '2':
                            return 'lepcsohaz'
                        """
def haloszoba():
    print('Megérkeztél a ')
    print('1 >> ')
    print('2 >> ')
    print('3 >> ')
    v = input('Merre haladsz tovább?: >> ')
    match v:
        case '1':
            return ''
        case '2':
            return ''
        case '3':
            return ''
        
def mosdo():
    print('Megérkeztél a ')
    print('1 >> ')
    print('2 >> ')
    print('3 >> ')
    v = input('Merre haladsz tovább?: >> ')
    match v:
        case '1':
            return ''
        case '2':
            return ''
        case '3':
            return ''

hely = foBejarat()
while hely != 'kijarat':
    match hely:
        case 'fobejarat':
            hely = foBejarat()
        case 'csarnok':
            hely = csarnok()
        case 'pince':
            hely = pince()
        case 'folyoso':
            hely = folyoso()
        case 'udvar':
            hely = udvar()
        case 'konyha':
            hely = konyha()
        case 'etkezo':
            hely = etkezo()
        case 'konyvtar':
            hely = konyvtar()
        case 'konyvtarTeljesitett':
            hely = konyvtarTeljesitett()
        case 'galeria':
            hely = galeria()
        case 'iroda':
            hely = iroda()
        case 'lepcsohaz':
            hely = lepcsohaz()
        case 'elsoEmelet':
            hely = elsoEmelet()
        case 'padlas':
            hely = padlas()
        case 'haloszoba':
            hely = haloszoba()
        case 'mosdo':
            hely = mosdo()