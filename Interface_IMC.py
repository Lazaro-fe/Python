import customtkinter as ctk
from tkinter import messagebox
ctk.set_appearance_mode('white')

# INICIO DE JANELA DE CALCÚLO DE IMC

janela_IMC = ctk.CTk("Gray")
janela_IMC.geometry('600X400')
janela_IMC.title('CTK')

# CALCULO DE IMC
def calculo_de_IMC():
    try:

        valor_peso = float(peso.get())
        valor_altura = float(altura.get())

        calculo_de_altura = altura * altura
        calculo_final_de_imc = peso / calculo_de_altura

        if(calculo_final_de_imc < 18.5):
            classificação

# ELEMENTOS DENTRO DA JANELA

ctk.CTkLabel(janela_IMC,
             text='Calculadora de IMC',
             text_color='Blue',
             font=('Arial', 45)).pack(pady=20)

# BLOCO DE ESCRITA DO PESO
peso = ctk.CTKEntry(janela_IMC,
                    width=450,
                    height = 30,
                    placeholder_text= 'Digite seu peso em kg: ',
                    border_width=2,
                    border_color='Gray')

peso.pack(pady=10)

altura = ctk.CTkEntry(janela_IMC,
                      width=450,
                      height=30,
                      placeholder_text='Digite a sua altura em metros: ',
                      border_width=2,
                      border_color='gray')

