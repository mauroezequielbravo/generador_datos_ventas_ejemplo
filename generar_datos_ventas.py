import csv
import random
from datetime import datetime, timedelta
import os

# Configuración de datos
random.seed(42)  # Para reproducibilidad

# Nombres y datos para generar contenido realista
nombres_empleados = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Luis Rodríguez",
    "Carmen Sánchez", "Jorge Torres", "Isabel Ruiz", "Miguel Jiménez", "Elena Moreno",
    "Roberto Silva", "Patricia Vargas", "Fernando Castro", "Lucía Morales", "Diego Herrera",
    "Sofia Ortega", "Ricardo Mendoza", "Valeria Rojas", "Hector Guzmán", "Natalia Paredes",
    "Oscar Vega", "Camila Fuentes", "Andrés Valenzuela", "Daniela Espinoza", "Felipe Carrasco",
    "Gabriela Soto", "Manuel Contreras", "Valentina Miranda", "Sebastian Bravo", "Antonella Salazar",
    "Matias Flores", "Javiera Reyes", "Nicolas Gutierrez", "Constanza Valdes", "Benjamin Araya",
    "Catalina Sepulveda", "Maximiliano Tapia", "Amanda Leiva", "Cristobal Munoz", "Francisca Vera",
    "Ignacio Molina", "Trinidad Figueroa", "Agustin Cortes", "Antonia Campos", "Joaquin Silva",
    "Emilia Vidal", "Tomas Poblete", "Josefa Lagos", "Felipe Peña", "Catalina Bustos"
]

nombres_productos = [
    "Laptop HP Pavilion", "Mouse Inalámbrico Logitech", "Teclado Mecánico RGB", "Monitor Samsung 24\"",
    "Auriculares Sony WH-1000XM4", "Webcam Logitech C920", "Disco Duro Externo 1TB", "Memoria USB 32GB",
    "Cargador Inalámbrico", "Cable HDMI 2m", "Adaptador USB-C", "Hub USB 4 puertos", "Soporte Monitor",
    "Alfombrilla Gaming", "Lámpara LED Escritorio", "Organizador Cables", "Funda Laptop 15\"",
    "Base Refrigeración", "Micrófono Blue Yeti", "Pendrive 128GB", "Cable Ethernet 5m",
    "Teclado Numérico", "Mouse Pad Gaming", "Cable VGA", "Adaptador HDMI-VGA", "Cargador Portátil",
    "Soporte Tablet", "Cable Lightning", "Cable Micro USB", "Adaptador Bluetooth", "Hub Ethernet"
]

nombres_proveedores = [
    "TechCorp Solutions", "Digital Dynamics", "Innovation Tech", "Smart Systems", "Future Electronics",
    "Global Tech Supply", "Premium Components", "Elite Technology", "Advanced Solutions", "Tech Masters",
    "Digital World", "Smart Electronics", "Tech Innovations", "Future Systems", "Global Solutions",
    "Premium Tech", "Elite Electronics", "Advanced Tech", "Tech Solutions", "Digital Systems",
    "Smart World", "Tech Dynamics", "Future Electronics", "Global Innovations", "Premium Systems",
    "Elite Solutions", "Advanced World", "Tech Dynamics", "Digital Innovations", "Smart Solutions"
]

nombres_clientes = [
    "Alejandro Morales", "Valentina Silva", "Sebastian Torres", "Isabella Rojas", "Matias Herrera",
    "Sofia Castro", "Nicolas Ortega", "Camila Mendoza", "Benjamin Guzman", "Antonella Paredes",
    "Maximiliano Vega", "Trinidad Fuentes", "Agustin Valenzuela", "Emilia Espinoza", "Tomas Carrasco",
    "Josefa Soto", "Felipe Contreras", "Catalina Miranda", "Joaquin Bravo", "Antonia Salazar",
    "Ignacio Flores", "Francisca Reyes", "Cristobal Gutierrez", "Amanda Valdes", "Maximiliano Araya",
    "Daniela Sepulveda", "Oscar Tapia", "Valeria Leiva", "Fernando Munoz", "Lucia Vera",
    "Diego Molina", "Carmen Figueroa", "Roberto Cortes", "Patricia Campos", "Hector Silva",
    "Natalia Vidal", "Ricardo Poblete", "Elena Lagos", "Miguel Peña", "Isabel Bustos",
    "Luis Morales", "Ana Silva", "Carlos Torres", "María Rojas", "Juan Herrera",
    "Sofia Castro", "Luis Ortega", "Carmen Mendoza", "Roberto Guzman", "Patricia Paredes",
    "Hector Vega", "Natalia Fuentes", "Ricardo Valenzuela", "Elena Espinoza", "Miguel Carrasco",
    "Isabel Soto", "Luis Contreras", "Ana Miranda", "Carlos Bravo", "María Salazar",
    "Juan Flores", "Sofia Reyes", "Luis Gutierrez", "Carmen Valdes", "Roberto Araya",
    "Patricia Sepulveda", "Hector Tapia", "Natalia Leiva", "Ricardo Munoz", "Elena Vera",
    "Miguel Molina", "Isabel Figueroa", "Luis Cortes", "Ana Campos", "Carlos Silva",
    "María Vidal", "Juan Poblete", "Sofia Lagos", "Luis Peña", "Carmen Bustos",
    "Roberto Morales", "Patricia Silva", "Hector Torres", "Natalia Rojas", "Ricardo Herrera",
    "Elena Castro", "Miguel Ortega", "Isabel Mendoza", "Luis Guzman", "Ana Paredes",
    "Carlos Vega", "María Fuentes", "Juan Valenzuela", "Sofia Espinoza", "Luis Carrasco",
    "Carmen Soto", "Roberto Contreras", "Patricia Miranda", "Hector Bravo", "Natalia Salazar",
    "Ricardo Flores", "Elena Reyes", "Miguel Gutierrez", "Isabel Valdes", "Luis Araya",
    "Ana Sepulveda", "Carlos Tapia", "María Leiva", "Juan Munoz", "Sofia Vera",
    "Luis Molina", "Carmen Figueroa", "Roberto Cortes", "Patricia Campos", "Hector Silva",
    "Natalia Vidal", "Ricardo Poblete", "Elena Lagos", "Miguel Peña", "Isabel Bustos",
    "Luis Morales", "Ana Silva", "Carlos Torres", "María Rojas", "Juan Herrera",
    "Sofia Castro", "Luis Ortega", "Carmen Mendoza", "Roberto Guzman", "Patricia Paredes",
    "Hector Vega", "Natalia Fuentes", "Ricardo Valenzuela", "Elena Espinoza", "Miguel Carrasco",
    "Isabel Soto", "Luis Contreras", "Ana Miranda", "Carlos Bravo", "María Salazar",
    "Juan Flores", "Sofia Reyes", "Luis Gutierrez", "Carmen Valdes", "Roberto Araya",
    "Patricia Sepulveda", "Hector Tapia", "Natalia Leiva", "Ricardo Munoz", "Elena Vera",
    "Miguel Molina", "Isabel Figueroa", "Luis Cortes", "Ana Campos", "Carlos Silva",
    "María Vidal", "Juan Poblete", "Sofia Lagos", "Luis Peña", "Carmen Bustos",
    "Roberto Morales", "Patricia Silva", "Hector Torres", "Natalia Rojas", "Ricardo Herrera",
    "Elena Castro", "Miguel Ortega", "Isabel Mendoza", "Luis Guzman", "Ana Paredes",
    "Carlos Vega", "María Fuentes", "Juan Valenzuela", "Sofia Espinoza", "Luis Carrasco",
    "Carmen Soto", "Roberto Contreras", "Patricia Miranda", "Hector Bravo", "Natalia Salazar",
    "Ricardo Flores", "Elena Reyes", "Miguel Gutierrez", "Isabel Valdes", "Luis Araya",
    "Ana Sepulveda", "Carlos Tapia", "María Leiva", "Juan Munoz", "Sofia Vera",
    "Luis Molina", "Carmen Figueroa", "Roberto Cortes", "Patricia Campos", "Hector Silva",
    "Natalia Vidal", "Ricardo Poblete", "Elena Lagos", "Miguel Peña", "Isabel Bustos"
]

nombres_establecimientos = [
    "Centro Comercial Plaza Norte", "Mall Plaza Vespucio", "Costanera Center", "Parque Arauco",
    "Alto Las Condes", "Mall Florida Center", "Plaza Oeste", "Mall Plaza Tobalaba",
    "Mall Plaza Egaña", "Plaza Norte 2", "Mall Plaza Sur", "Plaza Oeste 2",
    "Mall Plaza Los Dominicos", "Plaza Vespucio 2", "Mall Plaza Maipú", "Plaza Norte 3"
]

direcciones_establecimientos = [
    "Av. Américo Vespucio 1737, Huechuraba", "Av. Vicuña Mackenna 7110, La Florida",
    "Av. Andrés Bello 2425, Providencia", "Av. Kennedy 5413, Las Condes",
    "Av. Kennedy 9001, Las Condes", "Av. Vicuña Mackenna 5870, La Florida",
    "Av. Américo Vespucio 1501, Pudahuel", "Av. Las Condes 13451, Las Condes",
    "Av. Las Condes 13451, Las Condes", "Av. Américo Vespucio 1737, Huechuraba",
    "Av. Gran Avenida 9292, San Miguel", "Av. Américo Vespucio 1501, Pudahuel",
    "Av. Apoquindo 6570, Las Condes", "Av. Vicuña Mackenna 7110, La Florida",
    "Av. Pajaritos 1317, Maipú", "Av. Américo Vespucio 1737, Huechuraba"
]

def generar_email(nombre):
    """Genera email con errores ocasionales"""
    nombre_limpio = nombre.lower().replace(' ', '')
    dominios = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'live.com']
    
    # 5% de probabilidad de error en email
    if random.random() < 0.05:
        return f"{nombre_limpio}@invalid-email"  # Email inválido
    elif random.random() < 0.03:
        return f"{nombre_limpio}@gmail"  # Dominio incompleto
    else:
        return f"{nombre_limpio}@{random.choice(dominios)}"

def generar_fecha_nacimiento():
    """Genera fecha de nacimiento con errores ocasionales"""
    # 3% de probabilidad de error en fecha
    if random.random() < 0.03:
        return "32/13/2023"  # Fecha inválida
    elif random.random() < 0.02:
        return "00/00/0000"  # Fecha nula
    else:
        año = random.randint(1960, 2005)
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)
        return f"{dia:02d}/{mes:02d}/{año}"

def generar_precio():
    """Genera precio con errores ocasionales"""
    # 2% de probabilidad de precio negativo
    if random.random() < 0.02:
        return random.randint(-1000, -100)
    # 1% de probabilidad de precio cero
    elif random.random() < 0.01:
        return 0
    else:
        return random.randint(5000, 500000)

def generar_stock():
    """Genera stock con errores ocasionales"""
    # 3% de probabilidad de stock negativo
    if random.random() < 0.03:
        return random.randint(-50, -1)
    else:
        return random.randint(0, 200)

def generar_fecha_venta(fecha_inicio, fecha_fin):
    """Genera fecha de venta con errores ocasionales"""
    # 1% de probabilidad de fecha futura
    if random.random() < 0.01:
        return (fecha_fin + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
    else:
        dias = random.randint(0, (fecha_fin - fecha_inicio).days)
        return (fecha_inicio + timedelta(days=dias)).strftime("%Y-%m-%d")

# Generar datos
fecha_inicio = datetime(2024, 1, 1)
fecha_fin = datetime(2024, 1, 30)

# 1. Empleados
print("Generando empleados...")
with open('empleados.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id_empleado', 'nombre'])
    
    for i in range(50):
        # 2% de probabilidad de nombre vacío
        if random.random() < 0.02:
            nombre = ""
        else:
            nombre = nombres_empleados[i]
        writer.writerow([i+1, nombre])

# 2. Productos
print("Generando productos...")
with open('productos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id_producto', 'nombre', 'precio', 'descripcion'])
    
    for i in range(1000):
        nombre = nombres_productos[i % len(nombres_productos)] + f" {i+1}"
        precio = generar_precio()
        descripcion = f"Descripción del producto {nombre}"
        
        # 1% de probabilidad de descripción vacía
        if random.random() < 0.01:
            descripcion = ""
            
        writer.writerow([i+1, nombre, precio, descripcion])

# 3. Proveedores
print("Generando proveedores...")
with open('proveedores.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id_proveedor', 'nombre'])
    
    for i in range(30):
        nombre = nombres_proveedores[i]
        writer.writerow([i+1, nombre])

# 4. Clientes
print("Generando clientes...")
with open('clientes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id_cliente', 'nombre', 'email', 'fecha_nacimiento'])
    
    for i in range(200):
        nombre = nombres_clientes[i]
        email = generar_email(nombre)
        fecha_nacimiento = generar_fecha_nacimiento()
        writer.writerow([i+1, nombre, email, fecha_nacimiento])

# 5. Establecimientos
print("Generando establecimientos...")
with open('establecimientos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id_establecimiento', 'nombre', 'direccion', 'horario_apertura', 'horario_cierre'])
    
    for i in range(16):
        nombre = nombres_establecimientos[i]
        direccion = direcciones_establecimientos[i]
        horario_apertura = "09:00"
        horario_cierre = "22:00"
        writer.writerow([i+1, nombre, direccion, horario_apertura, horario_cierre])

# 6. Stock
print("Generando stock...")
with open('stock.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id_stock', 'id_producto', 'stock'])
    
    for i in range(1000):
        stock = generar_stock()
        writer.writerow([i+1, i+1, stock])

# 7. Ventas
print("Generando ventas...")
ventas = []
id_venta = 1

# Asegurar que cada cliente tenga al menos una venta en el mes
for cliente_id in range(1, 201):
    fecha_venta = generar_fecha_venta(fecha_inicio, fecha_fin)
    empleado_id = random.randint(1, 50)
    monto_total = random.randint(10000, 500000)
    ventas.append([id_venta, cliente_id, empleado_id, monto_total, fecha_venta])
    id_venta += 1

# Agregar ventas adicionales aleatorias
ventas_adicionales = random.randint(800, 1200)
for _ in range(ventas_adicionales):
    cliente_id = random.randint(1, 200)
    fecha_venta = generar_fecha_venta(fecha_inicio, fecha_fin)
    empleado_id = random.randint(1, 50)
    monto_total = random.randint(10000, 500000)
    ventas.append([id_venta, cliente_id, empleado_id, monto_total, fecha_venta])
    id_venta += 1

with open('ventas.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id_venta', 'id_cliente', 'id_empleado', 'monto_total', 'fecha_venta'])
    writer.writerows(ventas)

# 8. Venta Detalle
print("Generando detalles de ventas...")
with open('venta_detalle.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['id_venta_detalle', 'id_venta', 'id_producto', 'cantidad', 'precio_unitario'])
    
    id_venta_detalle = 1
    for venta in ventas:
        # Cada venta tiene entre 1 y 5 productos
        num_productos = random.randint(1, 5)
        for _ in range(num_productos):
            id_producto = random.randint(1, 1000)
            cantidad = random.randint(1, 10)
            precio_unitario = random.randint(5000, 100000)
            writer.writerow([id_venta_detalle, venta[0], id_producto, cantidad, precio_unitario])
            id_venta_detalle += 1

print("¡Archivos CSV generados exitosamente!")
print("Archivos creados:")
print("- empleados.csv")
print("- productos.csv") 
print("- proveedores.csv")
print("- clientes.csv")
print("- establecimientos.csv")
print("- stock.csv")
print("- ventas.csv")
print("- venta_detalle.csv") 