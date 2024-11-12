from fpdf import FPDF
from datetime import datetime


class Boleta(FPDF):
    def __init__(self, items):
        super().__init__()
        # Detalles fijos de la boleta (simulación)
        self.razon_social = 'Restaurante Ejemplo'
        self.rut = '12345678-9'
        self.direccion = 'Calle Falsa 123'
        self.telefono = '+56 9 1234 5678'
        self.fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')  # Obtener fecha actual
        self.items = items
        self.total = 0
        self.iva = 0.19  # IVA fijo del 19%

        self.calcular_totales()
        # Desactivar saltos de página automáticos
        self.set_auto_page_break(auto=False)

    def calcular_totales(self):
        """Calcula los totales y el IVA a partir de los ítems proporcionados."""
        self.subtotal = 0
        for item in self.items:
            nombre, cantidad, precio_total = item
            self.subtotal += precio_total

        self.monto_iva = self.subtotal * self.iva
        self.total = self.subtotal + self.monto_iva

    def header(self):
        """Genera la cabecera de la boleta."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Boleta Restaurante', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, f'Razón Social del Negocio: {self.razon_social}', 0, 1)
        self.cell(0, 10, f'RUT: {self.rut}', 0, 1)
        self.cell(0, 10, f'Dirección: {self.direccion}', 0, 1)
        self.cell(0, 10, f'Teléfono: {self.telefono}', 0, 1)
        self.cell(0, 10, f'Fecha: {self.fecha}', 0, 1)
        self.ln(10)

    def body(self):
        """Genera el cuerpo de la boleta con los detalles de los ítems."""
        self.set_font('Arial', 'B', 10)
        self.cell(70, 10, 'Nombre', 1)
        self.cell(30, 10, 'Cantidad', 1)
        self.cell(40, 10, 'Precio Total', 1)
        self.ln()

        self.set_font('Arial', '', 10)
        for item in self.items:
            nombre, cantidad, precio_total = item
            self.cell(70, 10, nombre, 1)
            self.cell(30, 10, str(cantidad), 1)
            self.cell(40, 10, f"${precio_total:.2f}", 1)
            self.ln()

        self.ln(10)
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, f'Subtotal: ${self.subtotal:.2f}', 0, 1, 'R')
        self.cell(0, 10, f'IVA (19%): ${self.monto_iva:.2f}', 0, 1, 'R')
        self.cell(0, 10, f'Total: ${self.total:.2f}', 0, 1, 'R')

    def footer(self):
        """Genera el pie de página de la boleta."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Gracias por su compra. Para cualquier consulta, llamenos al {}'.format(self.telefono), 0, 0,
                  'C')
        self.ln(4)
        self.cell(0, 10, 'Los productos adquiridos no tienen garantía.', 0, 0, 'C')

    def generar_boleta(self, filename):
        """Genera el archivo PDF de la boleta."""
        self.add_page()  # Solo se agrega una página
        self.header()  # Generar la cabecera
        self.body()  # Generar el cuerpo
        self.footer()  # Generar el pie de página
        self.output(filename)  # Guardar el archivo PDF
