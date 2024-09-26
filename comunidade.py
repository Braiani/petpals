import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pywinstyles


root = ctk.CTk()
root.title("Pet Pals")
root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
root.state("zoomed")
root.resizable(False, False)
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
inicio.place(x=700, y=35)

loja = ctk.CTkLabel(frame_header, text="Loja", font=('Arial',20, 'bold'), text_color="black")
loja.place(x=800, y=35)

comunidade = ctk.CTkLabel(frame_header, text='Comunidade', font=('Arial', 20, 'bold'), text_color='black')
comunidade.place(x=890, y=35)

sobre = ctk.CTkLabel(frame_header, text="Sobre", font=('Arial',20, 'bold'), text_color="black")
sobre.place(x=1050, y=35)

contato = ctk.CTkLabel(frame_header, text="Contato", font=('Arial',20, 'bold'), text_color="black")
contato.place(x=1165, y=35)


#Texto das Imagens ==           ==             ==    


taylor_joshua = ctk.CTkLabel(root, text='Taylor Joshua', font=('Arial',40, 'bold'), text_color='black')
taylor_joshua.place(x=650, y=160)

t1 = ('''Nisl nunc vitae integer ridiculus ultrices quam a scelerisque est. Sollicitudin volutpat blandit maecenas ornare dictum tempor. Amet sem non rutrum et duis. Id nisi ac vitae enim neque sapien.
Eu arcu consectetur etiam bibendum fermentum sed lobortis fringilla imperdiet. Aliquet ultrices risus dolor gravida. Faucibus sodales semper a magnis sapien viverra purus sed tortor. Amet risus blandit nunc odio rutrum
''')
texto1 = ctk.CTkLabel(root, text=t1, font=('Arial',20),wraplength=636, justify='left', text_color='gray')
texto1.place(x=650, y=250)

joshua_taylor = ctk.CTkLabel(root, text='Joshua Taylor', font=('Arial',40, 'bold'), text_color='black', anchor='s')
joshua_taylor.place(x=320, y=470)

t2 = ('Morbi viverra eleifend in cras orci a leo tellus. Nunc purus\nadipiscing diam aliquet lorem nunc. Ipsum euismod risus amet\neget non. Pulvinar condimentum ultricies tellus a non pellentesque odio pellentesque\nblandit. Aliquet et massa eget vitae justo tellu \ndonec ac enim. Rhoncus adipiscing cursus'
    )

texto2 = ctk.CTkLabel(root, text=t2, font=('Arial',20), wraplength=680, justify='left', anchor='n', text_color='gray')
texto2.place(x=320, y=600)

# Imagens dos cachorros ==      ==            ==     ==

img_dog1 = ("imagens/fotocachorro.png")
dog = Image.open(img_dog1)
dog_img = ImageTk.PhotoImage(dog)

label_dog1 = ctk.CTkLabel(root, image=dog_img, text='')
label_dog1.place(x=320, y=160)

cachorro = ("imagens/cachorrooculos.png")
cacho = Image.open(cachorro)
cacho_img = ImageTk.PhotoImage(cacho)

label_cachorro = ctk.CTkLabel(root, image=cacho_img, text="")
label_cachorro.place(x=1000, y=450)



#Botão ==          ==               == 

botao = ctk.CTkButton(root, text="", font=("Arial",20), 
                      fg_color="black", text_color="white",  width=50, height=50, corner_radius=100, command=lambda:print('oi'))
botao.place(x=850, y=750, anchor='center')

botao_text = ctk.CTkLabel(root, text='<', font=('Arial', 20), text_color='white', fg_color='#000003')
botao_text.place(x=850, y=750, anchor='center')
pywinstyles.set_opacity(botao_text, color="#000003")







#Rodapé ==       ==         ==         == 

img_rodape = ("imagens/rodapecerto.png")  
rodape = Image.open(img_rodape)
# rodape = img.resize((20,20))
rodape_img = ImageTk.PhotoImage(rodape)

label_rodape = ctk.CTkLabel(root, image=rodape_img, text='')
label_rodape.place(x=0, y=860)

root.mainloop()
