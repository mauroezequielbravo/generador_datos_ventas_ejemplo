# Datos de Ventas - Archivos CSV

Este proyecto contiene archivos CSV generados para simular un sistema de ventas con datos que incluyen errores para propósitos de validación y transformación.

## Generación de Datos

Para generar los archivos CSV, ejecuta los siguientes comandos:

```bash
# 1. Generar todos los archivos CSV base
python generar_datos_ventas.py

# 2. Separar ventas por día (opcional)
python separar_ventas_por_dia.py
```

### Requisitos
- Python 3.6 o superior
- No se requieren dependencias adicionales (solo módulos estándar de Python)

## Archivos Generados

### 1. empleados.csv
- **Registros**: 50 empleados
- **Campos**: id_empleado, nombre
- **Errores incluidos**: Nombres vacíos (2% de probabilidad)

### 2. productos.csv
- **Registros**: 1,000 productos
- **Campos**: id_producto, nombre, precio, descripcion
- **Errores incluidos**: 
  - Precios negativos (2% de probabilidad)
  - Precios cero (1% de probabilidad)
  - Descripciones vacías (1% de probabilidad)

### 3. proveedores.csv
- **Registros**: 30 proveedores
- **Campos**: id_proveedor, nombre

### 4. clientes.csv
- **Registros**: 200 clientes
- **Campos**: id_cliente, nombre, email, fecha_nacimiento
- **Errores incluidos**:
  - Emails inválidos (5% de probabilidad)
  - Dominios incompletos (3% de probabilidad)
  - Fechas de nacimiento inválidas (3% de probabilidad)
  - Fechas nulas (2% de probabilidad)

### 5. establecimientos.csv
- **Registros**: 16 establecimientos
- **Campos**: id_establecimiento, nombre, direccion, horario_apertura, horario_cierre

### 6. stock.csv
- **Registros**: 1,000 registros de stock
- **Campos**: id_stock, id_producto, stock
- **Errores incluidos**: Stock negativo (3% de probabilidad)

### 7. ventas.csv
- **Registros**: ~1,230 ventas (200 mínimas + ventas adicionales)
- **Campos**: id_venta, id_cliente, id_empleado, monto_total, fecha_venta
- **Características**:
  - Cada cliente tiene al menos una venta en el mes
  - Ventas distribuidas en 30 días (enero 2024)
  - Fechas futuras ocasionales (1% de probabilidad)

### 8. venta_detalle.csv
- **Registros**: ~3,650 detalles de venta
- **Campos**: id_venta_detalle, id_venta, id_producto, cantidad, precio_unitario
- **Características**: Cada venta tiene entre 1 y 5 productos

## Archivos Diarios (Opcional)

Si ejecutas `python separar_ventas_por_dia.py`, se crearán los siguientes directorios:

### ventas_diarias/
- Archivos: `ventas_YYYY-MM-DD.csv`
- Contiene las ventas separadas por día
- Útil para simular cargas diarias

### venta_detalle_diarias/
- Archivos: `venta_detalle_YYYY-MM-DD.csv`
- Contiene los detalles de ventas separados por día
- Corresponde a las ventas del día correspondiente

### resumen_ventas_diarias.csv
- Resumen estadístico de ventas por día
- Campos: fecha, total_ventas, total_detalles, monto_total_dia, promedio_venta

## Período de Datos
- **Fecha inicio**: 1 de enero de 2024
- **Fecha fin**: 30 de enero de 2024
- **Duración**: 30 días

## Volumen de Datos
- **Empleados**: 50
- **Clientes**: 200
- **Productos**: 1,000
- **Proveedores**: 30
- **Establecimientos**: 16
- **Ventas**: ~1,230
- **Detalles de venta**: ~3,650

## Errores Incluidos para Validación

### Emails
- `usuario@invalid-email` - Dominio inválido
- `usuario@gmail` - Dominio incompleto

### Fechas
- `32/13/2023` - Fecha inválida
- `00/00/0000` - Fecha nula

### Precios
- Valores negativos (ej: -500)
- Valores cero

### Stock
- Valores negativos (ej: -25)

### Fechas de Venta
- Fechas futuras (posteriores al 30 de enero)

## Uso

Los archivos están listos para ser utilizados en procesos de ETL, validación de datos, y transformaciones. Los errores incluidos permiten probar:

1. **Validaciones de integridad**
2. **Transformaciones de datos**
3. **Limpieza de datos**
4. **Reglas de negocio**

## Generación

Los archivos fueron generados usando el script `generar_datos_ventas.py` que incluye:
- Datos realistas en español
- Errores controlados para testing
- Distribución temporal de ventas
- Relaciones entre tablas mantenidas

## Carga Diaria

Se incluye un script de ejemplo `cargar_ventas_diarias.sh` para cargar datos diarios:

```bash
# Cargar ventas de un día específico
./cargar_ventas_diarias.sh 2024-01-15
```

El script verifica la existencia de los archivos y proporciona ejemplos de comandos para:
- PostgreSQL
- MySQL

Puedes modificar el script según tu base de datos específica. 