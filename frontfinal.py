from tkinter import *
from PIL import Image, ImageTk
from typing import Sized, Text
import whois
import subprocess
import os
# posteriormente vou trocar todas as telas do pyautogui para usar o tkinter diretamente
import pyautogui as gui
import webbrowser  # usei para abrir páginas no navegador do usuario
import functions as f
import modais
import threading

root = Tk()
root.title("Auto atendimento Brasil dos Parafusos")
# root.minsize(600,100)
root.geometry('1000x800')


img = Image.open('brasil.png')

# Cria uma label para exibir a imagem
label_img = Label(root)
label_img.pack(fill=BOTH, expand=YES)

# Função para redimensionar a imagem


def resize_image(event):
    global img
    # Obtém o novo tamanho da janela
    width, height = event.width, event.height
    # Redimensiona a imagem
    img = img.resize((width, height))
    # Atualiza a imagem exibida na label
    photo = ImageTk.PhotoImage(img)
    label_img.config(image=photo)
    label_img.image = photo  # Previne garbage collection


# Associa a função ao evento <Configure> da janela
root.bind('<Configure>', resize_image)

# Exibe a imagem inicialmente
photo = ImageTk.PhotoImage(img)
label_img.config(image=photo)
label_img.image = photo


# usa a classe Menu do tkinter e direciona a janela root
menu_bar = Menu(root, font=("Arial", 300))

# Cria o menu "Soluções"
solutions_menu = Menu(menu_bar, tearoff=False)

# solutions_menu.add_command(label="Abrir", command=lambda: print("Abrir"))
solutions_menu.add_command(label="Testar e-mail",
                           command=lambda: print("Siger travado"))
solutions_menu.add_command(
    label="Scannow", command=lambda: f.scannow())
solutions_menu.add_command(
    label="CHKDSK", command=lambda: f.chkdsk())
solutions_menu.add_command(label="Whois", command=lambda: print("Abrir"))
solutions_menu.add_command(label="Portal Interno",
                           command=lambda: webbrowser.open_new_tab('https://interno.brasildosparafusos.com.br'))
solutions_menu.add_command(label="Abrir chamado",
                           command=lambda: webbrowser.open_new_tab(
                               'https://formulario-ticket.milvus.com.br/home/e9d41bd4413eba979dc58bca3d094b3908760324a02a114eacf14cefe0dd670345f6a5abe7c38fe2275511244f9e2494aaae379c169296fa0b01822505b3f52233679f365de5ed94e56095a0d2b4be46b79ddf7ce5'))
solutions_menu.add_command(label="Planilha de Pedidos",
                           command=lambda: webbrowser.open_new_tab(
                               'https://brasildosparafusos365-my.sharepoint.com/:x:/g/personal/jeferson_brasildosparafusos365_onmicrosoft_com/EVIksprOcNZBghlk9_ABinIBhSGcumcxOR4ZaRbbqiGiVA?rtime=mB_4KyU820g'))
solutions_menu.add_command(label="SIGER travado",
                           command=lambda: f.sigertravado())
solutions_menu.add_command(label="Instalar SIGER",
                           command=lambda: f.installsiger())
solutions_menu.add_command(label="Spooler", command=lambda: f.spooler())
solutions_menu.add_command(label="Outlook travado",
                           command=lambda: f.outlooktravado())


# Cria o menu "Manuais"
manuais_menu = Menu(menu_bar, tearoff=0)
manuais_menu.add_command(label="Treinamento SIGER")
manuais_menu.add_command(label="Treinamento da expedição")
manuais_menu.add_command(label="Manual Oficial SIGER")
manuais_menu.add_command(label="Acessar manual básico do SIGER pelo próprio sistema")



# Cria o submenu pedidos / NF
submenu_pedidos = Menu(manuais_menu, tearoff=0)
submenu_pedidos.add_command(label="Consultar / reenviar NF já faturada", command=modais.nf_faturada)
submenu_pedidos.add_command(label="Tirar saldo de pedido parcialmente faturado")
submenu_pedidos.add_command(label="Emitir pedido interno", command=modais.nf_faturada)
submenu_pedidos.add_command(label="Cancelar separação de pedido", command=modais.nf_faturada)
submenu_pedidos.add_command(label="Emitir NF de cupom fiscal", command=modais.nf_faturada)
submenu_pedidos.add_command(label="Consultar NFE no Sefaz", command=modais.nf_faturada)

#submenu cadastros
submenu_cadastros = Menu(manuais_menu, tearoff=0)
submenu_cadastros.add_command(label="Como cadastrar produtos", command=lambda: webbrowser.open_new(
    'https://interno.brasildosparafusos.com.br/arquivos/manuais/cadastrodeproduto.pdf'))

#cria botões do submenu primeiro - RELATORIOS
submenu_relatorios = Menu(manuais_menu,tearoff=0)
submenu_relatorios.add_command(
    label=" Relatórios de venda por clientes ou produtos (listagem de pedidos faturados)")
submenu_relatorios.add_command(
    label=" Relatórios de venda por clientes ou produtos (listagem de saida de produtos)")



# Adiciona os submenus ao menu Manuais, vinculando aos botoes de submenu
manuais_menu.add_cascade(label="Pedidos / NF", menu=submenu_pedidos)
manuais_menu.add_cascade(label="Cadastros", menu=submenu_cadastros)
manuais_menu.add_cascade(label="Relatórios", menu=submenu_relatorios)

# cria menu suporte
suporte_menu= Menu(menu_bar, tearoff=0)
# adiciona botoes ao menu suporte 
suporte_menu.add_command(label="Download Team Viewer", command=lambda: webbrowser.open_new(
    'https://www.rech.com.br/download/suporte-remoto'))
suporte_menu.add_command(label="Download Anydesk", command=lambda: webbrowser.open_new(
    'https://anydesk.com/pt'))
suporte_menu.add_command(label="Download Skype", command=lambda: webbrowser.open_new(
    'http://www.skype.com/pt-br/download-skype/skype-for-computer/'))
suporte_menu.add_command(label="Contatos RECH", command=lambda: webbrowser.open_new(
    'https://interno.brasildosparafusos.com.br/contatosrech.html'))
suporte_menu.add_command(label="Nettcom", command=lambda: webbrowser.open_new(
    'https://nettcom.com.br/'))

# cria o menu slas
slas_menu= Menu(menu_bar,tearoff=0)
# adiciona botoes ao menu slas
slas_menu.add_command(label="O que é um SLA ?")
slas_menu.add_command(label="SLA Financeiro")
slas_menu.add_command(label="Sla TI")
slas_menu.add_command(label="SLA Coleta de Parafusos")

# cria o menu pessoas
pessoas_menu = Menu(menu_bar, tearoff=0)
# adiciona botoes ao menu pessoas
pessoas_menu.add_command(label="E-mails")

# cria o botao outros
outros_menu = Menu(menu_bar, tearoff=0)
# adiciona botoes ao menu outros
outros_menu.add_command(label="Enviar sugestão de melhoria para o portal")
outros_menu.add_command(label="Controle do SIGER MOBILE")
outros_menu.add_command(label="Sefaz fora do ar ?")
outros_menu.add_command(label="Senhas da WIFI")
outros_menu.add_command(label="Refrigeração Pampa (Ar condicionado) E-mail")
outros_menu.add_command(label="Refrigeração Pampa (Ar condicionado) Dados de contato")



# cria o menu ramais
ramais_menu = Menu(menu_bar, tearoff=0)
# adiciona botoes ao menu ramais
ramais_menu.add_command(label="Ramal Comercial")
ramais_menu.add_command(label="Ramal Estoque")
ramais_menu.add_command(label="Ramal Administrativo/TI")


# Adiciona os menus principais à barra de menu
menu_bar.add_cascade(label="Soluções", menu=solutions_menu)
menu_bar.add_cascade(label="Manuais e instruções", menu=manuais_menu)
menu_bar.add_cascade(label="Suporte", menu=suporte_menu)
menu_bar.add_cascade(label="SLAs",menu=slas_menu)
menu_bar.add_cascade(label="Pessoas", menu=pessoas_menu)
menu_bar.add_cascade(label="Outros", menu=outros_menu)
menu_bar.add_cascade(label="Ramais", menu=ramais_menu)




# Define o estilo para o botão "Abrir"
# solutions_menu.entryconfig(0, font=("Arial", 12), foreground="red")
def on_close():
    global thread 
    thread = False
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.config(menu=menu_bar)
# booleana de controle da thread
global thread
thread = True
t = threading.Thread(target=lambda: f.test_server(thread))
t.start()
root.mainloop()


