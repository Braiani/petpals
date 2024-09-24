import customtkinter as ctk
import os, sys
from PIL import Image

class Application:
    def __init__(self) -> None:
        self.janela = ctk.CTk()
        self.title = 'PetPals'
        self.background = 'white'
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
            'width': 1296
        }, position={
            'x': 312,
            'y': 24
        })


        fone = Image.open(f"{self.get_base_path()}/Assets/phone.png")
        mail = Image.open(f"{self.get_base_path()}/Assets/mail.png")
        location = Image.open(f"{self.get_base_path()}/Assets/location.png")

        self.set_image(imagem=fone, size=(24,24), master=frame, position={
            'x': 0,
            'y': 0,
        }, options={
            'bg_color': 'white'
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