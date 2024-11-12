import customtkinter as ctk
from tkinter import ttk
import re
from CTkMessagebox import CTkMessagebox

from Cocina import Cocina
from Manejar_ingredientes import Despensa, Ingrediente
from Menu import Menu
from Pedido import Pedido


class AppTomarOrden(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Ingredientes y Pedidos")
        self.geometry("800x800")
        self.despensa = Despensa()
        self.concina = Cocina(main=self, despensa=self.despensa)
        self.pedido = Pedido()

        self.add_tabs()
        self.add_widget_tab_menu()
        self.add_widget_tab_ingredientes()

    def add_tabs(self):
        self.tabview = ctk.CTkTabview(self, width=600, height=500)
        self.tabview.pack(padx=20, pady=20)

        self.tab_ingredientes = self.tabview.add("Ingreso de Libros")
        self.tab_menu = self.tabview.add("Pedido")

    # Tab Ingredientes

    def add_widget_tab_ingredientes(self):
        frame_form = ctk.CTkFrame(self.tab_ingredientes, fg_color='red')
        frame_form.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        frame_treeview = ctk.CTkFrame(self.tab_ingredientes, fg_color='red')
        frame_treeview.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Formulario nombre
        label_nombre = ctk.CTkLabel(frame_form, text="Nombre del Ingrediente:")
        label_nombre.pack(pady=5)
        self.entry_nombre = ctk.CTkComboBox(frame_form, values=self.despensa.ingredientes_posibles(), fg_color='white',
                                            border_width=0, text_color='black')
        self.entry_nombre.pack(pady=5)

        # Formulario autor
        label_cantidad = ctk.CTkLabel(frame_form, text="Cantidad:")
        label_cantidad.pack(pady=5)
        self.entry_cantidad = ctk.CTkEntry(frame_form, fg_color='white', text_color='black', border_width=0)
        self.entry_cantidad.pack(pady=5)

        # Botón de ingreso
        self.boton_ingresar = ctk.CTkButton(frame_form, text="Ingresar Ingrediente", fg_color='yellow',
                                            text_color='black', hover_color='white')
        self.boton_ingresar.configure(command=self.ingresar_ingrediente)
        self.boton_ingresar.pack(pady=10)

        # Botón para eliminar ingrediente
        self.boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar Ingrediente",
                                            command=self.eliminar_ingrediente, fg_color='yellow', text_color='black',
                                            hover_color='white')
        self.boton_eliminar.pack(pady=10)

        # Treeview en el segundo frame
        style = ttk.Style()
        style.configure('Treeview', font=('Arial', 12))
        style.configure('Treeview.Heading', font=('Arial', 16))
        self.tree_ingredientes = ttk.Treeview(frame_treeview, columns=("Ingrediente", "Cantidad"), show="headings")
        self.tree_ingredientes.heading("Ingrediente", text="Ingrediente")
        self.tree_ingredientes.heading("Cantidad", text="Cantidad")
        self.tree_ingredientes.pack(expand=True, fill="both", padx=10, pady=10)

        self.boton_menu = ctk.CTkButton(frame_treeview, text='Generar Menú', command=self.cartas.check_menu,
                                        fg_color='yellow', text_color='black', hover_color='white')
        self.boton_menu.pack()

    @staticmethod
    def validar_nombre(nombre):
        if re.match(r"^[a-zA-Z\s]+$", nombre):
            return True
        else:
            CTkMessagebox(title="Error de Validación", message="El nombre debe contener solo letras y espacios.",
                          icon="warning")
            return False

    @staticmethod
    def validar_cantidad(cantidad):
        try:
            int(cantidad)
            return True
        except:
            CTkMessagebox(title="Error de Validación", message="La cantidad debe ser un entero",
                          icon="warning")
            return False

    def ingresar_ingrediente(self):
        nombre = self.entry_nombre.get()
        cantidad = self.entry_cantidad.get()

        if self.validar_nombre(nombre) and self.validar_cantidad(cantidad):
            self.despensa.add_ingrediente(Ingrediente(nombre, int(cantidad)))

        self.update_tree_ingredientes()

    def eliminar_ingrediente(self):
        seleccion = self.tree_ingredientes.selection()
        if not seleccion:
            CTkMessagebox(title="Error", message="Por favor selecciona un ingrediente para eliminar.", icon="warning")
            return

        item = self.tree_ingredientes.item(seleccion)
        nombre = item['values'][0]
        self.despensa.remove_ingrediente(nombre)
        self.despensa.mostrar_ingredientes()
        self.update_tree_ingredientes()

    def update_tree_ingredientes(self):
        for item in self.tree_ingredientes.get_children():
            self.tree_ingredientes.delete(item)

        for ingrediente, cantidad in self.despensa.ingredientes.items():
            if cantidad > 0:
                self.tree_ingredientes.insert("", "end", values=(ingrediente, cantidad))

    # Tab Menú

    def add_widget_tab_menu(self):
        self.frame_menu = ctk.CTkFrame(self.tab_menu, fg_color='red', height=300, width=400)
        self.frame_menu.pack(fill='both', expand=False)

        self.boton_eliminar_pedido = ctk.CTkButton(self.tab_menu, text='Eliminar Menú', command=self.eliminar_menu,
                                                   fg_color='yellow', text_color='black', hover_color='white')
        self.boton_eliminar_pedido.pack(pady=10)

        self.total = ctk.CTkLabel(self.tab_menu, text='El total es 0$')
        self.total.pack()

        self.frame_tree_pedido = ctk.CTkFrame(self.tab_menu, fg_color='red', height=300, width=200)
        self.frame_tree_pedido.pack(fill='both', expand=False)

        self.boton_boleta = ctk.CTkButton(self.tab_menu, text='Generar Boleta', fg_color='yellow', text_color='black',
                                          hover_color='white', command=self.obtener_detalle_compra)
        self.boton_boleta.pack(pady=10)

        # Tarjetas
        self.cartas = Menu(self.frame_menu, self.concina, self.pedido)

        # Tree Pedido
        style = ttk.Style()
        style.configure('Treeview', font=('Arial', 12))
        style.configure('Treeview.Heading', font=('Arial', 16))
        self.tree_pedido = ttk.Treeview(self.frame_tree_pedido, columns=("Nombre del Menú", "Cantidad", "Precio Unitario"), show="headings")
        self.tree_pedido.heading("Nombre del Menú", text="Nombre del Menú")
        self.tree_pedido.heading("Cantidad", text="Cantidad")
        self.tree_pedido.heading("Precio Unitario", text="Precio Unitario")
        self.tree_pedido.pack(expand=True, fill="both", padx=10, pady=10)

    def update_tree_pedido(self):
        for item in self.tree_pedido.get_children():
            self.tree_pedido.delete(item)

        for p in self.pedido.mostrar_pedido():
            if p[0] == 'Papas Fritas':
                valor = 500
            if p[0] == 'Pepsi':
                valor = 1100
            if p[0] == 'Completo':
                valor = 1800
            if p[0] == 'Hamburguesa':
                valor = 3500
            self.tree_pedido.insert("", "end", values=(p[0], p[1], valor))
        self.total.configure(text=f'El total es {self.get_total()}$')

    def eliminar_menu(self):
        seleccion = self.tree_pedido.selection()
        if not seleccion:
            CTkMessagebox(title="Error", message="Por favor selecciona un ingrediente para eliminar.", icon="warning")
            return

        item = self.tree_pedido.item(seleccion)
        nombre = item['values'][0]
        cant = item['values'][1]
        if nombre == 'Papas Fritas':
            self.despensa.add_ingrediente(Ingrediente('papa', 5*int(cant)))
        if nombre == 'Pepsi':
            self.despensa.add_ingrediente(Ingrediente('bebida', int(cant)))
        if nombre == 'Completo':
            self.despensa.add_ingrediente(Ingrediente('pan de completo', int(cant)))


        self.pedido.eliminar_elemento(nombre)
        self.update_tree_pedido()
        self.update_tree_ingredientes()

    def get_total(self):
        total = 0
        for item in self.tree_pedido.get_children():
            cantidad = int(self.tree_pedido.item(item, "values")[1])
            precio = int(self.tree_pedido.item(item, "values")[2])
            total += cantidad * precio

        print(f"Valor total de la compra es: {total} pesos")
        return total

    def obtener_detalle_compra(self):
        detalle_compra = []

        for item in self.tree_pedido.get_children():
            valores = self.tree_pedido.item(item, "values")
            nombre_alimento = valores[0]
            cantidad = int(valores[1])
            precio_por_unidad = int(valores[2])
            total_precio = cantidad * precio_por_unidad
            detalle_compra.append([nombre_alimento, cantidad, total_precio])

        print()
        for detalle in detalle_compra:
            print(f"Alimento: {detalle[0]}, Cantidad: {detalle[1]}, Total: {detalle[2]}")
        print()
        return detalle_compra


main = AppTomarOrden()

main.mainloop()
