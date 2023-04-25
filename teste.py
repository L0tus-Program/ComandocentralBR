from tkinter import *

# Cria a janela principal
root = Tk()

# Define a geometria da janela com largura 500 e altura 500
root.geometry('500x500')

# Define a imagem de fundo
background_image = PhotoImage(file='brasil.png')

# Cria um label para exibir a imagem de fundo
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Cria os botões
button1 = Button(root, text='Botão 1', width=10)
button2 = Button(root, text='Botão 2', width=10)
button3 = Button(root, text='Botão 3', width=10)

# Posiciona os botões utilizando o gerenciador de layout grid
button1.grid(row=1, column=1, padx=10, pady=10)
button2.grid(row=1, column=2, padx=10, pady=10)
button3.grid(row=1, column=3, padx=10, pady=10)

# Centraliza a linha dos botões
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)

# Posiciona os botões centralizados horizontalmente e verticalmente
button1.place(relx=0.5, rely=0.5, anchor=CENTER)
button2.place(relx=0.5, rely=0.6, anchor=CENTER)
button3.place(relx=0.5, rely=0.7, anchor=CENTER)

# Inicia o loop da interface gráfica
root.mainloop()
