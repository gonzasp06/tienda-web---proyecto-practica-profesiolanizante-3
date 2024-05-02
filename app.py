from flask import Flask, request, jsonify, render_template, session, redirect, url_for  
import mysql.connector
from database import conectar_base_datos
import os #Subir foto tipo archivo al servidor
from werkzeug.utils import secure_filename 
from math import ceil #calcular el numero de paginas
import bcrypt #encriptar
from flask_mail import Mail, Message #enviar email
from flask_session import Session
from datetime import datetime

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'smarthouse889@gmail.com'
app.config['MAIL_PASSWORD'] = 'qyyj qqnn ossz vlob'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'smarthouse889@gmail.com'
# Inicializar Flask-Mail  
mail = Mail(app)

#configuracion de la sesion
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = False
app.secret_key = 'smarthouse123@'
Session(app)

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

productos_por_pagina = 9

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

########### GESTIÓN DE CUENTAS - NUEVOS USUARIOS Y VERIFICACION ############

@app.route('/nuevo_usuario')
def crear_usuario():
    return render_template('f_nuevo_usuario.html')

#cifrado de contraseñas
def cifrar_contraseñas(contraseña):
    hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

#verificar contraseña cifrada
def verificar_contraseña(contraseña, hashed_password):
    return bcrypt.checkpw(contraseña.encode('utf-8'), hashed_password.encode('utf-8'))

@app.route('/cargar_usuario', methods=['POST'])
def cargar_usuario():
    if request.method == 'POST':
        datos_usuario = request.form
        # Cifrar la contraseña
        hashed_password = cifrar_contraseñas(datos_usuario['contraseña'])
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuario (nombre, apellido, email, contraseña, is_admin) VALUES (%s, %s, %s, %s, %s)",(datos_usuario['nombre'], datos_usuario['apellido'], datos_usuario['email'], hashed_password, 0))
        conexion.commit()
        cursor.close()
        enviar_correo(datos_usuario['email'])
        return jsonify({"mensaje": "Cuenta creada"}), 200
    else:
        return jsonify({"error": "Método no permitido"}), 405

@app.route('/verificar', methods=['POST'])
def verificar_usuario():
    if request.method == 'POST':
        email = request.form['email']
        contraseña_verificar = request.form['contraseña']
        usuario = buscar_usuario(email)
        if usuario:
            contraseña = (usuario['contraseña'])
            # Verificando la contraseña proporcionada con la almacenada
            if verificar_contraseña(contraseña_verificar, contraseña) == True:
                mensaje = f"¡Usuario encontrado! Hola, {usuario['nombre']}."
                session['usuario'] = usuario
                print(session)
                registrar_sesion(usuario['id'])
                # Verificar si la clave 'rol' está en la sesión antes de acceder a su valor
                if 'rol' in session and session['rol'] == 1:
                    print('Administrador')
                elif 'rol' in session and session['rol'] == 0:
                    print('Cliente')
                return jsonify({"mensaje": mensaje, "usuario": usuario}), 200
            else:
                return jsonify({"error": "Credenciales incorrectas"}), 401
            
        else:
            return jsonify({"error": "Credenciales incorrectas"}), 401
    else:
        return jsonify({"error": "Método no permitido"}), 405
    
def buscar_usuario(email):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM catalogo.usuario WHERE email = %s", (email,))
    usuario = cursor.fetchone()
    cursor.close() 
    if usuario:
        return {
            'id': usuario[0], 
            'nombre': usuario[1],  
            'apellido': usuario[2], 
            'email': usuario[3],       
            'contraseña': usuario[4],
            'rol': usuario[5]
        }
    else:
        return None

def registrar_sesion(idusuario):
    cursor = conexion.cursor()
    fecha_hora = datetime.now()
    cursor.execute('INSERT INTO sesiones(fecha_sesion, idusuario) VALUES (%s, %s)', (fecha_hora, idusuario))
    conexion.commit()
    cursor.close()

@app.route('/cuenta', methods=['GET', 'POST'])
def acceso_cuentas():
    if request.method == 'POST':
        email = request.form['email']
        contraseña = request.form['contraseña']
        usuario = buscar_usuario(email)
        if usuario and verificar_contraseña(contraseña, usuario['contraseña']):
            return redirect(url_for('index'))
        else:
            return jsonify({"error": "Credenciales incorrectas"}), 401
    else:
        return render_template('f_acceso.html')
    
@app.route('/acceso')
def render_acceso():
    return render_template('acceso.html') 

@app.route('/cerrar_sesion', methods=['POST'])
def cerrar_sesion():
    # Eliminar la sesión del usuario
    session.clear()
    # Devolver una respuesta exitosa
    return 'Sesión cerrada', 200

###### Mandar un correo de confirmacion de cuenta creada

def enviar_correo(email):
    mensaje = render_template('confirm_email.html', email=email)
    subject = 'Confirmación de correo'
    destinatario = [email]
    correo = Message(subject, recipients=destinatario)
    correo.html = mensaje
    mail.send(correo)

###################### CARGA DE PRODUCTOS ##################################################r
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

########### GESTIÓN DE CUENTAS - ACTUALIZAR ROLES Y ELIMINAR CUENTAS ############R

@app.route('/usuarios')
def usuarios():
    usuarios = obtener_usuarios()
    return render_template('gestion_usuarios.html', usuarios=usuarios)

def obtener_usuarios():
    cursor = conexion.cursor()
    consulta = 'SELECT idusuario, nombre, apellido, email, is_admin FROM catalogo.usuario;'
    cursor.execute(consulta )
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios

@app.route('/actualizar_rol/<int:usuario_id>', methods=['POST'])
def actualizar_rol(usuario_id):
    nuevo_estado = request.json['isAdmin']
    cursor = conexion.cursor()
    accion = 'UPDATE catalogo.usuario SET is_admin = %s WHERE idusuario = %s;'
    cursor.execute(accion, (nuevo_estado, usuario_id))
    conexion.commit()
    cursor.close()
    return "Rol de usuario actualizado", 200

@app.route('/eliminar/<int:usuario_id>', methods=['POST'])
def eliminar_usuario(usuario_id):
    cursor = conexion.cursor()
    accion = 'DELETE FROM catalogo.usuario WHERE idusuario = %s;'
    cursor.execute(accion, (usuario_id,))
    conexion.commit()
    cursor.close()
    return jsonify({"mensaje": "Usuario eliminado correctamente", "usuario_id": usuario_id})
#### #HISTORIAL DE SESIONES DE USUARIO

@app.route('/historial_sesiones/<int:usuario_id>', methods=['GET'])
def mostrar_sesiones(usuario_id):
    cursor = conexion.cursor()
    accion = 'SELECT fecha_sesion FROM catalogo.sesiones WHERE idusuario = %s'
    cursor.execute(accion, (usuario_id,))
    sesiones = cursor.fetchall()
    usuario = obtener_nombre_usuario(usuario_id)
    conexion.commit()
    cursor.close()
    return render_template('historial_sesiones.html', sesiones=sesiones, nombre_usuario=usuario)

def obtener_nombre_usuario(usuario_id):
    cursor = conexion.cursor()
    consulta = 'SELECT nombre FROM catalogo.usuario WHERE idusuario = %s;'
    cursor.execute(consulta, (usuario_id,))
    nombre = cursor.fetchone()[0]
    cursor.close()
    return nombre

#############################################################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)