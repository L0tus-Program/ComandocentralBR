from tkinter import *
from tkinter import font
import webbrowser
# --------- MODAIS ----------


def open_modal():
    def send(i):
        match i:
            case 0:
                print("Sem email")
            case 1:
                webbrowser.open_new_tab(
                    "mailto:fernando@brasildosparafusos.com.br")
            case _:
                print("ERRO WTF")

    # Cria a janela modal
    modal_window = Toplevel() # sem o root entre parenteses, seria necessario apenas se estivesse no mesmo arquivo
    
    modal_window.title("Janela modal")
    modal_window.geometry("400x400")

    # Torna a janela modal
    modal_window.grab_set()

    # Adiciona widgets à janela modal
    label = Label(modal_window, text="Esta é uma janela modal!")
    label.pack(pady=50)

    button = Button(modal_window, text="Enviar e-mail",
                    command=lambda: send(1))
    button.pack(pady=50)

    # Botão para fechar a janela modal
    close_button = Button(modal_window, text="Fechar",
                          command=modal_window.destroy)
    close_button.pack()




def nf_faturada():
    
    title = "Consultar / reenviar NF já faturada"
    message = "Para reenviar ou consultar notas já faturadas, podemos ir para o menu FAT 2-3-G e selecionar a primeira opção.\nAli é só filtrar a nota que queremos e, na parte inferior da tela teremos as opções disponíveis para a nota selecionada."

    # Cria uma nova janela Toplevel
    # sem o root entre parenteses, seria necessario apenas se estivesse no mesmo arquivo
    modal = Toplevel()

    # Configura a janela para parecer um modal
    modal.grab_set()
    modal.transient()

    # Cria um objeto de fonte com negrito e tamanho grande para o título
    title_font = font.Font(family='Helvetica', size=16, weight='bold')

    # Adiciona o título como um Label com a fonte configurada
    title_label = Label(modal, text=title, font=title_font)
    title_label.pack(pady=10)

    # Adiciona o texto como um Label com uma fonte menor
    text_label = Label(modal, text=message, font='Helvetica 12')
    text_label.pack(padx=20, pady=20)

    # Adiciona um botão "Fechar"
    button = Button(modal, text='Fechar', command=modal.destroy)
    button.pack(pady=10)

    # Espera até que o usuário feche a janela modal
    modal.wait_window()
