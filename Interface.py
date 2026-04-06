import customtkinter as ctk
# PRODUZINDO ADAPTAÇÃO DE TEMAS DE UMA JANELA
ctk.set_appearance_mode('dark')

# COMEÇO DE JANELA

janela = ctk.CTk()
# DEFININDO O TAMANHO DA JANELA
janela = ctk.CTk('#964B00')
janela.geometry('600x450')
janela.title('Controle de Acesso')
janela.iconbitmap('padlock.ico')

# AQUI COMEÇA OS ELEMENTOS DENTRO DA JANELA

ctk.CTkLabel(janela, text= 'ACESSO PRIVADO', text_color= 'white', font=('Roboto', 54)).pack(pady=20)

login = ctk.CTkEntry(janela,
                     width=450,
                     height=20,
                     placeholder_text='Digite seu Login',
                     border_width=2,
                     border_color='lightgreen')

login.pack(pady = 10)

senha = ctk.CTkEntry(janela,
                     width=450,
                     height=20,
                     placeholder_text='Digite sua senha',
                     border_width=2,
                     border_color='lightgreen',
                     show = '*')

senha.pack(pady = 10)

botao = ctk.CTkButton(janela,
                      text= 'Acessar',
                      fg_color= 'black',
                      width= 300)

botao.pack(pady = 15)

# INICIE A JANELA WEB
janela.mainloop()