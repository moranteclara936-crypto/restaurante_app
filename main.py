# Archivo principal del programa

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Restaurante El Buen Sabor")

# Crear productos
producto1 = Producto("Hamburguesa", 5.50, "Comida")
producto2 = Producto("Pizza", 8.00, "Comida")
producto3 = Producto("Jugo Natural", 2.50, "Bebida")

# Crear clientes
cliente1 = Cliente("María López", "1723456789")
cliente2 = Cliente("Carlos Pérez", "1712345678")

# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print("===================================")
print(restaurante.nombre)
print("===================================")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()