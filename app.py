from flask import Flask, request, jsonify, render_template
import mysql.connector

from database import conectar_base_datos

#Subir foto tipo archivo al servidor
import os
from werkzeug.utils import secure_filename 
from math import ceil

app = Flask(__name__)

# Carpeta para imágenes
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# conexión a base de datos
conexion = conectar_base_datos()

# Verificar conexión
# http://127.0.0.1:5000/verificar_conexion
@app.route('/verificar_conexion')
def verificar_conexion():
    if conexion.is_connected():
        return 'Conexión exitosa'
    else:
        return 'Error de conexión'


def obtener_productos():
    cursor= conexion.cursor()
    consulta= 'SELECT * FROM catalogo.producto;'
    cursor.execute(consulta)
    productos=cursor.fetchall()
    cursor.close()
    return productos

productos_por_pagina = 8

def obtener_productos_paginados(pagina):
    inicio = (pagina - 1) * productos_por_pagina
    fin = inicio + productos_por_pagina
    cursor = conexion.cursor()
    consulta = 'SELECT * FROM catalogo.producto LIMIT %s, %s;'
    cursor.execute(consulta, (inicio, productos_por_pagina))
    productos = cursor.fetchall()
    cursor.close()
    return productos

# Ruta raíz
@app.route('/')
@app.route('/<int:pagina>')
def mostrar_catalogo(pagina=1):
    productos = obtener_productos_paginados(pagina)
    total_productos = len(obtener_productos())  
    total_paginas = ceil(total_productos / productos_por_pagina)  # Calcular el total de páginas necesarias
    return render_template('index.html', productos=productos, pagina_actual=pagina, total_paginas=total_paginas)


def filtrar_categoria(categoria_seleccionada):
    cursor = conexion.cursor()
    consulta = 'SELECT * FROM catalogo.producto WHERE categoria = %s;'
    cursor.execute(consulta, (categoria_seleccionada, ))
    productos = cursor.fetchall()
    cursor.close()
    return productos

@app.route('/<categoria>')
def mostrar_catalogo_categoria(categoria):
    productos = filtrar_categoria(categoria)
    return render_template('categoria.html', productos=productos, categoria=categoria)

# Ruta para cargar un nuevo producto
@app.route('/formulario')
def carga_producto():
    return render_template('formulario_carga_producto.html')

@app.route('/cargar_producto', methods=['POST'])
def cargar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        categoria = request.form['categoria']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        foto = request.files['foto']
        
        # Guardar la imagen en el sistema de archivos
        if foto:
            filename = secure_filename(foto.filename)
            ruta_imagen = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            foto.save(ruta_imagen)
        else:
            ruta_imagen = None

        # Ingresar info a la BD
        cursor = conexion.cursor()
        consulta = "INSERT INTO producto (nombre, descripcion, categoria, precio, cantidad, foto) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombre, descripcion, categoria, precio, cantidad, ruta_imagen)
        cursor.execute(consulta, valores)
        conexion.commit()
        cursor.close()
        
        return jsonify({"mensaje": "Producto cargado correctamente"}), 200
    else:
        return jsonify({"error": "Método no permitido"}), 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
