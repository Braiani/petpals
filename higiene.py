import customtkinter as ctk
from PIL import Image
from Application import Application
from SqlHandler import SqlHandler
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

    conectar = SqlHandler()
    sql = 'Select * from products'

    produto = conectar.exec_query(sql)
    print(produto)

    for i in produto:    
        print(i.get('title'))
        


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


    a = 0
    b = 0
    for i in produto:
        higiene.set_text(frame1,i.get('title'),'top','Poppins',20,'bold','white',0.075+a,0.65, 'center')
        higiene.set_text(frame1,'R$' + str(i.get('price')),'top','Poppins',15,'normal','white',0.070+a,0.675, 'center')
        a+=0.19    

        icone1 = higiene.set_image(f'{higiene.get_base_path()}/imagem/icone/Icon+ bg.png',25,25)
        botton1 = higiene.set_button(frame1, '', 'top', icone1, 'white', 'white','white',0.15+b, 0.65, 'center')
        pywinstyles.set_opacity(botton1, color='white')
        b+=0.2

    higiene.start()