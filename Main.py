from Application import Application
import customtkinter as ctk

class Main(Application):
    def __init__(self) -> None:
        super().__init__()
        self.set_geometry(1920,1080)

    def start(self):
        self.janela.mainloop()

root = Main()
root.header()

root.start()