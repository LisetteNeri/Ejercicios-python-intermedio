from cliente import Cliente
from administrador import Administrador
from producto import Producto
from venta import Venta
from tienda import Tienda

cliente1 = Cliente("Luis", "luis@gmail.com", 10000.00)
admin1 = Administrador("Ana", "ana@admin.com", ["gestion_ventas", "gestion_inventario"])

p1 = Producto("Teclado", 250.00)
p2 = Producto("Mouse", 150.00)
p3 = Producto("Monitor", 800.00)
p4 = Producto("CPU",1200.00)

lista_productos =[p1,p2,p3,p4]

venta1 = Venta(cliente1)
venta1.agregar_producto(p1)
venta1.agregar_producto(p2)
venta1.agregar_producto(p3)

tienda = Tienda("TechStore")
print(admin1.mostrar_info())

print("--- Verificación de Precios ---")
for producto in lista_productos:
    es_valido = Producto.es_precio_valido(producto.precio)
    print(f"¿Precio de '{producto.nombre}' ( ${producto.precio:.2f}) válido? {es_valido}")
print(f"\nTotal de productos creados hasta ahora: {Producto.total_productos()} \n")

tienda.registrar_venta(venta1)
print(cliente1.mostrar_info())
print(f"Total de la venta 1 (Teclado, Mouse, Monitor): ${venta1.total():.2f}")
print(f"Ventas registradas en {tienda.nombre}: {len(tienda.ventas)}")
