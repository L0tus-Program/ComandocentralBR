import subprocess
import os
import shutil 
# posteriormente vou trocar todas as telas do pyautogui para usar o tkinter diretamente
import pyautogui as gui
import whois
import time
import smtplib
from email.mime.text import MIMEText
from plyer import notification
from tkinter import *
import socket

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





## ----- FUNCOES DE VERIFICAÇÃO DE REDE NO SERVIDOR ----------


def notificacao():
    try:  # constrói e exibe a notificação do lembrete
        notification.notify(
            title="SERVIDOR",
            message="Seu computador não está conectado ao servidor do SIGER, ou apresenta instabilidade. A TI já foi notificada!",
            timeout=10,
        )
    except Exception as e:
        # print(f'Erro notificação {e}' )
        pass


def email_falha():
    username = "felipe@brasildosparafusos.com.br"
    password = "Brasil@01"
    emailDestino = "felipe@brasildosparafusos.com.br"
    computador = socket.gethostname()
    conteudo = f'Servidor não encontrado no ping! {computador}'
    # Criação do objeto MIMEText
    # é necessário codificar o objeto para utf-8 para poder enviar acentos
    msg = MIMEText(conteudo, 'plain', 'utf-8')
    msg['To'] = emailDestino
    msg['From'] = username
    msg['Subject'] = f'Falha no ping de servidor pelo {computador}'

    # Adicionando cabeçalhos de conteúdo
    msg.add_header('Content-Type', 'text/plain; charset=UTF-8')

    # Enviando o e-mail
    with smtplib.SMTP("email-ssl.com.br", 587) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, emailDestino, msg.as_string())

    print("E-mail enviado com sucesso!")


def test_server(thread):
    print("Entrou em test_server")
    # iniciar loop infinito
    while thread == True:
        time.sleep(1)
    # realizar ping no servidor SERVER
        ping = os.system("ping server")
    # analisar retorno do ping
        if ping == 1:
            print("Equipamento não encontrado na rede")
            # em caso de servidor offline, enviar e-mail para felipe@brasildosparafusos.com.br
            email_falha()
            notificacao()
            time.sleep(20)

            # exibir notificação na tela do usuario caso o server esteja offline

        else:
            #print(ping)
            print("Host encontrado")
    
   


