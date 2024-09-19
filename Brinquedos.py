from Application import Application
import customtkinter
class Brinquedos(Application): 
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        self.janela.mainloop()


brinquedos = Brinquedos()

#Barra de opções 
barra = customtkinter.CTkFrame(master = brinquedos.janela, width = 1920, height=150, fg_color="#FFFFFF").place(relx=0.5,rely=0, anchor="center")

#Opções da barra 

bt_inicio = customtkinter.CTkButton(master = brinquedos.janela, text = "", width=50, height=60, fg_color="#FFFFFF", hover_color="#FFFFFF").place(relx=0.05,rely=0.03,anchor="center")

brinquedos.start()