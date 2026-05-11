import customtkinter as ctk
from tkinter import messagebox
ctk.set_appearance_mode('white')

# CALCULO DE NOTAS
def calculo_de_nota():
    try:
        
        v_nota_1 = float(nota_1.get())
        v_nota_2 = float(nota_2.get())
        v_nota_3 = float(nota_2.get())
        
        valor_da_media_de_notas = (v_nota_1 + v_nota_2 + v_nota_3) / 3
        
        if(valor_da_media_de_notas >= 5):
            resultado_text='Você passou de ano! =)'
            resultado_text=f"Média Final: {valor_da_media_de_notas:.1f}"
        else:
            resultado_text="Você está de recuperação!!"
            resultado_text=f"Média final: {valor_da_media_de_notas:.1f}"
            
        label_resultado.configure(text=resultado_text)
    except ValueError:
        messagebox.showerror('Error: ', 'Valor errado!\nTente Novamente!!')
        
# INÍCIO DA JANELA
janela_escola = ctk.CTk("Brown")
janela_escola.geometry('600x400')
janela_escola.title('CTK')

# ELEMENTOS DENTRO DA JANELA

ctk.CTkLabel(janela_escola,
             text='APP ESCOLAR',
             text_color='Blue',
             font=('Arial', 45)).pack(pady=20)

# BLOCO DE ESCRITA DA 1° UNIDADE
nota_1 = ctk.CTkEntry(janela_escola,
                     width=450,
                     height=30,
                     placeholder_text='Digite a nota da 1° unidade: ',
                     border_width=2,
                     border_color='blue')

nota_1.pack(pady=10)

# BLOCO DE ESCRITA DA 2° UNIDADE
nota_2 = ctk.CTkEntry(janela_escola,
                      width=450,
                      height=30,
                      placeholder_text='Digite a nota da 2° unidade: ',
                      border_width=2,
                      border_color='blue')

nota_2.pack(pady=10)

# BLOCO DE ESCRITA DA 3° UNIDADE
nota_3 = ctk.CTkEntry(janela_escola,
                      width=450,
                      height=30,
                      placeholder_text='Digite a nota da 3° unidade: ',
                      border_width=2,
                      border_color='blue')

nota_3.pack(pady=10)

bota_media = ctk.CTkButton(janela_escola,
                          text='Média Final',
                          fg_color='cyan',
                          text_color='black',
                          width=300,
                          command=calculo_de_nota)

bota_media.pack(pady=10)

# O RESULTADO APARECE NESSE LOCAL

label_resultado = ctk.CTkLabel(janela_escola, 
                               text='',
                               font=('Roboto', 24), 
                               text_color='blue') 

label_resultado.pack(pady=10)

janela_escola.mainloop()