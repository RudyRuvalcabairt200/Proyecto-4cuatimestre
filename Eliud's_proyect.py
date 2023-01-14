#              ________________________________________________
#             /                                                \
#            |    _________________________________________     |
#            |   |                                         |    |
#            |   |            PROYECTO 3 UNIDAD            |    |
#            |   |         AUTOMATIZACION DE REDES         |    |
#            |   |                                         |    |
#            |   |      RUDY MALCOM RUVALCABA LOZANO       |    |
#            |   |                                         |    |
#            |   |                                         |    |
#            |   |                   4-A                   |    |
#            |   |                                         |    |
#            |   |                                         |    |
#            |   |                                         |    |
#            |   |                                         |    |
#            |   |                                         |    |
#            |   |_________________________________________|    |
#            |                                                  |
#             \_________________________________________________/
#                    \___________________________________/
#                 ___________________________________________
#              _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
#           _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
#        _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
#     _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
#  _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
# :-------------------------------------------------------------------------:
# `---._.-------------------------------------------------------------._.---'
#A0-8C-FD-22-08-60 javis
#00-08-1D-10-2B-19 zairo
from netmiko import ConnectHandler                    
import re                                             
import json                                           
from time import * 
from tkinter import *
import tkinter
windowmac = tkinter.Tk()
windowmac.geometry("800x600")
windowmac.title("Automatizacion de redes")
#windowmac.iconbitmap("gun.ico")
windowmac.config(cursor="cross")
windowmac.config(bg="white")
#wallpaper = PhotoImage(file="fondo.png")
#fondo = Label(windowmac,image=wallpaper).place(x=0,y=0)


mac_cuadro=StringVar()
ip_cuadro=StringVar()
password_cuadro=StringVar()
password2_cuadro=StringVar()
privilege_cuadro=StringVar()

def enviar (mac_cuadro):
    mamarre8.insert(END,("LA MAC ES:",mac_cuadro))
    mamarre8.insert(END,("\n"))
    

texto = tkinter.Label(windowmac, text= "PROYECTO 3")
mamarre = Label(windowmac,text="ADD MAC OF DEVICE")
mamarre.place(x=60,y=80, width=120, height=20)


def textodecaja():
    text20 = mamarre8.get()
    print(text20)
    
mamarre8 = Entry (windowmac,textvariable=mac_cuadro)
mamarre8.place(x=250,y=80, width=200, height=25)

mamarre = Label(windowmac,text="What's ip address of the switch:")
mamarre.place(x=60,y=160, width=180, height=20)

mamarre8 = Entry(windowmac, bg="gray")
mamarre8.place(x=250,y=160, width=200, height=25)

mamarre = Label(windowmac,text="The username is...")
mamarre.place(x=60,y=240, width=120, height=20)

mamarre8 = Entry(windowmac, bg="gray")
mamarre8.place(x=250,y=240, width=200, height=25)

mamarre = Label(windowmac,text=" unlock switch with privilege:")
mamarre.place(x=60,y=320, width=160, height=20)

mamarre8 = Entry(windowmac, bg="gray")
mamarre8.place(x=250,y=320, width=200, height=25)


mamarre8 = Entry(windowmac, bg="gray")
mamarre8.place(x=500,y=80, width=200, height=300)
Botonsearch=tkinter.Button(windowmac,text="Search", command=lambda:enviar(mac_cuadro.get()))
Botonsearch=tkinter.Button(windowmac,text="Search", command=textodecaja)
Botonsearch.place(x=300,y=400, width=120, height=30)

#fondowindow=PhotoImage(file="pantalla1.jpg")
#fondophoto=Label(windowmac,image=fondowindow).place(x=0,y=0)

#text1=Label(text="ADD MAC OF DEVICE:",font=("Agecy FB",11)).place(x=50,y=100)
#cuadro de texto
#entradax=StringVar()
#boxtext1=Entry(windowmac,entradavariable=entradax).place(x=80,y=100)
Reload = 1
#tittle=input("                   _.------.                        .----.__\n                  /         \_.       ._           /---.__  \ \n                 |  O    O   | \___  //|          /       `\ | \n                 |  .vvvvv.  | )   `(/ |         | o     o  \| \n                 /  |     |  |/      \ |  /|   ./| .vvvvv.  |\n                /   `^^^^^'  / _   _  `|_ ||  / /| |     |  | \ \n              ./  /|         | O)  O   ) \|| //' | `^vvvv'  |/\\ \n              /   / |         \        /  | | ~   \          |  \\ \n              \  /  |        / \ Y   /'   | \     |          |   ~ \n               `'   |  _     |  `._/' |   |  \     7        /\n        _.-'-' `-'-'|  |`-._/   /    \ _ /    .    | \n    __.-'            \  \   .   / \_.  \ -|_/\/ `--.|_\n --'                  \  \ |   /    |  |              `-\n ______                                  _            _____ \n | ___ \                                | |          |____ |\n | |_/ / _ __   ___   _   _   ___   ___ | |_   ___       / /\n |  __/ | '__| / _ \ | | | | / _ \ / __|| __| / _ \      \ \ \n | |    | |   | (_) || |_| ||  __/| (__ | |_ | (_) | .___/ / \n \_|    |_|    \___/  \__, | \___| \___| \__| \___/  \____/ \n                       __/ |                                 \n                      |___/                           \n ")
#support = tkinter(windowmac, textbox = "ADD MAC OF DEVICE:")
support = input ("     ,_  \n     ,'  `\,_   \n     |_,-'_)    \n     /##c '\  ( \n     ' |'  -{.  )\n      /\__-' \[]\n     /`-_`\   \n     '     \    ADD MAC OF DEVICE: ")   
support = support.replace("-","")                   
support = support.lower()                           
DeviceSwitch = input("\n          /\\ \ \n        /     \ \n     |  |-o-o-|\n        C  V  D   \n        | ___ |\n         \___/ \n       _/<|_|>\_\n      / |/\_/\| \ \n     |    |\|    |\n     |    |\|  | |\n     |    |\|  | |\n     \\   |\|  | |    What's ip address of the switch: ")  
nombredeusuario = input("______________\n||            ||\n||            ||\n||            ||\n||____________||\n \\ ############ \\ \n  \\ ############ \\ \n   \      ____    \ \n    \_____\___\____\ \     The username is...: ")                              
passwordevice = input("                _______________________________________________\n             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_\n          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_\n       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_\n    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_\n _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_\n:-----------------------------------------------------------------------------:\n`---._.-----------------------------------------------------------------._.---'      generate you password: ")
devicepassword = input("\n °°°°°°°°°°°°|\ \n °°°°°°°°°°°°|_\ \n °°°°°°°°°°°°|__\ \n °°°°°°°°°°°°|___\ \n °°°°°°°°°°°°|____\°°°°°° \n °°°°°°°°°°°°|_____\°°°°°° \n °°°°°°°°°°°°|______\°°°°°° \n °°°°°°______|_______________ \n ~~~~\____________________/~~~~ \n ,.-~*´¨¯¨`*•~-.¸,.-~*´¨¯¨`*•~-.¸,.-~*´¨¯¨`*•~-.¸,.-~*´¨¯¨`*•~-.¸,.-~* \n ´¨¯¨`*•~-.¸,.-~*´¨¯¨`*•~-.¸,.-~*´¨¯¨`*•~-.¸,.-~*´ `*•~-.¸,.-~*´`*•~-.¸,.-~*´•~-.¸,.-~*´¨¯¨`*•  unlock switch with privilege: ")
fierro1 = {#ssh
    "host": DeviceSwitch,
    "username": nombredeusuario,
    "password": passwordevice,
    "device_type": "cisco_ios",
    "secret": devicepassword,}                                
Connect_Device = ConnectHandler(**fierro1)             
Connect_Device.enable()                               
while Reload==1:
    try:
        showMCneighbords = Connect_Device.send_command("show cdp neighbors detail",use_textfsm = True)
        showMCneighbords = (json.dumps(showMCneighbords, indent = 2)) #vecinos
        showMCneighbords = json.loads(showMCneighbords)
        for switch  in range(len(showMCneighbords)):
            name_sw = (showMCneighbords[switch]["destination_host"])
            ipvmana = (showMCneighbords[switch]["management_ip"]) #datosvecinos
            portoutside = (showMCneighbords[switch]["local_port"])
            try:
                portoutside=list(portoutside)
                portvt="" #portfa
                dellist=("s","t","E","t","h","e","r","n","e","t")
                for lyrics in dellist:
                    portoutside.remove(lyrics)
                for letter in portoutside:
                    portvt+=letter     
            except:
                portoutside=list(portoutside)
                portvt="" #portgi
                dellist=("i","g","a","b","i","t","E","t","h","e","r","n","e","t")
                for lyrics in dellist:
                    portoutside.remove(lyrics)
                for letter in portoutside:
                    portvt+=letter
    except:
        print("No found device switch cdp")
        pass #nocdp
    try:
        showMCtable = Connect_Device.send_command("show mac address-table",use_textfsm = True)
        showMCtable = (json.dumps(showMCtable, indent = 2))
        showMCtable = json.loads(showMCtable) #searchvecinos
        for mac in range(len(showMCtable)) :
            MACaddress = (showMCtable[mac]["destination_address"])
            portMAC = (showMCtable[mac]['destination_port'])#ssdmac
            MAC1= re.compile(r"\w\w\w\w.\w\w\w\w.\w\w\w\w")
            MAC2 = (MAC1.search(MACaddress))
            MAC3 = MAC2.group()#emplyformatmac
            MAC3 = MAC3.replace(".","")
            MAC3 = MAC3.lower()
            showMCtable[mac]["destination_address"] = MAC3
    except:
        print("No found any MAC for search")
    try:
        for mac in range(len(showMCtable)):
            if support == (showMCtable[mac]['destination_address']):
            
                DestMAC = (showMCtable[mac]['destination_address'])
                port = (showMCtable[mac]['destination_port'])[0]
            else:
                pass
        for mac in range(len(showMCtable)):#OBTENCCION PUERTO E IP DEL VECINO-------------|
            localport= (showMCneighbords[mac]["local_port"])#ip obt vecino
            ipaddressh=(showMCneighbords[mac]["management_ip"])
            try:
                if port == localport:
                    print(f"HostConexion {ipaddressh}")
                    fierro1 = {
                        "host": ipaddressh,
                        "username": nombredeusuario,
                        "password": passwordevice,
                        "device_type": "cisco_ios",
                        "secret": devicepassword,}
                    Connect_Device = ConnectHandler(**fierro1)             
                    Connect_Device.enable()
                else:#MACSI
                    showoutputrun = Connect_Device.send_command("show run | include hostname")
                    print(f'''\n
                    Mac of this device: {support}
                    Is connected at device: {port}
                    Switch: {showoutputrun}
                    \n''')
                    Reload=0
                    break
            except:#NOMAC
                print(f'''\n
                Mac of this device: {support}
                not available
                \n''')
                Reload=0
                break
    except:#ERRORMAC
        print("¡ERROR!\n No found conexion MAC")
        
windowmac.mainloop()        