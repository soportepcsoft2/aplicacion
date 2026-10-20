import tkinter as tk

#ventana principal
main = tk.Tk()
main.title("PCSOFT Tecnología")
main.geometry("900x600")

#barra de menu
main.option_add('*tearOff', tk.FALSE)

menubar = tk.Menu(main)
main.config(menu=menubar)

#menu donde se agregan los casos de soporte
menu_soporte = tk.Menu(menubar)
menubar.add_cascade(label="Soporte", menu=menu_soporte)
menu_soporte.add_command(label="Agregar Caso", command=lambda: agregar_caso())
menu_soporte.add_command(label="Ver Casos", command=lambda: ver_casos())

#menu donde se agregan la informacion de los clientes
menu_clientes = tk.Menu(menubar)
menubar.add_cascade(label="Clientes", menu=menu_clientes)
menu_clientes.add_command(label="Agregar Cliente", command=lambda: agregar_cliente())
menu_clientes.add_command(label="Ver Clientes", command=lambda: ver_clientes())

#menu donde se agregan la informacion de los servidores en inventario
menu_servidores = tk.Menu(menubar)
menubar.add_cascade(label="Servidores", menu=menu_servidores)
menu_servidores.add_command(label="Agregar Servidor", command=lambda: agregar_servidor())
menu_servidores.add_command(label="Ver Servidores", command=lambda: ver_servidores())

#menu en donde se agregan la informacion de los servidores en venta
menu_servidores_venta = tk.Menu(menubar)
menubar.add_cascade(label="Servidores en Venta", menu=menu_servidores_venta)
menu_servidores_venta.add_command(label="Agregar Servidor en Venta", command=lambda: agregar_servidor_venta())
menu_servidores_venta.add_command(label="Ver Servidores en Venta", command=lambda: ver_servidores_venta())

#padding y orientación
padding_label = {"padx": 10, "pady": 10, "sticky": "we"}  # padding y orientación de etiquetas y entradas
padding_frame = {"padx": 20, "pady": 20, "fill": "both", "expand": True}  # padding de los frames

#contenedor principal
contenedor_principal = tk.Frame(main)
contenedor_principal.pack(**padding_frame)

#funcion para limpiar la ventana principal
def limpiar_ventana():
    for widget in contenedor_principal.winfo_children():
        widget.destroy()

#ventana agregar cliente
def agregar_cliente():
    limpiar_ventana()   
    main.title("Agregar Cliente")
    agregar_cliente = tk.Frame(contenedor_principal)
    agregar_cliente.pack(**padding_frame)

    #formulario cliente
    label_nombre = tk.Label(agregar_cliente, text="Nombre:")
    entry_nombre = tk.Entry(agregar_cliente)
    label_nombre.grid(row=0, column=0, **padding_label)
    entry_nombre.grid(row=0, column=1, **padding_label)

    label_ruc_dni = tk.Label(agregar_cliente, text="RUC/DNI:")
    entry_ruc_dni = tk.Entry(agregar_cliente)
    label_ruc_dni.grid(row=1, column=0, **padding_label)
    entry_ruc_dni.grid(row=1, column=1, **padding_label)

    label_telefono = tk.Label(agregar_cliente, text="Teléfono:")
    entry_telefono = tk.Entry(agregar_cliente)
    label_telefono.grid(row=2, column=0, **padding_label)
    entry_telefono.grid(row=2, column=1, **padding_label)

    label_correo = tk.Label(agregar_cliente, text="Correo:")
    entry_correo = tk.Entry(agregar_cliente)
    label_correo.grid(row=3, column=0, **padding_label)
    entry_correo.grid(row=3, column=1, **padding_label)

    label_direccion = tk.Label(agregar_cliente, text="Dirección:")
    entry_direccion = tk.Entry(agregar_cliente)
    label_direccion.grid(row=4, column=0, **padding_label)
    entry_direccion.grid(row=4, column=1, **padding_label)

    agregar_cliente.grid_columnconfigure(1, weight=1)

  
#ventana agregar servidor
def agregar_servidor():
    limpiar_ventana()
    main.title("Agregar Servidor")
    agregar_servidor = tk.Frame(contenedor_principal)
    agregar_servidor.pack(**padding_frame)

    #formulario servidor
    label_nombre = tk.Label(agregar_servidor, text="Nombre:")
    entry_nombre = tk.Entry(agregar_servidor)
    label_nombre.grid(row=0, column=0, **padding_label)
    entry_nombre.grid(row=0, column=1, **padding_label)

    label_formato = tk.Label(agregar_servidor, text="Formato:")
    entry_formato = tk.Entry(agregar_servidor)
    label_formato.grid(row=1, column=0, **padding_label)
    entry_formato.grid(row=1, column=1, **padding_label)

    label_procesador = tk.Label(agregar_servidor, text="Procesador:")
    entry_procesador = tk.Entry(agregar_servidor)
    label_procesador.grid(row=2, column=0, **padding_label)
    entry_procesador.grid(row=2, column=1, **padding_label)

    label_memoria = tk.Label(agregar_servidor, text="Memoria:")
    entry_memoria = tk.Entry(agregar_servidor)
    label_memoria.grid(row=3, column=0, **padding_label)
    entry_memoria.grid(row=3, column=1, **padding_label)

    label_red = tk.Label(agregar_servidor, text="Red:")
    entry_red = tk.Entry(agregar_servidor)
    label_red.grid(row=4, column=0, **padding_label)
    entry_red.grid(row=4, column=1, **padding_label)

    label_almacenamiento = tk.Label(agregar_servidor, text="Almacenamiento:")
    entry_almacenamiento = tk.Entry(agregar_servidor)
    label_almacenamiento.grid(row=5, column=0, **padding_label)
    entry_almacenamiento.grid(row=5, column=1, **padding_label)

    label_disco = tk.Label(agregar_servidor, text="Disco duro:")
    entry_disco = tk.Entry(agregar_servidor)
    label_disco.grid(row=6, column=0, **padding_label)
    entry_disco.grid(row=6, column=1, **padding_label)

    label_controladora = tk.Label(agregar_servidor, text="Controladora:")
    entry_controladora = tk.Entry(agregar_servidor)
    label_controladora.grid(row=7, column=0, **padding_label)
    entry_controladora.grid(row=7, column=1, **padding_label)

    label_fuente = tk.Label(agregar_servidor, text="Fuente de poder:")
    entry_fuente = tk.Entry(agregar_servidor)
    label_fuente.grid(row=8, column=0, **padding_label)
    entry_fuente.grid(row=8, column=1, **padding_label)

    label_administracion = tk.Label(agregar_servidor, text="Administración:")
    entry_administracion = tk.Entry(agregar_servidor)
    label_administracion.grid(row=9, column=0, **padding_label)
    entry_administracion.grid(row=9, column=1, **padding_label)

    label_garantia = tk.Label(agregar_servidor, text="Garantía:")
    entry_garantia = tk.Entry(agregar_servidor)
    label_garantia.grid(row=10, column=0, **padding_label)
    entry_garantia.grid(row=10, column=1, **padding_label)

    agregar_servidor.grid_columnconfigure(1, weight=1)

    boton_copiar = tk.Button(agregar_servidor, text="Copiar Datos", command=copiar_datos)
    boton_copiar.grid(row=11, column=0, **padding_label, columnspan=2)

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
        salida.pack(**padding_frame)


main.mainloop()