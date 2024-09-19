import customtkinter as ctk

class Application:
    def __init__(self) -> None:
        self.janela = ctk.CTk()
        self.title = 'PetPals'
        self.background = 'white'
        self.set_background(self.background)
        self.set_geometry(1920,1080)

    def set_geometry(self, width, height):
        self.janela.attributes('-toolwindow', True)

        self.janela.geometry(f"{width}x{height}+-10+0")

    def set_title(self, title=""):
        self.janela.title(title)

    def set_background(self, color):
        self.background = color
        self.janela.config(background=color)