#!/bin/bash
# Script de ejemplo para cargar datos diarios
# Uso: ./cargar_ventas_diarias.sh YYYY-MM-DD

FECHA=$1

if [ -z "$FECHA" ]; then
    echo "Uso: $0 YYYY-MM-DD"
    echo "Ejemplo: $0 2024-01-15"
    exit 1
fi

echo "Cargando ventas del día: $FECHA"

# Verificar que existen los archivos
VENTAS_FILE="ventas_diarias/ventas_$FECHA.csv"
DETALLES_FILE="venta_detalle_diarias/venta_detalle_$FECHA.csv"

if [ ! -f "$VENTAS_FILE" ]; then
    echo "Error: No se encontró el archivo de ventas: $VENTAS_FILE"
    exit 1
fi

if [ ! -f "$DETALLES_FILE" ]; then
    echo "Error: No se encontró el archivo de detalles: $DETALLES_FILE"
    exit 1
fi

echo "Archivos encontrados:"
echo "- $VENTAS_FILE"
echo "- $DETALLES_FILE"

# Aquí puedes agregar los comandos para cargar a tu base de datos
# Ejemplo para PostgreSQL:
# psql -d tu_base_datos -c "\COPY ventas FROM '$VENTAS_FILE' CSV HEADER;"
# psql -d tu_base_datos -c "\COPY venta_detalle FROM '$DETALLES_FILE' CSV HEADER;"

# Ejemplo para MySQL:
# mysql -u usuario -p tu_base_datos -e "LOAD DATA INFILE '$VENTAS_FILE' INTO TABLE ventas FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;"
# mysql -u usuario -p tu_base_datos -e "LOAD DATA INFILE '$DETALLES_FILE' INTO TABLE venta_detalle FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;"

echo "Carga completada para el día: $FECHA"
