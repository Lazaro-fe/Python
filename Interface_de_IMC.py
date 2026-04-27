import customtkinter as ctk
from tkinter import messagebox
ctk.set_appearance_mode('white')

# CALCULO DE IMC
def calculo_imc():
    try:
        
        peso = float(peso.get())
        altura = float(altura.get())
        
        