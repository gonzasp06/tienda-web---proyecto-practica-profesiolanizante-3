from flask import Flask, request, jsonify, render_template
import mysql.connector

from database import conectar_base_datos

#Subir foto tipo archivo al servidor
import os
from werkzeug.utils import secure_filename 

app = Flask(__name__)

# Carpeta para imágenes
UPLOAD_FOLDER = 'uploads'
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

# Ruta raíz
@app.route('/')
def index():
    return render_template('formulario_carga_producto.html') # HTML

# Ruta para cargar un nuevo producto
# http://127.0.0.1:5000/
# http://127.0.0.1:5000/cargar_producto

@app.route('/cargar_producto', methods=['POST'])
def cargar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
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
        consulta = "INSERT INTO producto (nombre, descripcion, precio, cantidad, foto) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, descripcion, precio, cantidad, ruta_imagen)  # Corrección aquí
        cursor.execute(consulta, valores)
        conexion.commit()
        cursor.close()
        
        return jsonify({"mensaje": "Producto cargado correctamente"}), 200
    else:
        return jsonify({"error": "Método no permitido"}), 405


if __name__ == '__main__':
    app.run(debug=True)
