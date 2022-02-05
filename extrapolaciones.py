#Coded by $ix
import random
import time
import os
import requests
import json
from colorama import *
init()
def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clean()
print(Fore.CYAN + """  
  ██████  ██▓ ██▓    ▓█████  ███▄    █ ▄▄▄█████▓
▒██    ▒ ▓██▒▓██▒    ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒
░ ▓██▄   ▒██▒▒██░    ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░
  ▒   ██▒░██░▒██░    ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
▒██████▒▒░██░░██████▒░▒████▒▒██░   ▓██░  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░░▓  ░ ▒░▓  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   
░ ░▒  ░ ░ ▒ ░░ ░ ▒  ░ ░ ░  ░░ ░░   ░ ▒░    ░    
░  ░  ░   ▒ ░  ░ ░      ░      ░   ░ ░   ░      
      ░   ░      ░  ░   ░  ░         ░          
                                                """)
def namso():
    print(f"""hay un 50% de que no funcione!""")
    a = str(input("Ingresa tu bin: "))
    año = "34567"
    if len(a) == 16:
        count = int(input("Ingresa la cantidad de CCS a generar:"))
        clean()
        print("¡Generados!")
        b = 1
        while b <= count:
            cc = ""
            for i in range(16):
                if a[i] == "1" or a[i] == "2" or a[i] == "3" or a[i] == "4" or a[i] == "5" or a[i] == "6" or a[i] == "7" or a[i] == "8" or a[i] == "9":
                    cc += a[i]
                elif a[i] == "x" or a[i] == "X":
                    cc += random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
                ++i
            cc += "|" + random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]) + "|" + "202" + año[random.randint(0, 4)] + "|" + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
            print(cc)
            b += 1
    else:
        for i in range(16):
            if len(a) <= 16:
                a += "x"
        count = int(input("Ingresa la cantidad de CCS a generar:"))
        b = 1
        clean()
        print("¡Generados!")
        while b <= count:
            cc = ""
            for i in range(16):
                if a[i] == "1" or a[i] == "2" or a[i] == "3" or a[i] == "4" or a[i] == "5" or a[i] == "6" or a[i] == "7" or a[i] == "8" or a[i] == "9":
                    cc += a[i]
                elif a[i] == "x" or a[i] == "X":
                    cc += random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
                ++i
            cc += "|" + random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]) + "|" + "202" + año[random.randint(0, 4)] + "|" + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
            print(cc)
            b += 1
def similitud():
    cc_final = ""
    one = str((input("Ingresa la primera cc: ")))
    two = str((input("Ingresa la segunda cc: ")))
    clean()
    print("¡Generados!")
    if len(one) == 16 and len(two) == 16:
        for i in range(7):
            cc_final += one[i]
            ++i  
        for i in range(16):
            if i >= 7:
                if one[i] == two[i]:
                    cc_final += one[i]
                else:
                    cc_final += "x"
                ++i
        print(Fore.GREEN + "[+]" + Fore.WHITE + cc_final)
    else:
        print("Tarjeta mal puesta..")

def identacion():
    cc_final = ""
    one = str((input("Ingresa la primera cc: ")))
    if len(one) == 16:
        clean()
        print("¡Generados!")
        for i in range(6):
            cc_final += one[i]
            ++i
                #7, 10, 11, 14
        for i in range(16):
            if i >= 6:
                if i == 7 or i == 10 or i == 11 or i == 14:
                    cc_final += "x"
                else:
                    cc_final += one[i]
            ++i
        print(Fore.GREEN + "[+]" + Fore.WHITE + cc_final)
    else:
        print("Tarjeta mal puesta..")

def cc_generator():
    clean()
    a = int(input("Ingresa el numero de CCS a generar: "))  
    cc = ""
    b = 1
    año = "34567"
    clean()
    print("¡Generados!")
    while b <= a:
        for i in range(16):
            if i == 0:
                cc += random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
            else:
                cc += random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        cc += "|" + random.choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]) + "|" + "202" + año[random.randint(0, 4)] + "|" + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) + random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        print(Fore.GREEN + "[+]" + Fore.RED + " => " + Fore.WHITE + cc)
        b += 1
        cc = ""
def info_bin():
    clean()
    a = input("Ingresa tu bin: " + Fore.RED + "")
    clean()
    print(Fore.CYAN + "Info Del Bin => " + Fore.RED + a)
    try:
        data = requests.get(f"https://lookup.binlist.net/{a}").json()
        print(Fore.GREEN + "[+]" + Fore.WHITE + " Pais => " + data["country"]["name"])
        time.sleep(0.7)
        print(Fore.GREEN + "[+]" + Fore.WHITE + " Tipo => " + data["scheme"] + data["type"])
        time.sleep(0.7)
        print(Fore.GREEN + "[+]" + Fore.WHITE + " Banco => " + data["bank"]["name"] + " - " + data["bank"]["city"])
    except:
        print("Ha ocurrido un error...")

def basic():
    clean()
    a = input(Fore.CYAN + "Ingresa tu CC: ")
    cc_final = ""
    if len(a) == 16:
        for i in range(16):
            if i >= 10:
                cc_final += "x"
            else:
                cc_final += a[i]
            ++i 
        print("Aqui esta tu bin extrapolado: " + cc_final)
    else:
        print("Ha ocurrido un Error.")
print(Fore.CYAN + "1: Generador De CC A Base De Bins.")
print(Fore.CYAN + "2: Extrapolacion De Tipo Basica")
print(Fore.CYAN + "3: Extrapolacion De Tipo Similitud.")
print(Fore.CYAN + "4: Extrapolacion De Tipo identacion.")
print(Fore.CYAN + "5: Generador De CCS Aleatorias.")
print(Fore.CYAN + "6: Informacion De Bin.")
eleccion = int(input(Fore.CYAN + "Elige una ==>: "))
if eleccion == 1:
    namso()
elif eleccion == 2:
    basic()
elif eleccion == 3:
    similitud()
elif eleccion == 4:
    identacion()
elif eleccion == 5:
    cc_generator()
elif eleccion == 6:
    info_bin()