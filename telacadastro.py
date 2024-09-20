import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pywinstyles

def submit_login():
    nome = entry_nomecompleto.get()
    senha = entry_senha.get()
    confirmar_senha = entry_confirmar_senha.get()
    
    if senha != confirmar_senha:
        messagebox.showerror("Erro", "As senhas não coincidem.")
    else:
        messagebox.showinfo("Sucesso", f"Login realizado com sucesso, {nome}!")


root = ctk.CTk()
root.resizable(False, False)
root.title("Pet Pals")
root.state("zoomed")
root.geometry("1920x1080")
root.configure(fg_color="white")

# Header da Tela de Cadastro!!

frame_header = ctk.CTkLabel(root, text="PetPal", font=("Arial",20, 'bold'), text_color="black", width=200)
frame_header.place(x=25, y=35)

imgpatacachorro = ("imagens/patacachorro.png")  # "petpals/imagens/patacachorro.png"
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

imagemfundo = ("imagens/imgfundo.png")  # "petpals/imagens/imgfundo.png."
imgfundo = Image.open(imagemfundo)
tk_fundo = ImageTk.PhotoImage(imgfundo)


## Tela de Login!!

root.update()
width_tela = root.winfo_width()

label_fundo = ctk.CTkLabel(root, image=tk_fundo, text='', width=width_tela)
label_fundo.place(x=0, y=100)

frame_login = ctk.CTkFrame(root, width=380, height=450, fg_color='#F8F9FA', corner_radius=25, bg_color="#ffffff")
frame_login.place(x=820, y=270)
pywinstyles.set_opacity(frame_login, color="#ffffff")

nome_completo = ctk.CTkLabel(frame_login, text="Nome Completo", font=('Arial', 16, 'bold'), text_color='black')
nome_completo.place(x=35, y=50)
entry_nomecompleto = ctk.CTkEntry(frame_login, width=300)
entry_nomecompleto.place(x=35, y=80)

email = ctk.CTkLabel(frame_login, text="Email", font=('Arial', 16, 'bold'), text_color='black')
email.place(x=35, y=110)
entry_email = ctk.CTkEntry(frame_login,width=300)
entry_email.place(x=35, y=140)

senha = ctk.CTkLabel(frame_login, text="Senha", font=('Arial', 16, 'bold'), text_color='black')
senha.place(x=35, y=170)
entry_senha = ctk.CTkEntry(frame_login, show='*', width=300) 
entry_senha.place(x=35, y=200)

confirmar_senha = ctk.CTkLabel(frame_login, text="Confirmar Senha", font=('Arial', 16, 'bold'), text_color='black')
confirmar_senha.place(x=35, y=230)
entry_confirmar_senha = ctk.CTkEntry(frame_login, show='*', width=300)
entry_confirmar_senha.place(x=35, y=260)


check_var = ctk.BooleanVar()
checkbox_termos = ctk.CTkCheckBox(frame_login, text="Li e concordo com os termos de uso", variable=check_var,
 font=("Arial",12, 'bold'), text_color='black')
checkbox_termos.place(x=45, y=300)

check_var_termo2 = ctk.BooleanVar()
checkbox_termo2 = ctk.CTkCheckBox(frame_login, text="Li e concordo com as politicas da empresa", variable=check_var_termo2, font=("Arial",12, 'bold'), text_color='black')
checkbox_termo2.place(x=45, y=330)

botao = ctk.CTkButton(frame_login, text="Cadastrar", font=("Arial",17), command=submit_login, 
                               fg_color="orange", text_color="white",  width=150, height=50)
botao.place(x=120, y=380)

#Rodapé da Tela de Cadastro!!

frame_rodape = ctk.CTkLabel(root, text="PetPal", font=("Arial",20, 'bold'), text_color="black",  width=200)# width=200
frame_rodape.place(x=25, y=950)

imgpatacachorro = ("imagens/patacachorro.png")  # "petpals/imagens/patacachorro.png"
img = Image.open(imgpatacachorro)
img = img.resize((20,20))
img_tk = ImageTk.PhotoImage(img)

root.mainloop()