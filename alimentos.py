import customtkinter as ctk
from PIL import Image
from Application import Application
from SqlHandler import SqlHandler
import pywinstyles

# ------------------------------------------------------------------------------- Classe ------------------------------------------------------------------------------- #
class alimentos(Application):
    def __init__(self) -> None:
        super().__init__()

    def start(self):
        self.janela.config(background="white")
        self.janela.title('Categoria - alimentos')
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
#    alimentos = alimentos()
#
#    conectar = SqlHandler()
#    sql = 'Select * from products'
#
#    produto = conectar.exec_query(sql)
#    print(produto)
#
#    for i in produto:    
#        print(i.get('title'))
        
    produto = [{'id_product': 1, 'title': 'Sachê Snoopy', 'image': 'imagem\alimentos\Img.png', 'price': 9.99, 'id_category': 4}, 
     {'id_product': 2, 'title': 'Sachê Pluto', 'image': 'imagem\alimentos\Img2.png', 'price': 9.99, 'id_category': 4}, 
     {'id_product': 3, 'title': 'Ração Yosh', 'image': 'imagem\alimentos\Img3.png', 'price': 29.99, 'id_category': 4}, 
     {'id_product': 4, 'title': 'Ração Muttley', 'image': 'imagem\alimentos\Img4.png', 'price': 29.99, 'id_category': 4}, 
     {'id_product': 5, 'title': 'Ração Doo', 'image': 'imagem\alimentos\Img5.png', 'price': 29.99, 'id_category': 4}]

    # --- Frame
    frame1 = alimentos.set_frame(alimentos, 'white', 306, 306, 0.1,0.5,'center')
    frame2 = alimentos.set_frame(alimentos, 'white', 306,306, 0.3 ,0.5,'center')
    frame3 = alimentos.set_frame(alimentos, 'white', 306,306, 0.5,0.5,'center')
    frame4 = alimentos.set_frame(alimentos, 'white', 306,306, 0.7,0.5,'center')
    frame5 = alimentos.set_frame(alimentos, 'white', 306,306, 0.9,0.5,'center')

    # --- Image
    imagem1 = alimentos.set_image(f'{alimentos.get_base_path()}/image/Zalimentos/Img.png', 306,306)
    imagem1_label = alimentos.set_image_label(frame1, imagem1,'','top','Poppins',15,'bold','white',0.1,0.5, 'center')

    imagem2 = alimentos.set_image(f'{alimentos.get_base_path()}/imagem/alimentos/Im2.png', 306,306)
    imagem2_label = alimentos.set_image_label(frame2, imagem2,'','top','Poppins',15,'bold','white',0.3,0.5, 'center')

    imagem3 = alimentos.set_image(f'{alimentos.get_base_path()}/imagem/alimentos/Img3 7.png',306,306)
    imagem3_label = alimentos.set_image_label(frame3, imagem3,'','top','Poppins',15,'bold','white',0.5,0.485, 'center')

    imagem4 = alimentos.set_image(f'{alimentos.get_base_path()}/imagem/alimentos/Img4.png',306,306)
    imagem4_label = alimentos.set_image_label(frame4, imagem4,'','top','Poppins',15,'bold','white',0.7,0.485, 'center')

    imagem5 = alimentos.set_image(f'{alimentos.get_base_path()}/imagem/alimentos/Img5.png',306,306)
    imagem5_label = alimentos.set_image_label(frame5, imagem5,'','top','Poppins',15,'bold','white',0.9,0.5, 'center')


    a = 0
    b = 0
    for i in produto:
        alimentos.set_text(frame1,i.get('title'),'top','Poppins',20,'bold','white',0.075+a,0.65, 'center')
        alimentos.set_text(frame1,'R$' + str(i.get('price')),'top','Poppins',15,'normal','white',0.070+a,0.675, 'center')
        a+=0.19    

        icone1 = alimentos.set_image(f'{alimentos.get_base_path()}/imagem/icone/Icon+ bg.png',25,25)
        botton1 = alimentos.set_button(frame1, '', 'top', icone1, 'white', 'white','white',0.15+b, 0.65, 'center')
        pywinstyles.set_opacity(botton1, color='white')
        b+=0.2

    alimentos.start()