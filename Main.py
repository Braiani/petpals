from Application import Application
import customtkinter as ctk
from PIL import Image

class Main(Application):
    def __init__(self) -> None:
        super().__init__()
        self.set_geometry(1920,1080)

    def start(self):
        self.janela.mainloop()

if __name__ == "__main__":
    root = Main()

    frame = ctk.CTkFrame(master=root.janela)

    image1 = Image.open("Assets/phone.png")

    img = ctk.CTkImage(image1, size=(40,40))
    label = ctk.CTkLabel(root.janela, image=img, text="")
    label.configure(bg_color="white")
    label.grid(row=0, column=0, padx=20, pady=20)

    root.start()