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
            print('Nagy zajt keltesz, ezzel felébresztettél egy szellemet.')
            print('1 >> Megálsz vele harcolni')
            print('2 >> Megpróbálsz elfutni.')
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
                        print('Meghaltál, a játéknak vége')
                        return 'kijarat'
                case '2':
                    global hp
                    os.system('cls')
                    print('Gyorsan elkezdesz futni vissza a pincéhez.')
                    print('A szellem elkapja a lábad és megsebez.')
                    print('Ezek után te sikeresen vissza érsz viszont vesztettél -10 hp-t.')
                    input("\nHa készen álasz nyomd meg az entert!")
                    hp =- 10
                    return 'pince'
        case '3':
            os.system('cls')
            print('Megérkeztél a laborba ahol egy kis üvegcsét találsz.')
            print('Meg tudod kockáztatni, hogy megiszod vagy sem.')
            print('1 >> Beleiszom.')
            print('2 >> Inkább  megyek máshova!')
            cselekves = input('Mit csinálsz?: >> ')
            match cselekves:
                case '1':
                    esely = random.randint(1,2)
                    if esely == 1:
                        print('Kinyitod az üveget')
                        print('Belekortyolsz')
                        print('Jobban érzed magad.')
                        print('A hp-d növekedett 5-el')
                        if hp < 95:
                            hp =+ 5
                        else:
                            hp =+ 0
                        input("\nHa készen álasz nyomd meg az entert!")
                        return 'pince'
                    if esely == 2:
                        print('Kinyitod az üveget')
                        print('Belekortyolsz')
                        print('Rossz érzést érzel majd, hánysz egyet.')
                        print('A hp-d csökkent 10-el')
                        hp =-10 
                        input("\nHa készen álasz nyomd meg az entert!")
                        return 'pince'
                case '2':
                    return 'pince'
        case '4':
            return 'fobejarat'

def folyoso():
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
            return 'konyvtar'
        case '5':
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
            os.system('cls')
            print('Egy labirintushoz érkezel mely egy kódót vár el tőled!')
            kodell = int(input('Mi a kód?: >> '))
            if kodell == 972 and labirintusKod == True:
                os.system('cls')
                print('Gratulálok, sikeresen túlélted és kijutottál a kastélyból')
                input("\nHa készen álasz nyomd meg az entert!")                    
                return 'kijarat'
            else:
                os.system('cls')
                print('Nem jó kód!')
                print('Keresgélj tovább!')
                input("\nHa készen álasz nyomd meg az entert!")
                return 'udvar'        
        case '4':
            return 'folyoso'


def csarnok():
    global kard
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
            print('A papírra az van írva, hogy:')
            print("\x1B[3m" + 'Sajtos - Gyengeség: Italian' + "\x1B[0m")
            input("\nHa készen álasz nyomd meg az entert!")
            return 'csarnok'
        case '2':
            os.system('cls')
            print('A közepéről belátod a csarnok elejét meg a végét')
            print('Az elején látsz valamit ami nem tudod micsoda.')
            print('A végén látsz egy dobozt')
            input("\nHa készen álasz nyomd meg az entert!")
            return 'csarnok'
        case '3':
            os.system('cls')
            print('A csarnok végében találsz egy dobozt.')
            print('Ki akarod nyitni?:')
            print('1 >> igen')
            print('2 >> nem')
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
    os.system('cls')
    print('A könyvtárban vagy.')
    print('A könyvtár a tudás bölcsője.')
    print('Megállít egy barátságosnak tűnő szellem.')
    print('1 >> Le állsz vele beszélni?')
    print('2 >> Vissza mész a folyosóra')
    mitCsinalsz = input('Mit csinálsz?:')
    match mitCsinalsz:
        case '1':
            os.system('cls')
            print('Bemutatkozik neked:')
            print("\x1B[3m" + 'A nevem Sajtos Bálint.' + "\x1B[0m")
            print("\x1B[3m" + 'Ahhoz, hogy tovább haladj le kell győznöd egy sakk mérközésben.' + "\x1B[0m")
            print("\x1B[3m" + 'Vágjunk is bele.' + "\x1B[0m")
            print('1 >> Ruy lopez')
            print('2 >> Four knights')
            print('3 >> Italian game')
            megnyitas = input('Melyik megnyitást hozod?:')
            match megnyitas:
                case '1':
                    os.system('cls')
                    print('A Játszma döntetlennel végződik, nem ér semmi baj, de nem haladhatsz tovább sem.')
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'konyvtar'
                case '2':
                    os.system('cls')
                    print('Ez Sajtos kedvenc megnyitása.')
                    print('Vesztettél!')
                    print('Mivel csúnyán el alázott ezért -20 hp')
                    hp =- 20
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'konyvtar'
                case '3':
                    os.system('cls')
                    print('Jól választottál, megnyerted a játékot')
                    print('A nyereményed + 5 hp')
                    hp =+ 5
                    input("\nHa készen álasz nyomd meg az entert!")
                    return 'konyvtarTeljesitett'
        case '2':
            return 'folyoso'

def konyvtarTeljesitett():
    os.system('cls')
    print('A  győzelmed után a könyvtárból több felé is haladhatsz')
    print('1 >> galéria')
    print('2 >> iroda')
    print('3 >> Vissza a folyosóra, de vigyázz ha vissza akarsz jönni a könyvtárba újra meg kell küzdeni Sajtossal.')

    v = input('Merre haladsz tovább?: >> ')
    match v:
        case '1':
            return 'galeria'
        case '2':
            return 'iroda'
        case '3':
            return 'folyoso'
        
def galeria():
    print('Megérkeztél a galériába')
    print('1 >> lépcsőház')
    print('2 >> iroda')
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
    print('Megérkeztél az irodába ')
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
        case 'konyvtar':
            hely = konyvtar()
        case 'konyvtarTeljesitett':
            hely = konyvtarTeljesitett()