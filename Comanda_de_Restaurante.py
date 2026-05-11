import customtkinter as ctk
from tkinter import messagebox
ctk.set_appearance_mode('dark')

# FUNCÃO PARA CALCULAR O VALOR TOTAL DA COMANDA
def calcular_comanda():
    try:
        valor_consumido = float(entry_consumido.get())
        quantidade_pessoas = int(entry_pessoas.get())
        
        valor_consumido_total = valor_consumido * 1.10
        valor_comanda = valor_consumido_total
        valor_individual = valor_comanda / quantidade_pessoas
        
        resultado_text = f'Valor total da comanda: R$ {valor_comanda:.2f}\nValor individual por pessoa: R$ {valor_individual:.2f}'
        label_resultado.configure(text=resultado_text)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para o consumo e a quantidade de pessoas.")
        
# INICIO DA JANELA DE INTERFACE
janela_comanda = ctk.CTk()
janela_comanda.geometry('600x400')
janela_comanda.title('Comanda de Restaurante')

# CONFIGURANDO ELEMENTOS NA JANELA
ctk.CTkLabel(janela_comanda,
             text='Comanda de Restaurante',
             text_color='White',
             font=('Arial', 45)).pack(pady=20)

# BLOCO DE ESCRITA DO VALOR CONSUMIDO
ctk.CTkLabel(janela_comanda, text='Valor Consumido (R$):').pack()
entry_consumido = ctk.CTkEntry(janela_comanda,
                            width=450,
                            height=30,
                            placeholder_text='Digite o valor consumido',
                            border_width=2,
                            border_color='blue')
entry_consumido.pack(pady=10)

# BLOCO DE ESCRITA DA QUANTIDADE DE PESSOAS
ctk.CTkLabel(janela_comanda, text='Quantidade de Pessoas:').pack()
entry_pessoas = ctk.CTkEntry(janela_comanda,
                            width=450,
                            height=30,
                            placeholder_text='Digite a quantidade de pessoas',
                            border_width=2,
                            border_color='blue')
entry_pessoas.pack(pady=10)

# BOTÃO PARA CALCULAR A COMANDA
ctk.CTkButton(janela_comanda,
              text='Calcular Comanda',
              command=calcular_comanda,
              fg_color='blue',
              text_color='white',
              height=40).pack(pady=10)

label_resultado = ctk.CTkLabel(janela_comanda, text='', font=('Arial', 16, 'bold'))
label_resultado.pack(pady=10)

janela_comanda.mainloop()