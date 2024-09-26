import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pywinstyles

def submit_login():
    nome = entry_nomecompleto.get()
    email = entry_email.get().strip()
    senha = entry_senha.get()
    confirmar_senha = entry_confirmar_senha.get()

    if not nome or not email or not senha or not confirmar_senha:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    if senha != confirmar_senha:
        messagebox.showerror("Erro", "As senhas não coincidem.")
        return

    if email in usuarios_existentes:
        messagebox.showerror("Erro", "Usuário já cadastrado.")
        return
    
    if not check_var.get() or not check_var_termo2.get():
        messagebox.showerror("Erro", "Você deve aceitar os termos de uso e as políticas da empresa.")
        return

    usuarios_existentes[email] = {
        'nome': nome,
        'senha': senha
    }
    messagebox.showinfo("Sucesso", f"Cadastro realizado com sucesso, {nome}!")

usuarios_existentes = {}


root = ctk.CTk()
root.resizable(False, False)
root.title("Pet Pals")
root.state("zoomed")
root.geometry("1920x1080")
root.configure(fg_color="white")

# Header da Tela de Cadastro!!

frame_header = ctk.CTkFrame(root, fg_color= "white", height=100, corner_radius=0)
frame_header.place(relx=0.5 , rely=0, relwidth=1, anchor="n")

label_texto = ctk.CTkLabel(frame_header, text="PetPal", font=("Arial",20, 'bold'), text_color="black", width=200)
label_texto.place(x=50, y=38)

imglogo = ("imagens/logo.png")  # "petpals/imagens/patacachorro.png"
img = Image.open(imglogo)
img = img.resize((70,70))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(frame_header, image=img_tk, text='')
label_img.place(x=51, y=15)

inicio = ctk.CTkLabel(frame_header, text="Inicio", font=('Arial',20, 'bold'), text_color="black")
inicio.place(x=800, y=35)

loja = ctk.CTkLabel(frame_header, text="Loja", font=('Arial',20, 'bold'), text_color="black")
loja.place(x=900, y=35)

sobre = ctk.CTkLabel(frame_header, text="Sobre", font=('Arial',20, 'bold'), text_color="black")
sobre.place(x=1000, y=35)

contato = ctk.CTkLabel(frame_header, text="Contato", font=('Arial',20, 'bold'), text_color="black")
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

frame_login = ctk.CTkFrame(root, width=309, height=521, fg_color='#F8F9FA', corner_radius=25, bg_color="#fafafa")
frame_login.place(x=845, y=220)
pywinstyles.set_opacity(frame_login, color="#fafafa")

nome_completo = ctk.CTkLabel(frame_login, text="Nome Completo", font=('Arial', 16, 'bold'), text_color='black')
nome_completo.place(x=20, y=50)
entry_nomecompleto = ctk.CTkEntry(frame_login, width=250, fg_color='white', border_width=0, height=30)
entry_nomecompleto.place(x=20, y=80)

email = ctk.CTkLabel(frame_login, text="Email", font=('Arial', 16, 'bold'), text_color='black')
email.place(x=20, y=125)
entry_email = ctk.CTkEntry(frame_login,width=250, fg_color='white', border_width=0, height=30)
entry_email.place(x=20, y=155)

senha = ctk.CTkLabel(frame_login, text="Senha", font=('Arial', 16, 'bold'), text_color='black')
senha.place(x=20, y=185)
entry_senha = ctk.CTkEntry(frame_login, show='*', width=250, fg_color='white', border_width=0, height=30) 
entry_senha.place(x=20, y=220)

confirmar_senha = ctk.CTkLabel(frame_login, text="Confirmar Senha", font=('Arial', 16, 'bold'), text_color='black')
confirmar_senha.place(x=20, y=255)
entry_confirmar_senha = ctk.CTkEntry(frame_login, show='*', width=250, fg_color='white', border_width=0, height=30)
entry_confirmar_senha.place(x=20, y=290)


check_var = ctk.BooleanVar()
checkbox_termos = ctk.CTkCheckBox(frame_login, text="Li e concordo com os termos de uso", variable=check_var,
 font=("Arial",12, 'bold'), text_color='black', corner_radius=100)
checkbox_termos.place(x=20, y=340)

check_var_termo2 = ctk.BooleanVar()
checkbox_termo2 = ctk.CTkCheckBox(frame_login, text="Li e concordo com as politicas da empresa",
 variable=check_var_termo2, font=("Arial",12, 'bold'), text_color='black', corner_radius=100)
checkbox_termo2.place(x=20, y=390)

botao = ctk.CTkButton(frame_login, text="Cadastrar", font=("Arial",17), command=submit_login, 
                               fg_color="#FD7E14", text_color="white",  width=135, height=45, corner_radius=8)
botao.place(x=80, y=450)

#Rodapé da Tela de Cadastro!!


img_rodape = ("imagens/rodapecerto.png")  # "petpals/imagens/patacachorro.png"
rodape = Image.open(img_rodape)
# rodape = img.resize((20,20))
rodape_img = ImageTk.PhotoImage(rodape)

label_rodape = ctk.CTkLabel(root, image=rodape_img, text='')
label_rodape.place(x=0, y=860)


root.mainloop()