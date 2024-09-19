import customtkinter as ctk
from PIL import Image


login = ctk.CTk()
login.title("Login")
login.geometry("1920x1080")


my_image = ctk.CTkImage(
    light_image=Image.open(r"C:\Users\RafaelMontiel\Downloads\casadog2.png"),
    dark_image=Image.open(r"C:\Users\RafaelMontiel\Downloads\casadog2.png"),
    size=(150, 150)  
)

image_label = ctk.CTkLabel(master=login, image=my_image, text="Logo Podre de Chique", compound="top")
image_label.place(x=960, y=200, anchor='center')  

frame_login = ctk.CTkFrame(master=login, width=510, height=500, corner_radius=10)
frame_login.place(x=960, y=540, anchor='center')

label_nome_email = ctk.CTkLabel(master=frame_login, text="Nome/Email")
label_nome_email.grid(row=0, column=0, padx=5, pady=5)

entry_nome_email = ctk.CTkEntry(master=frame_login, width=400)
entry_nome_email.grid(row=1, column=0, padx=5, pady=5)

label_senha = ctk.CTkLabel(master=frame_login, text="Senha")
label_senha.grid(row=2, column=0, padx=5, pady=5)

entry_senha = ctk.CTkEntry(master=frame_login, width=400, show="*")
entry_senha.grid(row=3, column=0, padx=5, pady=5)

button_cadastrar = ctk.CTkButton(master=frame_login, text="Cadastrar")
button_cadastrar.grid(row=4, column=0, sticky='nw')

button_login = ctk.CTkButton(master=frame_login, text="Entrar")
button_login.grid(row=4, column=1, sticky='n')


login.mainloop()
