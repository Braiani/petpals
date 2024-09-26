import customtkinter as ctk
from PIL import Image
from Application import Application
import pywinstyles

# ------------------------------------------------------------------------------- Classe ------------------------------------------------------------------------------- #
class higiene(Application):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        self.janela.config(background="white")
        self.janela.title('Categoria - Higiene')
        self.set_geometry('1920','1080')
        self.janela.mainloop()

    def set_frame(self,master, bg_color, windth, height, relx, rely, anchor):
        self.frame = ctk.CTkFrame(master=master, 
                                  fg_color=bg_color, 
                                  width=windth, 
                                  height=height)

        self.frame.place(relx=relx, 
                         rely=rely, 
                         anchor=anchor)

    def set_image(self,imagem,x,y):
        return ctk.CTkImage(
            Image.open(f'{imagem}'),
            size= (x,y)
        )

    def set_image_label(self,master, image, text, compound,font, num, intense, color, relx, rely, anchor):
        self.image_label = ctk.CTkLabel(master=master, 
                                        image=image, text=text, 
                                        compound=compound, 
                                        font=(font,num,intense), 
                                        fg_color=color)
        
        self.image_label.place(relx=relx,
                               rely=rely, 
                               anchor=anchor)

    def set_text(self,master, text, compound,font, num, intense, color1, relx, rely, anchor):

        self.image_label = ctk.CTkLabel(master=master, 
                                        text=text, 
                                        compound=compound, 
                                        font=(font,num,intense), 
                                        fg_color=color1)
        
        self.image_label.place(relx=relx,
                               rely=rely, 
                               anchor=anchor)



    def set_button(self, master, text, compound, image, fg_color, bg_color,hover,relx, rely, anchor):
        self.botao = ctk.CTkButton(master=master, 
                                   text=text, 
                                   compound=compound, 
                                   image=image, 
                                   fg_color=fg_color, 
                                   bg_color=bg_color,
                                   hover_color=hover)
    
        self.botao.place(relx=relx, 
                         rely=rely, 
                         anchor=anchor)
        return self.botao
    

# ------------------------------------------------------------------------------- Aplicação ------------------------------------------------------------------------------- #
if __name__ == '__main__':
    higiene = higiene()

    # --- Frame
    frame1 = higiene.set_frame(higiene.janela, 'white', 306, 306, 0.1,0.5,'center')
    frame2 = higiene.set_frame(higiene.janela, 'white', 306,306, 0.3 ,0.5,'center')
    frame3 = higiene.set_frame(higiene.janela, 'white', 306,306, 0.5,0.5,'center')
    frame4 = higiene.set_frame(higiene.janela, 'white', 306,306, 0.7,0.5,'center')
    frame5 = higiene.set_frame(higiene.janela, 'white', 306,306, 0.9,0.5,'center')

    # --- Image
    imagem1 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/cotonete.png', 306,306)
    imagem1_label = higiene.set_image_label(frame1, imagem1,'','top','Poppins',15,'bold','white',0.1,0.5, 'center')

    imagem2 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/pomada.png', 306,306)
    imagem2_label = higiene.set_image_label(frame2, imagem2,'','top','Poppins',15,'bold','white',0.3,0.5, 'center')

    imagem3 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/image 7.png',306,306)
    imagem3_label = higiene.set_image_label(frame3, imagem3,'','top','Poppins',15,'bold','white',0.5,0.485, 'center')

    imagem4 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/pet_shamp.png',306,306)
    imagem4_label = higiene.set_image_label(frame4, imagem4,'','top','Poppins',15,'bold','white',0.7,0.485, 'center')

    imagem5 = higiene.set_image(f'{higiene.get_base_path()}/imagem/higiene/dental.png',306,306)
    imagem5_label = higiene.set_image_label(frame5, imagem5,'','top','Poppins',15,'bold','white',0.9,0.5, 'center')


    # --- Text
    text_prod1 = higiene.set_text(frame1,'Cotonete','top','Poppins',20,'bold','white',0.05,0.65, 'center')
    text_price1 = higiene.set_text(frame1,'R$19,99','top','Poppins',15,'normal','white',0.042,0.679, 'center')

    text_prod2 = higiene.set_text(frame2,'Pomada Neodexa','top','Poppins',20,'bold','white',0.273,0.65, 'center')
    text_price2 = higiene.set_text(frame2,'R$59,99','top','Poppins',15,'normal','white',0.245,0.679, 'center')

    text_prod3= higiene.set_text(frame3,'Shamposhi','top','Poppins',20,'bold','white',0.465,0.65, 'center')
    text_price3 = higiene.set_text(frame3,'R$99,99','top','Poppins',15,'normal','white',0.453,0.679, 'center')

    text_prod4= higiene.set_text(frame4,'Pet Carrier','top','Poppins',20,'bold','white',0.670,0.65, 'center')
    text_price4 = higiene.set_text(frame4,'R$29,99','top','Poppins',15,'normal','white',0.658,0.679, 'center')

    text_prod5 = higiene.set_text(frame5,'Pasta Dental','top','Poppins',20,'bold','white',0.855,0.65, 'center')
    text_price5 = higiene.set_text(frame5,'R$29,99','top','Poppins',15,'normal','white',0.839,0.679, 'center')

    # --- Button
    icone1 = higiene.set_image(f'{higiene.get_base_path()}/imagem/icone/Icon+ bg.png',25,25)
    botton1 = higiene.set_button(frame1, '', 'top', icone1, 'white', 'white','white',0.15, 0.65, 'center')
    pywinstyles.set_opacity(botton1, color='white')

    icone2 = higiene.set_image(f'{higiene.get_base_path()}/imagem/icone/Icon+ bg.png',25,25)
    botton2 = higiene.set_button(frame2, '', 'top', icone2, 'white', 'white','white',0.362, 0.65, 'center')
    pywinstyles.set_opacity(botton2, color='white')

    icone3 = higiene.set_image(f'{higiene.get_base_path()}/imagem/icone/Icon+ bg.png',25,25)
    botton3 = higiene.set_button(frame3, '', 'top', icone3, 'white', 'white','white',0.555, 0.65, 'center')
    pywinstyles.set_opacity(botton3, color='white')

    icone4 = higiene.set_image(f'{higiene.get_base_path()}/imagem/icone/Icon+ bg.png',25,25)
    botton4 = higiene.set_button(frame4, '', 'top', icone4, 'white', 'white','white',0.765, 0.65, 'center')
    pywinstyles.set_opacity(botton4, color='white')

    icone5 = higiene.set_image(f'{higiene.get_base_path()}/imagem/icone/Icon+ bg.png',25,25)
    botton5 = higiene.set_button(frame5, '', 'top', icone5, 'white', 'white','white',0.955, 0.65, 'center')
    pywinstyles.set_opacity(botton5, color='white')


    higiene.start()
