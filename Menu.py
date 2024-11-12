from Cocina import Cocina
from Pedido import Pedido
import customtkinter as ctk
import os
from PIL import Image


class Menu:
    def __init__(self, parent, cocina: Cocina, pedido: Pedido):
        self.frame = parent
        self.cocina = cocina
        self.pedido = pedido

        self.imagenes = self.cargar_imagenes_para_ctkbutton()

    def check_menu(self):
        if self.cocina.despensa.ingredientes['papa'] >= 5:
            self.card_papas()
        if self.cocina.despensa.ingredientes['bebida'] >= 1:
            self.card_pepsi()
        if (self.cocina.despensa.ingredientes['pan de completo'] >= 1 and
                self.cocina.despensa.ingredientes['vienesa'] >= 1 and
                self.cocina.despensa.ingredientes['tomate'] >= 1 and
                self.cocina.despensa.ingredientes['palta'] >= 1):
            self.card_completo()
        if (self.cocina.despensa.ingredientes['pan de hamburguesa'] >= 1 and
                self.cocina.despensa.ingredientes['lamina de queso'] >= 1 and
                self.cocina.despensa.ingredientes['churrasco de carne'] >= 1):
            self.card_hamburguesa()

    def card_papas(self):
        self.tarjeta_papas = ctk.CTkButton(self.frame, text='Papas Fritas', command=self.cocina.make_papas, height=100,
                                           width=100, image=self.imagenes[3], border_width=3, border_color="yellow",
                                           fg_color="gray", hover_color="green", compound="top", text_color='black')
        self.tarjeta_papas.grid(row=0, column=0, padx=5, pady=5)

    def card_pepsi(self):
        self.tarjeta_pepsi = ctk.CTkButton(self.frame, text='Pepsi', command=self.cocina.make_bebida, height=100,
                                           width=100, image=self.imagenes[0], border_width=3, border_color="yellow",
                                           fg_color="gray", hover_color="green", compound="top", text_color='black')
        self.tarjeta_pepsi.grid(row=0, column=1, padx=5, pady=5)

    def card_completo(self):
        self.tarjeta_completo = ctk.CTkButton(self.frame, text='Completo', command=self.cocina.make_completo,
                                              height=100, width=100, image=self.imagenes[2], border_width=3,
                                              border_color="yellow", fg_color="gray", hover_color="green",
                                              compound="top", text_color='black')
        self.tarjeta_completo.grid(row=1, column=0, padx=5, pady=5)

    def card_hamburguesa(self):
        self.tarjeta_hamburguesa = ctk.CTkButton(self.frame, text='Hamburguesa', command=self.cocina.make_hamburguesa,
                                                 height=100, width=100, image=self.imagenes[1], border_width=3,
                                                 border_color="yellow", fg_color="gray", hover_color="green",
                                                 compound="top", text_color='black')
        self.tarjeta_hamburguesa.grid(row=1, column=1, padx=5, pady=5)

    @staticmethod
    def cargar_imagenes_para_ctkbutton(carpeta="img"):
        imagenes = []

        # Obtener todos los archivos .png de la carpeta especificada
        for archivo in os.listdir(carpeta):
            if archivo.endswith(".png"):
                ruta_imagen = os.path.join(carpeta, archivo)

                # Cargar la imagen con PIL
                imagen = Image.open(ruta_imagen).resize((100, 100))

                # Convertir la imagen al formato CTkImage
                ctk_imagen = ctk.CTkImage(imagen)

                # Agregar la imagen convertida a la lista
                imagenes.append(ctk_imagen)

        return imagenes
