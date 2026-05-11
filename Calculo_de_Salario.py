import customtkinter as ctk 
from tkinter import messagebox
ctk.set_appearance_mode('light')

# CALCULO DE SÁLARIO TOTAL
def calcular_salario_total():
    try:
        nome = str(nome_pessoa.get())
        valor_do_salario_base = float(entry_salario_base.get())
        
        if valor_do_salario_base < 2112.00:
            resultado_text = 'O salário está isento de impostos.\n'
            resultado_text = f'Valor do salário total: R$ {valor_do_salario_base:.2f}'
        elif valor_do_salario_base < 2826.65:
            imposto_sobre_salario = valor_do_salario_base * 0.075
            salario_com_imposto = valor_do_salario_base - imposto_sobre_salario
            resultado_text = f'Valor do salário total: R$ {salario_com_imposto:.2f}'
        else:
            imposto_sobre_salario = valor_do_salario_base * 0.15
            salario_com_imposto = valor_do_salario_base - imposto_sobre_salario
            resultado_text = f'Valor do salário total: R$ {salario_com_imposto:.2f}'
            
        label_resultado.configure(text=resultado_text)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o salário.")

# INICIO DA JANELA DE INTERFACE
janela_de_imposto= ctk.CTk()
janela_de_imposto = ctk.CTk(fg_color= 'Cyan')
janela_de_imposto.geometry('600x400')
janela_de_imposto.title('CTK')

# CONFIGURANDO ELEMENTOS NA JANELA
ctk.CTkLabel(janela_de_imposto,
             text= 'Cálculo de Imposto de Renda',
             text_color='Blue',
             font=('Arial', 45)).pack(pady=20)

# BLOCO DE ESCRITA DO NOME

ctk.CTkLabel(janela_de_imposto, text='NOME :').pack()
nome_pessoa = ctk.CTkEntry(janela_de_imposto,
             width=450,
             height=30,
             placeholder_text = 'Digite seu nome nesse bloco',
             border_width=2,
             border_color='blue')

nome_pessoa.pack(pady=10)

# BLOCO DE ESCRITA DO SALÁRIO

ctk.CTkLabel(janela_de_imposto, text='Salário Bruto (R$):').pack()
entry_salario_base = ctk.CTkEntry(janela_de_imposto,
                            width=450,
                            height= 30,
                            placeholder_text= 'Digite seu salário bruto',
                            border_width= 2,
                            border_color = 'blue')

entry_salario_base.pack(pady=10)

# BOTÃO DO CALCULO DE SALÁRIO

botao_calcular_salario = ctk.CTkButton(janela_de_imposto,
                                       text= 'CALCULAR IMPOSTO',
                                       fg_color= 'blue',
                                       text_color= 'white',
                                       height= 40,
                                       command= calcular_salario_total)

botao_calcular_salario.pack(pady=10)

label_resultado = ctk.CTkLabel(janela_de_imposto, 
                               text='', 
                               font=('Arial', 16, 'bold'))
label_resultado.pack(pady=10)

janela_de_imposto.mainloop()