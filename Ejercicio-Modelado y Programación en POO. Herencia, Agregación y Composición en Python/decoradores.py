
def log_transaccion(func):
    def wrapper(self, venta):
        print(f"--- [LOG] Iniciando registro de venta para {venta.cliente.nombre} en {self.nombre} ---")
        return func(self, venta)
    return wrapper