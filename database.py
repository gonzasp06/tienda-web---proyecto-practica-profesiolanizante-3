import mysql.connector

def conectar_base_datos():
    return mysql.connector.connect(
        host="localhost",  
        user="publico",  
        password="Userpublic@",  
        database="catalogo" 
    )