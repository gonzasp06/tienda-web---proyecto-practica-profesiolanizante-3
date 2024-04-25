import mysql.connector

def conectar_base_datos():
    return mysql.connector.connect(
        host="localhost",  
        user="root",  
        password="123456789",  
        database="catalogo" 
    )
