import customtkinter as ctk
from PIL import Image
from Application import Application

class Login(Application):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        self.janela.mainloop()

login = Login()
login.set_title("Login")
login.set_geometry("1920", "1080")
login.set_background("white")

bg_imagem = ctk.CTkImage(
    light_image=Image.open(r"imagem\image.png"),
    dark_image=Image.open(r"imagem\image.png"),
    size=(login.janela.winfo_screenwidth(), login.janela.winfo_screenheight())
)

bg_label = ctk.CTkLabel(master=login.janela, image=bg_imagem)
bg_label.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor='center')  

my_image = ctk.CTkImage(
    light_image=Image.open(r"C:\Users\RafaelMontiel\Downloads\casadog2.png"),
    dark_image=Image.open(r"C:\Users\RafaelMontiel\Downloads\casadog2.png"),
    size=(100, 100)  
)

image_label = ctk.CTkLabel(master=login.janela, image=my_image, text="PetPal", compound="left", font=('Verdana',20,'bold'), fg_color='white')
image_label.place(x=70, y=35, anchor='center')  


frame_login = ctk.CTkFrame(master=login.janela, width=400, height=225, corner_radius=10)
frame_login.place(relx=0.5, rely=0.5, anchor='center')

label_nome_email = ctk.CTkLabel(master=frame_login, text="Nome/Email", font=('Verdana',15,'bold'))
label_nome_email.place(relx=0.18, rely=0.15, anchor='center')

entry_nome_email = ctk.CTkEntry(master=frame_login, width=350)
entry_nome_email.place(relx=0.50, rely=0.25, anchor='center')

label_senha = ctk.CTkLabel(master=frame_login, text="Senha", font=('Verdana',15,'bold'))
label_senha.place(relx=0.13, rely=0.45, anchor='center')

entry_senha = ctk.CTkEntry(master=frame_login, width=350, show="*")
entry_senha.place(relx=0.50, rely=0.55, anchor='center')

button_cadastrar = ctk.CTkButton(master=frame_login, text="Cadastrar", fg_color='dark orange')
button_cadastrar.place(relx=0.25, rely=0.85, anchor='center')

button_login = ctk.CTkButton(master=frame_login, text="Entrar", fg_color='dark orange')
button_login.place(relx=0.75, rely=0.85, anchor='center')


login.start()
