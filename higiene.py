import customtkinter as ctk
from PIL import Image
from Application import Application
import pywinstyles

# ------------------------------------------------------------------------------- Classe ------------------------------------------------------------------------------- #
class higiene(Application):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        self.janela.config(background="black")
        self.janela.title('Categoria - Higiene')
        self.set_geometry('1920','1080')
        self.janela.mainloop()

    def set_frame(self,master, bg_color, windth, height, relx, rely, anchor):
        self.frame = ctk.CTkFrame(master=master, fg_color=bg_color, width=windth, height=height)
        self.frame.place(relx=relx, rely=rely, anchor=anchor)

    def set_image(self,imagem):
        return ctk.CTkImage(
            Image.open(f'{imagem}'),
            size= (306,306)
        )

    def set_image_label(self,master, image, text, compound,font, num, intense, color, relx, rely, anchor):
        self.image_label = ctk.CTkLabel(master=master, image=image, text=text, compound=compound, font=(font,num,intense), fg_color=color)
        self.image_label.place(relx=relx,rely=rely, anchor=anchor)

    def set_text(self,master, text, compound,font, num, intense, color1, relx, rely, anchor):
        self.image_label = ctk.CTkLabel(master=master, text=text, compound=compound, font=(font,num,intense), fg_color=color1)
        self.image_label.place(relx=relx,rely=rely, anchor=anchor)

# ------------------------------------------------------------------------------- Aplicação ------------------------------------------------------------------------------- #
if __name__ == '__main__':
    higiene = higiene()

    # --- Frame
    frame1 = higiene.set_frame(higiene.janela, 'blue', 306, 306, 0.1,0.5,'center')
    frame2 = higiene.set_frame(higiene.janela, 'yellow', 306,306, 0.3 ,0.5,'center')
    frame3 = higiene.set_frame(higiene.janela, 'red', 306,306, 0.5,0.5,'center')
    frame4 = higiene.set_frame(higiene.janela, 'black', 306,306, 0.7,0.5,'center')
    frame5 = higiene.set_frame(higiene.janela, 'green', 306,306, 0.9,0.5,'center')

    # --- Image
    imagem1 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/cotonete.png')
    imagem1_label = higiene.set_image_label(frame1, imagem1,'','top','Poppins',15,'bold','white',0.1,0.5, 'center')

    imagem2 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/dental.png')
    imagem2_label = higiene.set_image_label(frame2, imagem2,'','top','Poppins',15,'bold','white',0.3,0.5, 'center')

    imagem3 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/image 7.png')
    imagem3_label = higiene.set_image_label(frame3, imagem3,'','top','Poppins',15,'bold','white',0.5,0.5, 'center')

    imagem4 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/pet_shamp.png')
    imagem4_label = higiene.set_image_label(frame4, imagem4,'','top','Poppins',15,'bold','white',0.7,0.5, 'center')

    imagem5 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/pomada.png')
    imagem5_label = higiene.set_image_label(frame5, imagem5,'','top','Poppins',15,'bold','white',0.9,0.5, 'center')

    # --- Text
    text_prod1 = higiene.set_text(frame1,'Cotonete','top','Poppins',20,'normal','white',0.05,0.65, 'center')
    
    higiene.start()