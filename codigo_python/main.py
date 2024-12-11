import mispaquetes.funciones as funciones
import mispaquetes.aplicacion as api
import tkinter as tk
conn_sqlserver = None
cursor_sqlserver = None
conn_mysql = None
cursor_mysql = None
try:
    root = tk.Tk()
    root.title('Residencial')
    root.geometry('900x600')
    conn_sqlserver = funciones.conectar_sqlserver()
    conn_mysql = funciones.conectar_mysql()
    Encabezado = tk.Label(root , text="""BIENVENIDO
                          QUE DESEA HACER HOY?""")
    Encabezado.pack(pady=20)
    boton_agregar = tk.Button(root , text= 'AGREGAR' , command=lambda : api.agregar())
    boton_agregar.pack(pady=20)
    boton_mostrar = tk.Button(root , text= 'MOSTRAR TABLA' , command=lambda : api.mostrar_tablas(conn_sqlserver))
    boton_mostrar.pack(pady=20)
    root.mainloop()
except Exception as e:
    print('Ocurrio algo: ',{e})
finally:
    funciones.cerrar_serversql(conn_sqlserver)
    funciones.cerrar_mysql(conn_mysql)