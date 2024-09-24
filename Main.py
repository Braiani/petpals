from Application import Application
import customtkinter as ctk

class Main(Application):
    def __init__(self) -> None:
        super().__init__()
        self.set_geometry(1920,1080)

    def start(self):
        self.janela.mainloop()

root = Main()
root.top_header()

frame = root.set_frame(position={
    'y': 88,
    'x': 312
}, options={
    'width': 1216,
    'bg_color': 'black',
    'fg_color': 'white',
    'border_color': 'white',
    'border_width': 40
})

root.start()