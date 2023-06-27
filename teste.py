import subprocess
import os
# posteriormente vou trocar todas as telas do pyautogui para usar o tkinter diretamente
import pyautogui as gui
import whois
import shutil
import time 
import smtplib
from email.mime.text import MIMEText
from plyer import notification
from tkinter import *
import socket

def notificacao():
    try:  # constrói e exibe a notificação do lembrete
            notification.notify(
                title="SERVIDOR",
                message= "Seu computador não está conectado ao servidor do SIGER, ou apresenta instabilidade. A TI já foi notificada!",
                timeout=10,
            )
    except Exception as e:
        #print(f'Erro notificação {e}' )
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



def test_server():
    # iniciar loop infinito
    while True:
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
            print(ping)
            print("Host encontrado")

    

   




test_server()