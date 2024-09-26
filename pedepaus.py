import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry('1920x1080')
app.configure(fg_color='white')

framePetPaw = ctk.CTkLabel(app, text='PetPal', text_color='black', font=('', 20, 'bold'), width=200, fg_color='white')
framePetPaw.place(x=20, y=20,) 

framecateg = ctk.CTkLabel(app, text='CATEGORIAS', text_color='black', font=('', 40, 'bold'), width=200, fg_color='Seashell')
framecateg.place(relx=.5, y=250, anchor='center') 

img_path = 'imagens/casadog.png'
img = Image.open(img_path) 
img = img.resize((70, 70))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='', fg_color='white')
label_img.place(x=20, y=0) 

btinicio = ctk.CTkButton(app, text='Inicio', text_color='black', font=('', 20, 'bold'), corner_radius=0, fg_color='white', hover_color='darkorange')
btinicio.place(x=600, y=20)

btprod = ctk.CTkButton(app, text='Loja', text_color='black', font=('', 20, 'bold'), corner_radius=0, fg_color='white', hover_color='darkorange')
btprod.place(x=750, y=20)

btsobre = ctk.CTkButton(app, text='Comunidade', text_color='black', font=('', 20, 'bold'), corner_radius=0, fg_color='white', hover_color='darkorange')
btsobre.place(x=900, y=20)

btcomu = ctk.CTkButton(app, text='Sobre', text_color='black', font=('', 20, 'bold'), corner_radius=0, fg_color='white', hover_color='darkorange')
btcomu.place(x=1050, y=20)

btcomu = ctk.CTkButton(app, text='Contato', text_color='black', font=('', 20, 'bold'), corner_radius=0, fg_color='white', hover_color='darkorange')
btcomu.place(x=1200, y=20)

def frame_label(path,px,py,texto):
    img_path = path
    img = Image.open(img_path) 
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)

    frame_bosta = ctk.CTkFrame(app, width=300, height=320, fg_color='blue')
    frame_bosta.place(x=px, y=py, anchor='center')
    frame_bosta.pack_propagate(False)

    label_img = ctk.CTkLabel(frame_bosta, image=img_tk, text='', height=300, width=300, corner_radius=0)
    label_img.pack(padx=0, pady=0)

    label = ctk.CTkLabel(frame_bosta, font=('', 25, 'bold'), text=texto, text_color='black', height=100, width=300, fg_color='white', corner_radius=0)
    label.place(relx=.5, rely=.875, anchor='center')

frame_label('imagens/shampoo.png', 1500, 510, 'Higiene')
frame_label('imagens/brinquedo.png',1140, 510, 'Brinquedo')
frame_label('imagens/alimento.png',780, 510, 'Alimentação')
frame_label('imagens/coleira.png',420, 510, 'Acessórios')

# label_img.bind('<Button-1>', nova_tela())

img_path = 'imagens/Footer 2.png'
img = Image.open(img_path) 
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=0, y=853)

app.mainloop()