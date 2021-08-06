import os
import pyautogui as gui # posteriormente vou trocar todas as telas do pyautogui para usar o tkinter diretamente
import webbrowser

dom = "187.45.193.172"
control = 0
while control <1000 :
    varping = os.system("ping -n 1 " + dom) #parametro -n me permite escolher quantas vezes o servidor sera pingado nesse comando 
    control+=1

print("Terminou")

