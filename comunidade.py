import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pywinstyles


root = ctk.CTk()
root.resizable(False, False)
root.title("Pet Pals")
root.state("zoomed")
root.geometry("1920x1080")
root.configure(fg_color="white")


#Texto das Imagens ==           ==             ==    


oi = ('''Nisl nunc vitae integer ridiculus ultrices quam a scelerisque est. Sollicitudin volutpat blandit maecenas ornare dictum tempor. Amet sem non rutrum et duis. Id nisi ac vitae enim neque sapien.
Eu arcu consectetur etiam bibendum fermentum sed lobortis fringilla imperdiet. Aliquet ultrices risus dolor gravida. Faucibus sodales semper a magnis sapien viverra purus sed tortor. Amet risus blandit nunc odio rutrum
. Adipiscing tincidunt imperdiet at cursus ipsum vulputate pharetra. Tellus nulla commodo ut ut auctor orci blandit at elit. Turpis pulvinar sagittis tristique aliquam vitae ipsum dui. Amet tempor posuere mi amet vel lobortis bibendum. Commodo purus tincidunt cursus tellus massa vel viverra''')
texto1 = ctk.CTkLabel(root, text=oi, wraplength=636, justify='left')
texto1.place(x=700, y=250)








# Imagens dos cachorros ==      ==            ==     ==

img_dog1 = ("imagens/fotocachorro.png")
dog = Image.open(img_dog1)
dog_img = ImageTk.PhotoImage(dog)

label_dog1 = ctk.CTkLabel(root, image=dog_img, text='')
label_dog1.place(x=400, y=200)


cachorro = ("imagens/cachorrooculos.png")
cacho = Image.open(cachorro)
cacho_img = ImageTk.PhotoImage(cacho)

label_cachorro = ctk.CTkLabel(root, image=cacho_img, text="")
label_cachorro.place(x=1100, y=450)


#Rodapé ==       ==         ==         == 

img_rodape = ("imagens/rodape.png")  
rodape = Image.open(img_rodape)
# rodape = img.resize((20,20))
rodape_img = ImageTk.PhotoImage(rodape)

label_rodape = ctk.CTkLabel(root, image=rodape_img, text='')
label_rodape.place(x=0, y=860)


root.mainloop()
