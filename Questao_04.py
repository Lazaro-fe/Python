import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('white')

# FUNÇÃO PARA CALCULAR SITUAÇÃO DO ALUNO
def verificar_aluno():
    try:
        nome = entry_nome.get()
        nota = float(entry_nota.get())
        frequencia = float(entry_frequencia.get())
        
        if nota < 0 or nota > 10 or frequencia < 0 or frequencia > 100:
            messagebox.showerror("Erro", "Nota deve ser 0-10 e frequência 0-100!")
            return
        
        if nota >= 7 and frequencia >= 75:
            status = "Aprovado"
        elif nota < 7:
            status = "Reprovado por nota"
        else:
            status = "Reprovado por frequência"
        
        resultado_text = f"Aluno: {nome}\nNota: {nota:.1f}\nFrequência: {frequencia:.1f}%\nStatus: {status}"
        label_resultado.configure(text=resultado_text)
    
    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos para nota e frequência!")

# JANELA PRINCIPAL
janela = ctk.CTk()
janela.geometry("600x400")
janela.title("Sistema Escolar")

# TÍTULO
ctk.CTkLabel(janela, text="APP ESCOLAR", font=("Arial", 40), text_color="blue").pack(pady=20)

# NOME DO ALUNO
entry_nome = ctk.CTkEntry(janela, width=450, height=30, placeholder_text="Digite o nome do aluno")
entry_nome.pack(pady=10)

# NOTA
entry_nota = ctk.CTkEntry(janela, width=450, height=30, placeholder_text="Digite a nota do aluno (0-10)")
entry_nota.pack(pady=10)

# FREQUÊNCIA
entry_frequencia = ctk.CTkEntry(janela, width=450, height=30, placeholder_text="Digite a frequência (%)")
entry_frequencia.pack(pady=10)

# BOTÃO PARA VERIFICAR
ctk.CTkButton(janela, text="Verificar", fg_color="cyan", text_color="black", width=300, command=verificar_aluno).pack(pady=10)

# LABEL PARA RESULTADO
label_resultado = ctk.CTkLabel(janela, text="", font=("Roboto", 20), text_color="blue")
label_resultado.pack(pady=10)

janela.mainloop()