import time
import sys
import socket
import msvcrt

def garywelcome(version = str, delay = float):
    txt1 = (f'\n{'*' * 77}\n{f' Finding Gary  {version} ':*^77}\n{' by Fauzi ':*^77}\n{'*' * 77}\n\nPress any key to continue...')
    for char in txt1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    msvcrt.getch()
    txt2 = f'''\n\n{' Welcome Player! ':*^77}'''
    for char in txt2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

okay = f'\n{' Okay! ':*^77}\n'

garyrating = '''
10 - Outstanding
9  - Excellent
8  - Very Good
7  - Good
6  - Above Average
5  - Average
4  - Below Average
3  - Bad
2  - Very Bad
1  - Extremely Bad

In the scale of 1-10, please give us a rate! [ 1 - 10 ]
'''

garysorry = '''
We are so sorry! What aspect of this game can we improve?

1) Graphics
2) Difficulty
3) Response
4) Syntax Structure
5) Other
'''

def cm_inch(value = float):
    res = value / 2.54
    print(f"{value} cm adalah sebesar {res} inch")
    return

def inch_cm(value = float): 
    res = value * 2.54
    print(f"{value} inch adalah sebesar {res} cm")
    return

def m_ft(value = float):
    res =  value / 0.3048
    print(f"{value} m adalah sebesar {res} ft")

def ft_m(value = float):
    res = value * 0.3048
    print(f"{value} ft adalah sebesar {res} m / {res / 1000} km")
    return

def kmh_kt(value = float):
    res = value / 1.852
    print(f"{value} km/h adalah sebesar {res} knot atau mil laut (nautical miles) per jam [nmi/h]")
    return

def kt_kmh(value = float):
    res = value * 1.852
    print(f"{value} knot atau {value} nmi/h setara dengan {res} km/h")
    return

def mile_km(value = float):
    res = value * 1.609344
    print(f"{value} mil adalah sebesar {res} km")
    return

def km_mile(value = float):
    res = value / 1.609344
    print(f"{value} km adalah sebesar {res} mil")
    return

def filename():
    print(f"NAMA FILE INI ADALAH: {__name__}")
    print(f"Jika di-import maka file ini bernama zeelibrary, jika dalam debugging maka bernama __main__")
    
def hellopc(delay = float):
    pcname = socket.gethostname()
    txt = f'\n{'-':-^77}\n{f' Hello {pcname}! ':-^77}\n{'-':-^77}\n'
    for char in txt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
def helloname(name) -> str:
    print("*" * (len(name) + 6))
    print(f"** {name} **")
    print("*" * (len(name) + 6))
    
def exitprogram():
    print("\nProgram akan Dihentikan...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Program berhasil Dihentikan\n")

def slprt(text = str, delay = float):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        
class TempConv:
    def __init__(self):
        pass
        
    def celc(self, temp = float):
        self.temp = temp
        fahr = round(temp * 9 / 5 + 32, 2)
        rank = round((temp + 273.15) * 9 / 5, 2)
        reau = round(temp * 4 / 5 , 2)
        kelv = round(temp + 273.15, 2)
        slprt(f'\n{temp}°C setara dengan: {fahr}°F; {rank}°R; {reau}°Re; {kelv} K\n', 0.015)
        
    def fahr(self, temp = float):
        self.temp = temp
        celc = round((temp - 32) * 5 / 9, 2)
        rank = round(temp + 459.67, 2)
        reau = round((temp - 32) * 4 / 9 , 2)
        kelv = round((temp - 32) * 5 / 9 + 273.15, 2)
        slprt(f'\n{temp}°F setara dengan: {celc}°C; {rank}°R; {reau}°Re; {kelv} K\n', 0.015)
        
    def rank(self, temp = float):
        self.temp = temp
        fahr = round(temp - 459.67, 2)
        celc = round((temp - 491.67) * 5 / 9, 2)
        reau = round((temp - 491.67) * 4 / 9, 2)
        kelv = round(temp * 5 / 9, 2)
        slprt(f'\n{temp}°R setara dengan: {fahr}°F; {celc}°C; {reau}°Re; {kelv} K\n', 0.015)
        
    def reau(self, temp = float):
        self.temp = temp
        celc = round(temp * 5 / 4 , 2)
        fahr = round(temp * 9 / 4 + 32, 2)
        rank = round((temp * 5 / 4 + 273.15) * 9 / 5, 2)
        kelv = round(temp * 5 / 4 + 273.15, 2)
        slprt(f'\n{temp}°Re setara dengan: {fahr}°F; {rank}°R; {celc}°C; {kelv} K\n', 0.015)
        
    def kelv(self, temp = float):
        self.temp = temp
        celc = round(temp - 273.15, 2)
        fahr = round((temp - 273.15) * 9 / 5 + 32, 2)
        rank = round(temp * 9 / 5, 2)
        reau = round((temp - 273.15) * 4 / 5, 2)
        slprt(f'\n{temp} K setara dengan: {fahr}°F; {rank}°R; {reau}°Re; {celc}°C\n', 0.015)