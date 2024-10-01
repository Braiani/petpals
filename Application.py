import customtkinter as ctk
import os, sys
from PIL import Image, ImageTk

class Application:
    def __init__(self) -> None:
        self.janela = ctk.CTk()
        self.title = 'PetPals'
        self.ctk = ctk.set_appearance_mode("dark")
        self.background = '#F8F9FA'
        self.set_background(self.background)
        self.set_geometry(self.janela.winfo_screenwidth(),self.janela.winfo_screenheight())

    def set_geometry(self, width, height):
        # self.janela.attributes('-toolwindow', True)

        self.janela.geometry(f"{width}x{height}+-10+0")

    def set_title(self, title=""):
        self.janela.title(title)

    def set_background(self, color):
        self.background = color
        self.janela.config(background=color)

    @staticmethod
    def get_base_path():
        return os.path.dirname(os.path.abspath(sys.argv[0]))
    
    def top_header(self):
        frame = self.set_frame(options={
            'fg_color': 'white',
            'bg_color': 'white',
            'width': 1840,
            'height': 91
        }, position={
            'x': 0,
            'y': 24
        })


        logo = Image.open(f"{self.get_base_path()}/imagem/dogos/casadog2.png")
        fone = Image.open(f"{self.get_base_path()}/Assets/phone.png")
        mail = Image.open(f"{self.get_base_path()}/Assets/mail.png")
        location = Image.open(f"{self.get_base_path()}/Assets/location.png")

        self.set_image(imagem=fone, size=(24,24), master=frame, position={
            'x': 0,
            'y': 0,
        }, options={
            'bg_color': 'white',
        })

        text_options = {
            "font": ("Poppins", 16, "bold"),
            "text_color": "black",
            "bg_color": "white",
            "fg_color": "white"
        }

        self.set_label(master=frame, text="+55 67 99871-8371", options=text_options, position={
            "x": 32,
            "y": 0
        })

        self.set_image(master=frame, imagem=mail, size=(24,24), position={
            "x": 205,
            "y": 0
        }, options={
            'bg_color': 'white'
        })

        self.set_label(master=frame, text="pet_pal@outlook.com", position={
            'x': 237
        }, options=text_options)

        self.set_image(master=frame, imagem=location, size=(24,24), position={
            "x": 872,
            "y": 0
        }, options={
            'bg_color': 'white'
        })

        self.set_label(master=frame, text="R. do Parque, 75 - Centro, Campo Grande - MS", position={
            'x': 920
        }, options=text_options)
    
    
    def header(self, master=None):
        master = self.verificar_master(master=master)
        frame_header = ctk.CTkFrame(master=master, fg_color= "white", height=100, corner_radius=0)
        frame_header.place(relx=0.5 , rely=0, relwidth=1, anchor="n")

        label_texto = ctk.CTkLabel(frame_header, text="PetPal", font=("Arial",20, 'bold'), text_color="black", width=200)
        label_texto.place(x=50, y=38)

        imglogo = (f"{self.get_base_path()}/imagem/dogos/casadog2.png")  # "petpals/imagens/patacachorro.png"
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
 
    def verificar_master(self, master):
        if not master:
            return self.janela
        return master

    def set_frame(self, position: dict, options: dict, master = None):
        master = self.verificar_master(master=master)
        
        frame = ctk.CTkFrame(master=master)
        frame.configure(**options)
        frame.place(**position)
        return frame
    
    def set_image(self, imagem: Image, size: tuple, position: dict, options: dict, master = None):
        master = self.verificar_master(master=master)

        img = ctk.CTkImage(imagem, size=size)
        label = ctk.CTkLabel(master=master, image=img, text="")
        label.configure(**options)
        label.place(**position)
        return label
    
    def set_label(self, text: str, position: dict, options: dict, master = None):
        master = self.verificar_master(master=master)

        label = ctk.CTkLabel(master=master, text=text)
        label.configure(**options)
        label.place(**position)
        return label


if __name__ == "__main__":
    from Main import Main

    Main