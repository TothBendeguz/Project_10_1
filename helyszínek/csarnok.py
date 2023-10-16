import os

def csarnok():
    os.system('cls')
    print('Megérkeztél a csarnokba')
    print('1..Csarnok eleje')
    print('2..csarnok közepe')
    print('3..csarnok vége')
    print('4..Vissza a főbejárathoz')
    v = input('Merre folytatod az utad?')
    return v