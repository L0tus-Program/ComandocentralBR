import subprocess
import os
import shutil 
# posteriormente vou trocar todas as telas do pyautogui para usar o tkinter diretamente
import pyautogui as gui
import whois
import shutil 

def scannow():
    subprocess.call("start bats\sfcscannow.bat", shell=True)


def chkdsk():
    subprocess.call("start bats\chkdsk.bat", shell=True)


def outlooktravado():
        #print("chamando outlook travado")
    subprocess.call("start bats\outlooktravado.bat", shell=True)


def sigertravado():
    subprocess.call("start bats\sigertravado.bat", shell=True)


def testeEmail():  # função de teste de email
    dom = "email-ssl.com.br"
    w = whois.whois(dom)  # whois aplicado ao domínio
    varping = None
     # exibe a saida do whois dentro da propria aplicação
    gui.alert(w)
      # print("Whois sendo aplicado no domínio", dom)
      # gui.alert(w,"Resultado Whois")
    ping = gui.confirm(text='Deseja realizar um ping no ' +
                          dom+" ?", title='Ping', buttons=['Sim', 'Não'])
    if ping == "Sim":
        # ping realizado pelo OS no domínio recebe
        varping = os.system("ping " + dom)
        if varping == 0:
            gui.alert("Servidor pingado com sucesso", "Resultado ping")
        else:
            gui.alert("Servidor falhou no ping", "Resultado ping")
    else:
        gui.alert("Teste encerrado")


def spooler():
       
    subprocess.call("start bats\spooler.bat", shell=True)



def installsiger():
    print("Deletando siger no disco C")
    os.system("RD /S /Q C:\RECH")

    print("Buscando/deletando SIGER no disco D")
    os.system("RD /S /Q D:\RECH")

    print("Instalando siger")
    origem = 'SIGER.lnk'
   
    destino = os.path.expanduser("~\OneDrive - Brasil dos Parafusos\Área de Trabalho")
    print('Printando o destino ' + destino)
    shutil.copy(origem, destino)



    os.system(f'cd {destino} & start SIGER.lnk')




