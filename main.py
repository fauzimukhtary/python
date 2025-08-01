import time
from mysql.connector import errors
import zeelibrary as zee
from zeelibrary import slprt
import garyprogram
import tempconv


def importmarket():
    try:
        import market
        market.start()
    except errors.InterfaceError:
        return False

def mainmenu():
    slprt("\nWelcome to Main Menu ZEE Program!\n\nPilihlah salah satu program ini:\n\n1) Finding Gary Game\n2) ZEE Market\n3) Temperature Converter\n4) Keluar\n", 0.015)
    while True:
        try:
            useroption = int(input("\nSelect Your Program: "))
            if useroption == 1:
                garyprogram.start()
                break
            elif useroption == 2:
                if not importmarket():
                    slprt('\nMarket sedang offline! Kamu akan diarahkan kembali ke Main Menu... \n', 0.015)           
                    time.sleep(3)
                    mainmenu()
            elif useroption == 3:
                tempconv.start()
                break
            elif useroption == 4:
                zee.exitprogram()
                exit()
            else:
                slprt("\nInvalid!\n", 0.015)
        except ValueError:
            slprt("\nInvalid!\n", 0.015)

if __name__ == "__main__":
    zee.hellopc(0.005)
    mainmenu()