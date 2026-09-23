# Asignatura: Fundamentos de Programación - Semana 15
# Problema de la vida real: Registro de productos en una tienda
# 1. Crear una lista vacía para almacenar los productos de la tienda
print(" ABARROTES HENRY")
productos = []
# 2. Agregar funcionalidad para insertar/agregar datos a la colección
productos.append("Arroz")
productos.append("Azúcar")
productos.append("Aceite")
productos.append("Leche")
# 3. Mostrar de forma clara la información almacenada en pantalla
print("INVENTARIO INICIAL DE LA TIENDA ")
print(productos)
# 4. Incluir al menos una operación básica adicional sobre los datos (Eliminar)
productos.pop(2)
print("INVENTARIO ACTUALIZADO TRAS ELIMINAR ")
print(productos)