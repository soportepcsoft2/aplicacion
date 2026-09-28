import tkinter as tk

#ventana principal
main = tk.Tk()
main.title("PCSOFT Tecnología")
main.geometry("600x400")

#barra de menu
menubar = tk.Menu(main)
main.config(menu=menubar)
valores_menu = ("Casos", "Clientes", "Ayuda")

for valor in valores_menu:
    menubar.add_command(label=valor)


#padding y orientación
pad = {"padx": 10, "pady": 10, "sticky": "we"}  # padding y orientación de etiquetas y entradas


#ventana agregar cliente
def agregar_cliente():
    agregar_cliente = tk.Toplevel(main)
    agregar_cliente.title("Agregar Cliente")
    agregar_cliente.geometry("400x300")

    #formulario cliente
    label_nombre = tk.Label(agregar_cliente, text="Nombre:")
    entry_nombre = tk.Entry(agregar_cliente)
    label_nombre.grid(row=0, column=0, **pad)
    entry_nombre.grid(row=0, column=1, **pad)

    label_ruc_dni = tk.Label(agregar_cliente, text="RUC/DNI:")
    entry_ruc_dni = tk.Entry(agregar_cliente)
    label_ruc_dni.grid(row=1, column=0, **pad)
    entry_ruc_dni.grid(row=1, column=1, **pad)

    label_telefono = tk.Label(agregar_cliente, text="Teléfono:")
    entry_telefono = tk.Entry(agregar_cliente)
    label_telefono.grid(row=2, column=0, **pad)
    entry_telefono.grid(row=2, column=1, **pad)

    label_correo = tk.Label(agregar_cliente, text="Correo:")
    entry_correo = tk.Entry(agregar_cliente)
    label_correo.grid(row=3, column=0, **pad)
    entry_correo.grid(row=3, column=1, **pad)

    label_direccion = tk.Label(agregar_cliente, text="Dirección:")
    entry_direccion = tk.Entry(agregar_cliente)
    label_direccion.grid(row=4, column=0, **pad)
    entry_direccion.grid(row=4, column=1, **pad)

    agregar_cliente.grid_columnconfigure(1, weight=1)

  
#ventana agregar servidor
def agregar_servidor():
    agregar_servidor = tk.Toplevel(main)
    agregar_servidor.title("Agregar Servidor")
    agregar_servidor.geometry("400x600")

    #formulario servidor
    label_nombre = tk.Label(agregar_servidor, text="Nombre:")
    entry_nombre = tk.Entry(agregar_servidor)
    label_nombre.grid(row=0, column=0, **pad)
    entry_nombre.grid(row=0, column=1, **pad)

    label_formato = tk.Label(agregar_servidor, text="Formato:")
    entry_formato = tk.Entry(agregar_servidor)
    label_formato.grid(row=1, column=0, **pad)
    entry_formato.grid(row=1, column=1, **pad)

    label_procesador = tk.Label(agregar_servidor, text="Procesador:")
    entry_procesador = tk.Entry(agregar_servidor)
    label_procesador.grid(row=2, column=0, **pad)
    entry_procesador.grid(row=2, column=1, **pad)

    label_memoria = tk.Label(agregar_servidor, text="Memoria:")
    entry_memoria = tk.Entry(agregar_servidor)
    label_memoria.grid(row=3, column=0, **pad)
    entry_memoria.grid(row=3, column=1, **pad)

    label_red = tk.Label(agregar_servidor, text="Red:")
    entry_red = tk.Entry(agregar_servidor)
    label_red.grid(row=4, column=0, **pad)
    entry_red.grid(row=4, column=1, **pad)

    label_almacenamiento = tk.Label(agregar_servidor, text="Almacenamiento:")
    entry_almacenamiento = tk.Entry(agregar_servidor)
    label_almacenamiento.grid(row=5, column=0, **pad)
    entry_almacenamiento.grid(row=5, column=1, **pad)

    label_disco = tk.Label(agregar_servidor, text="Disco duro:")
    entry_disco = tk.Entry(agregar_servidor)
    label_disco.grid(row=6, column=0, **pad)
    entry_disco.grid(row=6, column=1, **pad)

    label_controladora = tk.Label(agregar_servidor, text="Controladora:")
    entry_controladora = tk.Entry(agregar_servidor)
    label_controladora.grid(row=7, column=0, **pad)
    entry_controladora.grid(row=7, column=1, **pad)

    label_fuente = tk.Label(agregar_servidor, text="Fuente de poder:")
    entry_fuente = tk.Entry(agregar_servidor)
    label_fuente.grid(row=8, column=0, **pad)
    entry_fuente.grid(row=8, column=1, **pad)

    label_administracion = tk.Label(agregar_servidor, text="Administración:")
    entry_administracion = tk.Entry(agregar_servidor)
    label_administracion.grid(row=9, column=0, **pad)
    entry_administracion.grid(row=9, column=1, **pad)

    label_garantia = tk.Label(agregar_servidor, text="Garantía:")
    entry_garantia = tk.Entry(agregar_servidor)
    label_garantia.grid(row=10, column=0, **pad)
    entry_garantia.grid(row=10, column=1, **pad)

    agregar_servidor.grid_columnconfigure(1, weight=1)

    boton_copiar = tk.Button(agregar_servidor, text="Copiar Datos", command=copiar_datos)
    boton_copiar.grid(row=11, column=0, **pad, columnspan=2)

    def copiar_datos():
        datos = {
            "Nombre": entry_nombre.get(),
            "Formato": entry_formato.get(),
            "Procesador": entry_procesador.get(),
            "Memoria": entry_memoria.get(),
            "Red": entry_red.get(),
            "Almacenamiento": entry_almacenamiento.get(),
            "Disco duro": entry_disco.get(),
            "Controladora": entry_controladora.get(),
            "Fuente de poder": entry_fuente.get(),
            "Administración": entry_administracion.get(),
            "Garantía": entry_garantia.get()
        }
        #generamos nueva ventana para mostrar los datos copiados
        ventana_datos = tk.Toplevel(agregar_servidor)

        #salida con formato para copiar 
        salida = tk.Text(ventana_datos, height=10, width=50)
        salida.pack(**pad)

#btn_agregar_cliente = tk.Button(main, text="Agregar Cliente", command=agregar_cliente)
#btn_agregar_cliente.pack(pady=20)

btn_agregar_servidor = tk.Button(main, text="Agregar Servidor", command=agregar_servidor)
btn_agregar_servidor.pack(pady=20)


main.mainloop()