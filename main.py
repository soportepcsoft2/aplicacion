import tkinter as tk

#estilos de padding para los widgets
padding_label = {"padx": 10, "pady": 10, "sticky": "we"}  # padding y orientación de etiquetas y entradas
padding_frame = {"padx": 20, "pady": 20, "fill": "both", "expand": True}  # padding de los frames

#ventana principal
main = tk.Tk()
main.title("PCSOFT Tecnología")
main.geometry("900x600")

#contenedor principal
contenedor_principal = tk.Frame(main)
contenedor_principal.pack(**padding_frame)

#barra de menu
main.option_add('*tearOff', tk.FALSE)
menubar = tk.Menu(main)
main.config(menu=menubar)

#agregar aqui las opciones de la barra de menu con sus respectivas funciones
menu_opciones = { 
    "Soporte": {
        "Agregar Caso": lambda: agregar_caso(),
        "Ver Casos": lambda: ver_casos()
    },
    "Clientes": {
        "Agregar Cliente": lambda: agregar_cliente(),
        "Ver Clientes": lambda: ver_clientes()
    },
    "Servidores": {
        "Agregar Servidor": lambda: agregar_servidor(),
        "Ver Servidores": lambda: ver_servidores()
    },
    "Servidores en Venta": {
        "Agregar Servidor en Venta": lambda: agregar_servidor_venta(),
        "Ver Servidores en Venta": lambda: ver_servidores_venta()
    }
}

for menu_nombre, opciones in menu_opciones.items():
    menu = tk.Menu(menubar)
    menubar.add_cascade(label=menu_nombre, menu=menu)
    for opcion_nombre, comando in opciones.items():
        menu.add_command(label=opcion_nombre, command=comando)

#funcion para limpiar la ventana principal
def limpiar_ventana():
    for widget in contenedor_principal.winfo_children():
        widget.destroy()

#funcion para agregar campos dinamicamente a un frame
def agregar_campos(frame, campos, datos):
    for indice, campo in enumerate(campos):
        label = tk.Label(frame, text=campo + ":")
        entry = tk.Entry(frame)
        label.grid(row=indice, column=0, **padding_label)
        entry.grid(row=indice, column=1, **padding_label)
        datos[campo] = entry
    frame.grid_columnconfigure(1, weight=1)

############################################### ventanas de cada opcion del menu ####################################################

#ventana agregar cliente
def agregar_cliente(): 
    limpiar_ventana()   
    main.title("Agregar Cliente")
    agregar_cliente = tk.Frame(contenedor_principal)
    agregar_cliente.pack(**padding_frame)

    campos = ["Nombre",  #agregar aqui los campos que se necesiten para agregar un cliente
              "RUC/DNI", 
              "Teléfono", 
              "Correo", 
              "Dirección"]

    datos = {} #diccionario para almacenar los datos ingresados por el usuario

    agregar_campos(agregar_cliente, campos, datos)
       
#ventana agregar servidor
def agregar_servidor_venta():
    limpiar_ventana()
    main.title("Agregar Servidor")
    agregar_servidor_venta= tk.Frame(contenedor_principal)
    agregar_servidor_venta.pack(**padding_frame)


    campos = ["Nombre",  #agregar aqui los campos que se necesiten para agregar un servidor
              "Formato", 
              "Formato", 
              "Procesador", 
              "Memoria", 
              "Red", 
              "Almacenamiento",
              "Controladora", 
              "Fuente de poder", 
              "Administración", 
              "Garantía"]

    datos = {} #diccionario para almacenar los datos ingresados por el usuario

    agregar_campos(agregar_servidor_venta, campos, datos)
        
    btn_guardar = tk.Button(agregar_servidor_venta, text="Guardar", command=lambda: [print(f"{campo}: {entry.get()}") for campo, entry in datos.items()])
    btn_guardar.grid(row=len(campos), column=0, columnspan=2, **padding_label)

#ventana agregar caso de soporte
def agregar_caso():
    limpiar_ventana()
    main.title("Agregar Caso de Soporte")
    agregar_caso = tk.Frame(contenedor_principal)
    agregar_caso.pack(**padding_frame)

    campos = ["Cliente",  #agregar aqui los campos que se necesiten para agregar un caso de soporte
              "Descripción del Problema", 
              "Fecha de Reporte", 
              "Estado",
              "Fecha de cierre"
              ]

    datos = {} #diccionario para almacenar los datos ingresados por el usuario

    agregar_campos(agregar_caso, campos, datos)
        
    btn_guardar = tk.Button(agregar_caso, text="Guardar", command=lambda: [print(f"{campo}: {entry.get()}") for campo, entry in datos.items()])
    btn_guardar.grid(row=len(campos), column=0, columnspan=2, **padding_label)


main.mainloop()