from Application import Application
import customtkinter as ctk
from PIL import Image

class Main(Application):
    def __init__(self) -> None:
        super().__init__()
        self.set_geometry(1920,1080)

    def start(self):
        self.janela.mainloop()

root = Main()

frame = ctk.CTkFrame(master=root.janela)
frame.configure(fg_color="white")
frame.configure(bg_color="white")
frame.grid(row=0, column=0, padx=312)

image1 = Image.open(f"{root.get_base_path()}/Assets/phone.png")

img = ctk.CTkImage(image1, size=(40,40))
label = ctk.CTkLabel(frame, image=img, text="")
label.configure(bg_color="white")
label.grid(row=0, column=0, padx=(0,8), pady=24)

ctk.CTkLabel(master=frame, text="+55 67 99871-8371")
label.configure(text_color="black", bg_color="white", fg_color="white")
label.grid(row=0, column=1, pady=24)

root.start()