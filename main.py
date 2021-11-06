from math import sqrt
import time
import math
import colorama
from colorama import Fore
from colored import fg
import os

zold=fg('green')
print("")
print(Fore.GREEN + " Másodfokú egyenlet kiszámolása levezetéssel")
time.sleep(3)
print(Fore.GREEN + " !!! Példa negatív szám megadására: -7 !!!\n !!! Példa tört szám megadására: 3.4 !!!\n")
time.sleep(3)

def program():
    a = float(input(Fore.WHITE + " --> " + Fore.GREEN + "Add meg az 'a' adatot:" + Fore.LIGHTBLUE_EX + " "))
    b = float(input(Fore.WHITE + " --> " + Fore.GREEN + "Add meg a 'b' adatot:" + Fore.LIGHTBLUE_EX + " "))
    c = float(input(Fore.WHITE + " --> " + Fore.GREEN + "Add meg az 'c' adatot:" + Fore.LIGHTBLUE_EX + " "))

    print(Fore.RED + " .")
    time.sleep(1)
    print(Fore.RED + " .")
    time.sleep(1)
    print(Fore.RED + " .")
    time.sleep(1)

    if b < 0:
        print(Fore.WHITE + " --> " + Fore.YELLOW + "1. lépés: " + Fore.LIGHTBLUE_EX + "{} +/- √{}² - 4 * {} * {} / 2*{}\n".format(b,b,a,c,a))
        time.sleep(2)

        ketszerb = b*b # b²
        masodikszorzas = -4*a*c 
        nevezoszorzas = 2*a

        if masodikszorzas > 0:
            print(Fore.WHITE + " --> " + Fore.YELLOW + "2. lépés: " + Fore.LIGHTBLUE_EX + "{} +/- √{} + {} / {}\n".format(b,ketszerb,masodikszorzas,nevezoszorzas))
            time.sleep(2)
            gyokalattossz = ketszerb + masodikszorzas
            print(Fore.WHITE + " --> " + Fore.YELLOW + "3. lépés: " + Fore.LIGHTBLUE_EX + "{} +/- √{} / {}\n".format(b,gyokalattossz,nevezoszorzas))
        elif masodikszorzas < 0:
            print(Fore.WHITE + " --> " + Fore.YELLOW + "2. lépés: " + Fore.LIGHTBLUE_EX + "{} +/- √{} {} / {}\n".format(b,ketszerb,masodikszorzas,nevezoszorzas))
            time.sleep(2)
            gyokalattossz = ketszerb + (1 * masodikszorzas)
            print(Fore.WHITE + " --> " + Fore.YELLOW + "3. lépés: " + Fore.LIGHTBLUE_EX + "{} +/- √{} / {}\n".format(b,gyokalattossz,nevezoszorzas))
        else:
            print(Fore.RED + " --> Hiba történt <--")
            time.sleep(2)


        if gyokalattossz < 0:
            print(Fore.LIGHTBLUE_EX + " --> Az egyenletnek nincs megoldása <--")
        else:
            gyokszamolas = math.sqrt(gyokalattossz)
            print(Fore.WHITE + " --> " + Fore.YELLOW + "4.1 lépés: " + Fore.LIGHTBLUE_EX + "{} + {} / {}".format(b,gyokszamolas,nevezoszorzas))
            print(Fore.WHITE + " --> " + Fore.YELLOW + "4.2 lépés: " + Fore.LIGHTBLUE_EX + "{} - {} / {}".format(b,gyokszamolas,nevezoszorzas))
            time.sleep(2)

            print(Fore.RED + " .")
            time.sleep(1)
            print(Fore.RED + " .")
            time.sleep(1)
            print(Fore.RED + " .")
            time.sleep(1)

            x1 = (-1 * b + gyokszamolas) / nevezoszorzas
            x2 = (-1 * b - gyokszamolas) / nevezoszorzas
            print(Fore.WHITE + " --> " + Fore.YELLOW + "x1 = " + Fore.LIGHTBLUE_EX + "{0:.2f}\n".format(x1))
            print(Fore.WHITE + " --> " + Fore.YELLOW + "x2 = " + Fore.LIGHTBLUE_EX + "{0:.2f}".format(x2))

    else:
        print(Fore.WHITE + " --> " + Fore.YELLOW + "1. lépés: " + Fore.LIGHTBLUE_EX + "-{} +/- √{}² - 4 * {} * {} / 2*{}\n".format(b,b,a,c,a))
        time.sleep(2)

        ketszerb = b*b # b²
        masodikszorzas = -4*a*c 
        nevezoszorzas = 2*a

        if masodikszorzas > 0:
            print(Fore.WHITE + " --> " + Fore.YELLOW + "2. lépés: " + Fore.LIGHTBLUE_EX + "-{} +/- √{} + {} / {}\n".format(b,ketszerb,masodikszorzas,nevezoszorzas))
            time.sleep(2)
            gyokalattossz = ketszerb + masodikszorzas
            print(Fore.WHITE + " --> " + Fore.YELLOW + "3. lépés: " + Fore.LIGHTBLUE_EX + "-{} +/- √{} / {}\n".format(b,gyokalattossz,nevezoszorzas))
        elif masodikszorzas < 0:
            print(Fore.WHITE + " --> " + Fore.YELLOW + "2. lépés: " + Fore.LIGHTBLUE_EX + "-{} +/- √{} {} / {}\n".format(b,ketszerb,masodikszorzas,nevezoszorzas))
            time.sleep(2)
            gyokalattossz = ketszerb + (1 * masodikszorzas)
            print(Fore.WHITE + " --> " + Fore.YELLOW + "3. lépés: " + Fore.LIGHTBLUE_EX + "-{} +/- √{} / {}\n".format(b,gyokalattossz,nevezoszorzas))
        else:
            print(Fore.RED + " --> Hiba történt <--")
        time.sleep(2)


        if gyokalattossz < 0:
            print(Fore.YELLOW + " --> Az egyenletnek nincs megoldása <--")
        else:
            gyokszamolas = math.sqrt(gyokalattossz)
            print(Fore.WHITE + " --> " + Fore.YELLOW + "4.1 lépés: " + Fore.LIGHTBLUE_EX + "-{} + {} / {}".format(b,gyokszamolas,nevezoszorzas))
            print(Fore.WHITE + " --> " + Fore.YELLOW + "4.2 lépés: " + Fore.LIGHTBLUE_EX + "-{} - {} / {}".format(b,gyokszamolas,nevezoszorzas))
            time.sleep(2)

            print(Fore.RED + " .")
            time.sleep(1)
            print(Fore.RED + " .")
            time.sleep(1)
            print(Fore.RED + " .")
            time.sleep(1)

            x1 = (-1 * b + gyokszamolas) / nevezoszorzas
            x2 = (-1 * b - gyokszamolas) / nevezoszorzas
            print(Fore.WHITE + " --> " + Fore.YELLOW + "x1 = " + Fore.LIGHTBLUE_EX + "{0:.2f}\n".format(x1))
            print(Fore.WHITE + " --> " + Fore.YELLOW + "x2 = " + Fore.LIGHTBLUE_EX + "{0:.2f}".format(x2))    

    print(Fore.RED + "===============================================================================")
    restart = input(Fore.GREEN + " Akarsz megint számolni?" +
                    Fore.YELLOW + " (i / n):" +
                    Fore.LIGHTBLUE_EX + " ")
    if restart == "i":
        program()
    else:
        exit()
program()
