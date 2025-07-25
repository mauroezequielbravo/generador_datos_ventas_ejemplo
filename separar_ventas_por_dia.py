import csv
import os
from datetime import datetime
from collections import defaultdict

def separar_ventas_por_dia():
    """Separa las ventas y detalles de ventas por día, creando un archivo por día"""
    
    # Crear directorio para los archivos diarios
    os.makedirs('ventas_diarias', exist_ok=True)
    os.makedirs('venta_detalle_diarias', exist_ok=True)
    
    # Leer ventas
    ventas_por_dia = defaultdict(list)
    ventas_info = {}  # Para almacenar información de cada venta
    
    print("Leyendo archivo de ventas...")
    with open('ventas.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            fecha = row['fecha_venta']
            ventas_por_dia[fecha].append(row)
            ventas_info[row['id_venta']] = row
    
    # Leer detalles de ventas
    detalles_por_dia = defaultdict(list)
    
    print("Leyendo archivo de detalles de ventas...")
    with open('venta_detalle.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id_venta = row['id_venta']
            if id_venta in ventas_info:
                fecha = ventas_info[id_venta]['fecha_venta']
                detalles_por_dia[fecha].append(row)
    
    # Generar archivos por día
    print("Generando archivos por día...")
    
    for fecha in sorted(ventas_por_dia.keys()):
        # Formatear fecha para nombre de archivo
        fecha_obj = datetime.strptime(fecha, '%Y-%m-%d')
        nombre_archivo = fecha_obj.strftime('%Y-%m-%d')
        
        # Archivo de ventas del día
        archivo_ventas = f'ventas_diarias/ventas_{nombre_archivo}.csv'
        with open(archivo_ventas, 'w', newline='', encoding='utf-8') as file:
            if ventas_por_dia[fecha]:
                writer = csv.DictWriter(file, fieldnames=ventas_por_dia[fecha][0].keys())
                writer.writeheader()
                writer.writerows(ventas_por_dia[fecha])
        
        # Archivo de detalles de ventas del día
        archivo_detalles = f'venta_detalle_diarias/venta_detalle_{nombre_archivo}.csv'
        with open(archivo_detalles, 'w', newline='', encoding='utf-8') as file:
            if detalles_por_dia[fecha]:
                writer = csv.DictWriter(file, fieldnames=detalles_por_dia[fecha][0].keys())
                writer.writeheader()
                writer.writerows(detalles_por_dia[fecha])
        
        print(f"Generado: {archivo_ventas} ({len(ventas_por_dia[fecha])} ventas)")
        print(f"Generado: {archivo_detalles} ({len(detalles_por_dia[fecha])} detalles)")
    
    # Crear archivo de resumen
    crear_resumen_diario(ventas_por_dia, detalles_por_dia)
    
    print(f"\n¡Archivos generados exitosamente!")
    print(f"Directorio ventas_diarias: {len(os.listdir('ventas_diarias'))} archivos")
    print(f"Directorio venta_detalle_diarias: {len(os.listdir('venta_detalle_diarias'))} archivos")

def crear_resumen_diario(ventas_por_dia, detalles_por_dia):
    """Crea un archivo de resumen con estadísticas diarias"""
    
    print("Creando archivo de resumen diario...")
    
    with open('resumen_ventas_diarias.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['fecha', 'total_ventas', 'total_detalles', 'monto_total_dia', 'promedio_venta'])
        
        for fecha in sorted(ventas_por_dia.keys()):
            ventas_del_dia = ventas_por_dia[fecha]
            detalles_del_dia = detalles_por_dia[fecha]
            
            total_ventas = len(ventas_del_dia)
            total_detalles = len(detalles_del_dia)
            monto_total = sum(int(venta['monto_total']) for venta in ventas_del_dia)
            promedio_venta = monto_total / total_ventas if total_ventas > 0 else 0
            
            writer.writerow([
                fecha,
                total_ventas,
                total_detalles,
                monto_total,
                round(promedio_venta, 2)
            ])
    
    print("Archivo de resumen creado: resumen_ventas_diarias.csv")

def crear_script_carga_diaria():
    """Crea un script de ejemplo para cargar datos diarios"""
    
    script_content = '''#!/bin/bash
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
# psql -d tu_base_datos -c "\\COPY ventas FROM '$VENTAS_FILE' CSV HEADER;"
# psql -d tu_base_datos -c "\\COPY venta_detalle FROM '$DETALLES_FILE' CSV HEADER;"

# Ejemplo para MySQL:
# mysql -u usuario -p tu_base_datos -e "LOAD DATA INFILE '$VENTAS_FILE' INTO TABLE ventas FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' IGNORE 1 LINES;"
# mysql -u usuario -p tu_base_datos -e "LOAD DATA INFILE '$DETALLES_FILE' INTO TABLE venta_detalle FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' IGNORE 1 LINES;"

echo "Carga completada para el día: $FECHA"
'''
    
    with open('cargar_ventas_diarias.sh', 'w', encoding='utf-8') as file:
        file.write(script_content)
    
    # Hacer el script ejecutable (en sistemas Unix)
    try:
        import stat
        os.chmod('cargar_ventas_diarias.sh', stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
    except:
        pass
    
    print("Script de carga diaria creado: cargar_ventas_diarias.sh")

if __name__ == "__main__":
    separar_ventas_por_dia()
    crear_script_carga_diaria() 