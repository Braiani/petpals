import customtkinter as ctk
from PIL import Image
from Application import Application
import pywinstyles

class higiene(Application):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        self.janela.config(background="white")
        self.janela.title('Categoria - Higiene')
        self.set_geometry('1920','1080')
        self.janela.mainloop()

    def set_frame(self,master, bg_color, relx, rely, anchor):
        self.frame = ctk.CTkFrame(master=master,fg_color=bg_color)
        self.frame.place(relx=relx,rely=rely,anchor=anchor)

    def set_image(self,imagem):
        self.my_image = ctk.CTkImage(
            Image.open(f'/{imagem}'),
            size= (306,306)
        )

    def set_image_label(self,master, image, text, compound,font, num, intense, color, x, y, anchor):
        self.image_label = ctk.CTkLabel(master=master, image=image, text=text, compound=compound, font=(font,num,intense), fg_color=color)
        self.image_label.grid(row=x,column=y)

if __name__ == '__main__':
    higiene = higiene()
    frame1 = higiene.set_frame(higiene.janela, 'blue',0.1,0.5,'center')
    frame2 = higiene.set_frame(higiene.janela, 'yellow',0.3 ,0.5,'center')
    frame3 = higiene.set_frame(higiene.janela, 'red', 0.5,0.5,'center')
    frame4 = higiene.set_frame(higiene.janela, 'black', 0.7,0.5,'center')
    frame5 = higiene.set_frame(higiene.janela, 'green', 0.9,0.5,'center')

    imagem1 = higiene.set_image(r'imagem\higiene\cotonete.png')
    imagem1_label = higiene.set_image_label(frame1, imagem1,'Cotonete','top','Verdana',10,'bold','transparent',0,0,'center')

    higiene.start()