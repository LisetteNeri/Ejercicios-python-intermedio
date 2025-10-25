from venta import Venta
from decoradores import log_transaccion

class Tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.ventas: list[Venta] = []

    @log_transaccion
    def registrar_venta(self, venta: Venta) -> None:
        self.ventas.append(venta)
