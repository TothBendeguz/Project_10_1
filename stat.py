if perc < 60 and perc >= 10:
        print(f'{ora}:{perc}')
    elif perc == 60:
        print(f'{ora + 1}:00')
    elif perc < 10:
        print(f'{ora}:0{perc}')
    perc += ora * 60
    perc = perc % 1440
    ora = int(perc / 60)
    perc = perc % 60