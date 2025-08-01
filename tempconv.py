import time
import main
import zeelibrary
from zeelibrary import slprt

temp = zeelibrary.TempConv()

def start():
    if __name__ == '__main__':
        zeelibrary.hellopc()
    slprt('\nSelamat datang di ZEETempConv!\n', 0.015)
    
    def celc():
        while True:
            try:
                slprt('\nSilakan masukkan suhu dalam °C = ', 0.015)
                value = input()
                if not value:
                    slprt('\nTidak boleh kosong!\n', 0.015)
                else:
                    value = float(value)  
                    temp.celc(value)
                    return
            except ValueError:
                slprt('\nHanya Masukkan Angka!\n', 0.015)
    
    def fahr():
        while True:
            try:
                slprt('\nSilakan masukkan suhu dalam °F = ', 0.015)
                value = input()
                if not value:
                    slprt('\nTidak boleh kosong!\n', 0.015)
                else:
                    value = float(value)  
                    temp.fahr(value)
                    return
            except ValueError:
                slprt('\nHanya Masukkan Angka!\n', 0.015)
            
    def rank():
        while True:
            try:
                slprt('\nSilakan masukkan suhu dalam °R = ', 0.015)
                value = input()
                if not value:
                    slprt('\nTidak boleh kosong!\n', 0.015)
                else:
                    value = float(value)  
                    temp.rank(value)
                    return
            except ValueError:
                slprt('\nHanya Masukkan Angka!\n', 0.015)
    
    def reau():
        while True:
            try:
                slprt('\nSilakan masukkan suhu dalam °Re = ', 0.015)
                value = input()
                if not value:
                    slprt('\nTidak boleh kosong!\n', 0.015)
                else:
                    value = float(value)  
                    temp.reau(value)
                    return
            except ValueError:
                slprt('\nHanya Masukkan Angka!\n', 0.015)
    
    def kelv():
        while True:
            try:
                slprt('\nSilakan masukkan suhu dalam K = ', 0.015)
                value = input()
                if not value:
                    slprt('\nTidak boleh kosong!\n', 0.015)
                else:
                    value = float(value)  
                    temp.kelv(value)
                    return
            except ValueError:
                slprt('\nHanya Masukkan Angka!\n', 0.015)

    def proceed():
        slprt('\nSilakan pilih suhu yang akan dikonversi:\n\n1. Celcius\n2. Fahrenheit\n3. Rankine\n4. Réaumur\n5. Kelvin\n', 0.015)
        while True:
            ans = input('\nPilihan anda: ')
            if not ans:
                slprt('\nTidak boleh kosong!\n', 0.015)
            else:
                try:
                    ans = int(ans)
                    if ans == 1:
                        celc()
                        return False
                    elif ans == 2:
                        fahr()
                        return False
                    elif ans == 3:
                        rank()
                        return False
                    elif ans == 4:
                        reau()
                        return False
                    elif ans == 5:
                        kelv()
                        return False
                    else:
                        slprt('\nIsikan antara 1-5 saja!\n', 0.015)
                except ValueError:
                    slprt('\nHanya isi angka!\n', 0.015)
    
    def restart():
        while True:
            slprt('\nRestart Program? Y/N = ', 0.015)
            ans = input().lower()
            if not ans:
                slprt('\nInvalid!\n', 0.015)
            else:
                if ans == 'y':
                    proceed()
                elif ans == 'n':
                    return False
                else:
                    slprt('\nInvalid!\n', 0.015)

    while True:
        proceed()
        if not restart():
            slprt('\nKamu akan diarahkan kembali ke ZEE Main Menu...\n', 0.015)
            time.sleep(3)
            if not __name__ == '__main__':
                main.mainmenu()
            break

if __name__ == "__main__":
    start()