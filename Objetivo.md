

# Objetivo
Tener archivos csv de las siguientes tablas. Quiero que se generen archivos para simular 30 dias de ventas, nuevos clientes, cambio en los stcok a medida que pasan los dias.
Tambien quiero que los datos tengan errores para poder simular validaciones y transformaciones cuando sean consumidos.
Dentro de lo posible quiero un volumen de datos medio, por ejemplo unos 50 empleados. 200 clientes. 1000 productos. 30 proveedores. Ventas para todos los clientes por 30 dias, por lo menos tiene que tener una compra en el mes.

# Tablas
- Empleados
    - id_empleado
    - nombre
- Productos
    - id_producto
    - nombre
    - precio
    - descripcion
- Proveedores
    - id_proveedor
    - nombre
- Clientes
    - id_cliente
    - nombre
    - email
    - fecha_nacimiento
- Establecimientos
    - id_establecimiento
    - nombre
    - direccion
    - horario_apertura
    - horario_cierre
- Stock
    - id_stock
    - id_producto
    - stock
- Ventas
    - id_venta
    - id_cliente
    - id_empleado
    - monto_total
    - fecha-venta
- venta_detalle
    - id_venta_detalle
    - id_venta
    - id_producto
    - cantidad
    - precio_unitario










