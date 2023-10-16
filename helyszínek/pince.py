import os

def pince():
    os.system('cls')
    print('Megérkeztél a pincébe')
    print('1..Vissza a főbejárathoz')
    print('2..Ha előre nézel látsz egy folyosót')
    print('3..Balra látsz egy nagy csarnokot')
    print('4..Vissza a főbejárathoz')
    v = input('Merre folytatod az utad?')
    return v