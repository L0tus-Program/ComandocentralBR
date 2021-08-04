import whois
import os
import pyautogui as gui
import tkinter
from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog as fd #Janela pra abrir arquivo


#filename = fd.askopenfilename()



def mainwho ():
    dom = gui.prompt("Insira o domínio para realizar o Whois")
    w = whois.whois(dom) # whois aplicado ao domínio
    varping = None
    print("Whois sendo aplicado no domínio", dom)
    gui.alert(w,"Resultado Whois")
    ping = gui.confirm(text='Deseja realizar um ping no'+dom+"?", title='Ping', buttons=['Sim', 'Não'])
    if ping == "Sim":
        varping = os.system("ping " + dom) #ping realizado pelo OS no domínio recebe
        if varping == 0:
            gui.alert("Servidor pingado com sucesso","Resultado ping")
        else:
            gui.alert("Servidor falhou no ping","Resultado ping")
    else:
        gui.alert("Programa encerrado")









# https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/

