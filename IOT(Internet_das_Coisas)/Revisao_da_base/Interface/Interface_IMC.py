import customtkinter as ctk
from tkinter import messagebox
ctk.set_appearance_mode('white')

# INICIO DE JANELA DE CALCÚLO DE IMC

janela_IMC = ctk.CTk("Gray")
janela_IMC.geometry('600x400')
janela_IMC.title('CTK')

# CALCULO DE IMC
def calculo_de_IMC():
    try:

        valor_peso = float(peso.get())
        valor_altura = float(altura.get())

        calculo_final_de_imc = valor_altura / (valor_altura * valor_altura)

        if(calculo_final_de_imc < 18.5):
            classificacao = "Abaixo do Peso"
        elif (18.5 <= calculo_final_de_imc < 24.9):
            classificacao = "Peso Normal"
        elif (25 <= calculo_final_de_imc < 29.9):
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"
        
        label_resultado.valor.configure(text= f"{calculo_final_de_imc:.2f}")
        label_resultado_class.configure(text=classificacao)

    except ValueError:
        messagebox.showerror("Erro de Entrada!", "Por favor!\nTente inserir números válidos!")

# ELEMENTOS DENTRO DA JANELA

# TÍTULO
ctk.CTkLabel(janela_IMC,
             text='Calculadora de IMC',
             text_color='Blue',
             font=('Arial', 45)).pack(pady=20)

# SUBTÍTULO
ctk.CTkLabel(janela_IMC,
            text='Descubra seu índice de massa corporal',
            text_color='gray',
            font=('Arial', 32)).pack(pady=20)

# BLOCO DE ESCRITA DO PESO
peso = ctk.CTkEntry(janela_IMC,
                    width=450,
                    height = 30,
                    placeholder_text= 'Digite seu peso em kg: ',
                    border_width=2,
                    border_color='Gray')

peso.pack(pady=10)

# BLOCO DE ESCRITA DE ALTURA
altura = ctk.CTkEntry(janela_IMC,
                      width=450,
                      height=30,
                      placeholder_text='Digite a sua altura em metros: ',
                      border_width=2,
                      border_color='gray')

altura.pack(pady=10)

# BOTÃO DE CALCULO DE IMC

botao_calcular = ctk.CTkButton(janela_IMC,
                              text= 'Calcular IMC',
                              fg_color= 'blue',
                              text_color= 'white',
                              height= 40,
                              command= calculo_de_IMC)

botao_calcular.pack(pady=10)

# Irá Mudar o '--' para o valor do IMC
label_resultado_valor = ctk.CTkLabel()