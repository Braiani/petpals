import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry('1920x1080')
app.configure(fg_color='white')

framephone = ctk.CTkLabel(app, text='+55 67 99871-8371', text_color='black', font=('', 15, 'bold'), width=200)
framephone.place(x=350, y=40) 

frame_email = ctk.CTkLabel(app, text='pet_pal@outlook.com', text_color='black', font=('', 15, 'bold'), width=200)
frame_email.place(x=565, y=38) 

framelocation = ctk.CTkLabel(app, text='R. do Parque, 75 - Centro, Campo Grande - MS', text_color='black', font=('', 15, 'bold'), width=200)
framelocation.place(x=1270, y=38) 

framePetPaw = ctk.CTkLabel(app, text='PetPal', text_color='black', font=('', 20, 'bold'), width=200)
framePetPaw.place(x=850, y=150,) 

img_path = '0509calculadora\AtividadeSetembro\pedepaus\imagens\phone.png'
img = Image.open(img_path) 
img = img.resize((30, 30))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=350, y=38)

img_path = '0509calculadora\AtividadeSetembro\pedepaus\imagens\email.png'
img = Image.open(img_path) 
img = img.resize((30, 30))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=550, y=38)

img_path = '0509calculadora\AtividadeSetembro\pedepaus\imagens\location-16-regular.png'
img = Image.open(img_path) 
img = img.resize((30, 30))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=1230, y=38)

img_path = '0509calculadora\AtividadeSetembro\pedepaus\imagens\paw.png'
img = Image.open(img_path) 
img = img.resize((30, 30))
img_tk = ImageTk.PhotoImage(img)

label_img = ctk.CTkLabel(app, image=img_tk, text='')
label_img.place(x=883, y=150)

inicio = ctk.CTkButton(app, text='INICIO', corner_radius=0)
inicio.place(x=50, y=150)

inicio = ctk.CTkButton(app, text='PRODUTOS', corner_radius=0)
inicio.place(x=200, y=150)

inicio = ctk.CTkButton(app, text='SOBRE', corner_radius=0)
inicio.place(x=350, y=150)

inicio = ctk.CTkButton(app, text='COMUNIDADE', corner_radius=0)
inicio.place(x=500, y=150)

buscar = ctk.CTkEntry(app, placeholder_text='Buscar...', width=250, corner_radius=50)
buscar.place(x=1270, y=150)

app.mainloop()