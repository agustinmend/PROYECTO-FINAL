import pyodbc
import pymysql
import pandas
import tkinter as tk
from tkinter import ttk, messagebox
def agregar_customer():
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title('Datos customer')
    ventana_agregar.geometry('900x600')
    
    etiqueta_ID = tk.Label(ventana_agregar , text='INGRESE ID DEL CLIENTE')
    etiqueta_ID.pack(pady=10)
    entry_ID = tk.Entry(ventana_agregar)
    entry_ID.pack(pady=10)
    
    etiqueta_firtsname = tk.Label(ventana_agregar , text='INGRESE NOMBRE DEL CLIENTE')
    etiqueta_firtsname.pack(pady=10)
    entry_firtsname = tk.Entry(ventana_agregar)
    entry_firtsname.pack(pady=10)

    etiqueta_middlename = tk.Label(ventana_agregar , text='INGRESE SEGUNDO NOMBRE DEL CLIENTE')
    etiqueta_middlename.pack(pady=10)
    entry_middlename = tk.Entry(ventana_agregar)
    entry_middlename.pack(pady=10)
    
    etiqueta_Lastname = tk.Label(ventana_agregar , text='INGRESE APELLIDO DEL CLIENTE')
    etiqueta_Lastname.pack(pady=10)
    entry_lastname = tk.Entry(ventana_agregar)
    entry_lastname.pack(pady=10)
    
    etiqueta_numberphone = tk.Label(ventana_agregar , text='INGRESE NRO DE TELEFONO DEL CLIENTE')
    etiqueta_numberphone.pack(pady=10)
    entry_numberphone = tk.Entry(ventana_agregar)
    entry_numberphone.pack(pady=10)
    
    etiqueta_email = tk.Label(ventana_agregar , text='INGRESE EMAIL DEL CLIENTE')
    etiqueta_email.pack(pady=10)
    entry_email = tk.Entry(ventana_agregar)
    entry_email.pack(pady=10)  
    pass
def agregar_lease():
    pass
def agregar_mantinience():
    pass
def agregar_payment():
    pass
def agregar_room():
    pass
def agregar_staff():
    pass

def agregar():
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title('AGREGAR')
    instruccion = tk.Label(ventana_agregar , text='SELECCIONE QUE DESEA AGREGAR')
    instruccion.pack(pady=10)
    boton_customer = tk.Button(ventana_agregar , text='CUSTOMER' , command= lambda : agregar_customer())
    boton_customer.pack(pady=10)
    boton_lease = tk.Button(ventana_agregar , text='LEASE' , command= lambda : agregar_lease())
    boton_lease.pack(pady=10)
    boton_mantinience = tk.Button(ventana_agregar , text='MANTINIENCE' , command= lambda : agregar_lease())
    boton_mantinience.pack(pady=10)
    boton_payent = tk.Button(ventana_agregar , text='PAYMENT' , command= lambda : agregar_lease())
    boton_payent.pack(pady=10)
    boton_Room = tk.Button(ventana_agregar , text='ROOM' , command= lambda : agregar_lease())
    boton_Room.pack(pady=10)
    boton_staff = tk.Button(ventana_agregar , text='STAFF' , command=lambda : agregar_lease())
    boton_staff.pack(pady=10)
    pass
def mostrar(conn , tabla):
    query = "Select * from " + tabla
    df = pandas.read_sql(query , conn)
    ventana_tabla = tk.Toplevel()
    ventana_tabla.title('TABLA')
    ventana_tabla.geometry("900x600")
    tree = ttk.Treeview(ventana_tabla)
    tree.pack(fill=tk.BOTH , expand= True)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"
    for col in df.columns:
        tree.heading(col , text= col)
        tree.column(col , width=150)

    for _, row in  df.iterrows():
        tree.insert("", "end" , values=list(row))

def mostrar_tablas(conn):
    ventana_tablas = tk.Toplevel()
    ventana_tablas.title('opciones de tabla')
    ventana_tablas.geometry('900x600')
    etiqueta = tk.Label(ventana_tablas , text='SELECCIONA LA TABLA Q DESEAS VER')
    etiqueta.pack(pady=20)
    boton_customer = tk.Button(ventana_tablas , text='CUSTOMER' , command= lambda : mostrar(conn , "customer"))
    boton_customer.pack(pady=20)
    boton_Lease = tk.Button(ventana_tablas , text='LEASE' , command= lambda : mostrar(conn , "lease"))
    boton_Lease.pack(pady=20)
    boton_mantinience = tk.Button(ventana_tablas , text='MANTINIENCE' , command= lambda : mostrar(conn , "mantinience"))
    boton_mantinience.pack(pady=20)
    boton_payent = tk.Button(ventana_tablas , text='PAYMENT' , command= lambda : mostrar(conn , "payment"))
    boton_payent.pack(pady=20)
    boton_Room = tk.Button(ventana_tablas , text='ROOM' , command= lambda : mostrar(conn , "room"))
    boton_Room.pack(pady=20)
    boton_staff = tk.Button(ventana_tablas , text='STAFF' , command=lambda : mostrar(conn , "staff"))
    boton_staff.pack(pady=20)
 
