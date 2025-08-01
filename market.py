from zeelibrary import slprt
from msvcrt import getch
from services import database
import main

def add():
    while True:
        try:
            slprt('\nKode Barang = ', 0.015)
            code = input().strip()
            slprt('Nama Barang = ', 0.015)
            name = input().strip()
            slprt('Harga Barang = ', 0.015)
            price = input().strip()
            slprt('Stok Barang = ', 0.015)
            stock = input().strip()
            
            if code and name and price and stock:
                price = int(price)
                stock = int(stock)
                database.insert(code, name, price, stock)
                price = format(price, ',d')
                slprt(f'\nBerhasil save dengan kode {code}: {name} Rp{price}; Stok: {stock}\n', 0.015)
                break
            else:
                slprt('\nSalah satu/sebagian tidak boleh kosong!\n', 0.015)

        except ValueError:
            slprt('\nHarga & Stok wajib menggunakan angka!\n', 0.015)

def check():
    items = database.fetch_item()
    slprt('\n****** Daftar Barang ZEE Market ******\n', 0.001)
    for item in items:
        id = item [0]
        code = item[1]
        name = item[2]
        price = item[3]
        stock = item[4]
        slprt(f"\n-- ID [{id}] --\nKode = {code}\nNama Barang = {name} | Rp{price}\nStok = {stock} pcs\n", 0.001)
    slprt('\nPress any key to continue... \n', 0.015)    
    getch()

def start_title():
        slprt("\nSilakan Pilih Menu di bawah:\n\n1. Tambah Barang\n2. List Barang\n3. Kembali\n\n", 0.015)

def start():
    slprt('\nSelamat datang di ZEE Market!\n', 0.015)
    while True:
        start_title()
        try:
            slprt('Pilihan kamu = ', 0.015)
            opt = int(input(""))
            if opt == 1:
                add()
                return start()
            elif opt == 2:
                check()
                return start()
            elif opt == 3:
                if not __name__ == "__main__":
                    main.mainmenu()
                else:
                    exit()
            else:
                slprt('\nInvalid!\n', 0.015)
        except ValueError:
            slprt('\nInvalid!\n', 0.015)

# debug
if __name__ == "__main__":
    start()