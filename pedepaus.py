import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry('1920x1080')
app.configure(fg_color='Seashell')

framefundo = ctk.CTkFrame(app, width=1880, height=85, fg_color='white', corner_radius=60)
framefundo.place(x=20, y=122)

framephone = ctk.CTkLabel(app, text='+55 67 99871-8371', text_color='black', font=('', 15, 'bold'), width=200)
framephone.place(x=350, y=40) 

frame_email = ctk.CTkLabel(app, text='pet_pal@outlook.com', text_color='black', font=('', 15, 'bold'), width=200)
frame_email.place(x=565, y=38) 

framelocation = ctk.CTkLabel(app, text='R. do Parque, 75 - Centro, Campo Grande - MS', text_color='black', font=('', 15, 'bold'), width=200)
framelocation.place(x=1270, y=38) 

framePetPaw = ctk.CTkLabel(app, text='PetPal', text_color='black', font=('', 20, 'bold'), width=200, fg_color='white')
framePetPaw.place(x=860, y=150,) 

framecateg = ctk.CTkLabel(app, text='CATEGORIAS', text_color='black', font=('', 40, 'bold'), width=200, fg_color='Seashell')
framecateg.place(x=825, y=250,) 

img_path = 'imagens\phone.png'
img = Image.open(img_path) 
img = img.resize((30, 30))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=350, y=38)

img_path = 'imagens\email.png'
img = Image.open(img_path) 
img = img.resize((30, 30))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=550, y=38)

img_path = 'imagens\location-16-regular.png'
img = Image.open(img_path) 
img = img.resize((30, 30))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=1230, y=38)

img_path = 'imagens\casadog.png'
img = Image.open(img_path) 
img = img.resize((70, 70))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='', fg_color='white')
label_img.place(x=860, y=130)

frameinicio = ctk.CTkLabel(app, text='', width=140, fg_color='darkorange')
frameinicio.place(x=50, y=153) 

def on_enter(button):
    button.configure(fg_color='darkorange')
def on_leave(button):
    button.configure(fg_color='orange')

btinicio = ctk.CTkButton(app, text='INICIO', corner_radius=0, fg_color='orange')
btinicio.place(x=50, y=150)
btinicio.bind("<Enter>", lambda event: on_enter(btinicio))
btinicio.bind("<Leave>", lambda event: on_leave(btinicio))

frameprod = ctk.CTkLabel(app, text='', width=140, fg_color='darkorange')
frameprod.place(x=200, y=153) 

btprod = ctk.CTkButton(app, text='PRODUTOS', corner_radius=0, fg_color='orange')
btprod.place(x=200, y=150)
btprod.bind("<Enter>", lambda event: on_enter(btprod))
btprod.bind("<Leave>", lambda event: on_leave(btprod))

framesobre = ctk.CTkLabel(app, text='', width=140, fg_color='darkorange')
framesobre.place(x=350, y=153) 

btsobre = ctk.CTkButton(app, text='SOBRE', corner_radius=0, fg_color='orange')
btsobre.place(x=350, y=150)
btsobre.bind("<Enter>", lambda event: on_enter(btsobre))
btsobre.bind("<Leave>", lambda event: on_leave(btsobre))

framecomu = ctk.CTkLabel(app, text='', width=140, fg_color='darkorange')
framecomu.place(x=500, y=153) 

btcomu = ctk.CTkButton(app, text='COMUNIDADE', corner_radius=0, fg_color='orange')
btcomu.place(x=500, y=150)
btcomu.bind("<Enter>", lambda event: on_enter(btcomu))
btcomu.bind("<Leave>", lambda event: on_leave(btcomu))

buscar = ctk.CTkEntry(app, placeholder_text='Buscar...', width=250, height=31, corner_radius=50)
buscar.place(x=1520, y=150)

framebusc = ctk.CTkLabel(app, text='', width=45, height=30, corner_radius=10, fg_color='darkorange')
framebusc.place(x=1750, y=151) 

imagem_busca = Image.open('imagens\lupa.png')
imagem_busca = imagem_busca.resize((20, 20))
imagem_tk = ImageTk.PhotoImage(imagem_busca)

busca = ctk.CTkButton(app, image=imagem_tk, text='', width=20, height=20, corner_radius=25, fg_color='orange')
busca.place(x=1750, y=150)
busca.image = imagem_tk
busca.bind("<Enter>", lambda event: on_enter(busca))
busca.bind("<Leave>", lambda event: on_leave(busca))

imagem_wishlist = Image.open('imagens\heart-twotone.png')
imagem_wishlist = imagem_wishlist.resize((20, 20))
imagem_tk = ImageTk.PhotoImage(imagem_wishlist)

wishlist = ctk.CTkButton(app, image=imagem_tk, text='', width=20, height=20, corner_radius=25, fg_color='white')
wishlist.place(x=1800, y=150)
wishlist.image = imagem_tk

imagem_cart = Image.open('imagens\cart-duotone.png')
imagem_cart = imagem_cart.resize((20, 20))
imagem_tk = ImageTk.PhotoImage(imagem_cart)

cart = ctk.CTkButton(app, image=imagem_tk, text='', width=20, height=20, corner_radius=25, fg_color='white')
cart.place(x=1850, y=150)
cart.image = imagem_tk

img_path = 'imagens\Footer 1.png'
img = Image.open(img_path) 
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=0, y=820)

app.mainloop()