import tkinter as tk

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

#menu donde se agregan los casos de soporte
menu_soporte = tk.Menu(menubar)
menubar.add_cascade(label="Soporte", menu=menu_soporte)
menu_soporte.add_command(label="Agregar Caso", command=lambda: agregar_caso())
menu_soporte.add_command(label="Ver Casos", command=lambda: ver_casos())

#menu donde se agregan la informacion de los clientes
menu_clientes = tk.Menu(menubar)
menubar.add_cascade(label="Clientes", menu=menu_clientes)
menu_clientes.add_command(label="Agregar Cliente", command=lambda:agregar_cliente())
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

#estilos de padding para los widgets
padding_label = {"padx": 10, "pady": 10, "sticky": "we"}  # padding y orientación de etiquetas y entradas
padding_frame = {"padx": 20, "pady": 20, "fill": "both", "expand": True}  # padding de los frames

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

    campos = ["Nombre", 
              "RUC/DNI", 
              "Teléfono", 
              "Correo", 
              "Dirección"]

    datos = {}

    for indice, campo in enumerate(campos):
        label = tk.Label(agregar_cliente, text=campo + ":")
        entry = tk.Entry(agregar_cliente)
        label.grid(row=indice, column=0, **padding_label)
        entry.grid(row=indice, column=1, **padding_label)
        datos[campo] = entry

    agregar_cliente.grid_columnconfigure(1, weight=1)

#ventana agregar servidor
def agregar_servidor_venta():
    limpiar_ventana()
    main.title("Agregar Servidor")
    agregar_servidor_venta= tk.Frame(contenedor_principal)
    agregar_servidor_venta.pack(**padding_frame)


    campos = ["Nombre", 
              "Formato", 
              "Procesador", 
              "Memoria", 
              "Red", 
              "Almacenamiento",
              "Controladora", 
              "Fuente de poder", 
              "Administración", 
              "Garantía"]

    datos = {}

    for indice, campo in enumerate(campos):
        label = tk.Label(agregar_servidor_venta, text=campo + ":")
        entry = tk.Entry(agregar_servidor_venta)
        label.grid(row=indice, column=0, **padding_label)
        entry.grid(row=indice, column=1, **padding_label)
        datos[campo] = entry

    agregar_servidor_venta.grid_columnconfigure(1, weight=1)
        
    btn_guardar = tk.Button(agregar_servidor_venta, text="Guardar", command=lambda: [print(f"{campo}: {entry.get()}") for campo, entry in datos.items()])
    btn_guardar.grid(row=len(campos), column=0, columnspan=2, **padding_label)


main.mainloop()