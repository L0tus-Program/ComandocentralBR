import tkinter as tk
from typing import Text
import whois
import os
import pyautogui as gui # posteriormente vou trocar todas as telas do pyautogui para usar o tkinter diretamente
import webbrowser

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets() # chama função para criar elementos na tela
        



    def create_widgets(self):
        # botão inicial de teste do servidor de emails
        self.home = tk.Button(self, fg="black", bg="grey", height=3,width=9)
        self.home["text"] = "Testar email"
        self.home.pack(side="left")
        self.home["command"] = self.testeEmail

        self.freearea = tk.Text(self,fg="green",width=30, height=10)
        self.freearea.pack(side="bottom")
        # botão para teste whois
        self.whois = tk.Button(self, fg="brown", text="Who" ,command=self.mainwho, height=3)
        self.whois.pack(side='left')

        # botão para sair do programa
        self.quit = tk.Button(self,text='QUIT', fg="black", bg="red", command=self.master.destroy, height=3)
        self.quit.pack(side="right")

        #botão para abrir o portal interno da Brasil (felipe/)
        self.interno = tk.Button(self, text="Portal interno", command=lambda: webbrowser.open_new_tab('http://felipe'), height=3)
        self.interno.pack(side='left')


    def testeEmail(self): #função de teste de email
        dom = "email-ssl.com.br"
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
            gui.alert("Teste encerrado")



    def mainwho (self): # função de whois e ping
        #self.quit['text']= "EXIT"
        dom = gui.prompt("Insira o domínio para realizar o Whois")
        w = whois.whois(dom) # whois aplicado ao domínio
        varping = None
        print("Whois sendo aplicado no domínio ", dom)
        gui.alert(w,"Resultado Whois")
        ping = gui.confirm(text='Deseja realizar um ping (teste de conexão) em '+dom+" ?", title='Ping', buttons=['Sim', 'Não'])
        if ping == "Sim":
            varping = os.system("ping " + dom) #ping realizado pelo OS no domínio recebe
            if varping == 0:
                gui.alert("Servidor pingado com sucesso","Resultado ping")
            else:
                gui.alert("Servidor falhou no ping","Resultado ping")
        else:
            gui.alert("Teste encerrado")






# create the application
myapp = App()
#
# here are method calls to the window manager class
#
myapp.master.title("Comand Line Brasil")
myapp.master.maxsize(600, 1000)
myapp.master.minsize(300,850)
# start the program
myapp.mainloop()