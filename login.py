import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image 


root = ctk.CTk()
root.resizable(False, False)
root.title("Pet Pals")
root.state("zoomed")
root.geometry("1920x1080")


# Header da Tela de Cadastro!!
headerframe = ctk.CTkLabel(root, text="PetPal", font=("Arial",20, 'bold'), text_color="black", width=200)
headerframe.place(x=25, y=35)

imgpatacachorro = ("petpals/imagens/patacachorro.png")
img = Image.open(imgpatacachorro)
img = img.resize((20,20))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(root, image=img_tk, text='')
label_img.place(x=70, y=33)

inicio = ctk.CTkLabel(root, text="Inicio", font=('Arial',20, 'bold'), text_color="black")
inicio.place(x=800, y=35)

loja = ctk.CTkLabel(root, text="Loja", font=('Arial',20, 'bold'), text_color="black")
loja.place(x=900, y=35)

sobre = ctk.CTkLabel(root, text="Sobre", font=('Arial',20, 'bold'), text_color="black")
sobre.place(x=1000, y=35)

contato = ctk.CTkLabel(root, text="Contato", font=('Arial',20, 'bold'), text_color="black")
contato.place(x=1100, y=35)

# Imagem de Fundo da Tela de Cadastro!!

imagemfundo = ("petpals/imagens/imgfundo.png")
imgfundo = Image.open(imagemfundo)
tk_fundo = ImageTk.PhotoImage(imgfundo)

root.update()
width_tela = root.winfo_width()

labelfundo = ctk.CTkLabel(root, image=tk_fundo, text='', width=width_tela)
labelfundo.place(x=0, y=100)

root.mainloop()