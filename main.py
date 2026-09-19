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
pad = {"sticky": "e", "padx": 10, "pady": 10}  # padding y orientación de etiquetas y entradas


#ventana agregar cliente
def agregar_cliente():
    agregar_cliente = tk.Toplevel(main)
    agregar_cliente.title("Agregar Cliente")
    agregar_cliente.geometry("400x300")

    #formulario cliente
    label_nombre = tk.Label(agregar_cliente, text="Nombre:")
    entry_nombre = tk.Entry(agregar_cliente)

    label_ruc_dni = tk.Label(agregar_cliente, text="RUC/DNI:")
    entry_ruc_dni = tk.Entry(agregar_cliente)

    label_telefono = tk.Label(agregar_cliente, text="Teléfono:")
    entry_telefono = tk.Entry(agregar_cliente)

    label_correo = tk.Label(agregar_cliente, text="Correo:")
    entry_correo = tk.Entry(agregar_cliente)

    label_direccion = tk.Label(agregar_cliente, text="Dirección:")
    entry_direccion = tk.Entry(agregar_cliente)

    label_nombre.grid(row=0, column=0, **pad)
    entry_nombre.grid(row=0, column=1, **pad)

    label_ruc_dni.grid(row=1, column=0, **pad)
    entry_ruc_dni.grid(row=1, column=1, **pad)

    label_telefono.grid(row=2, column=0, **pad)
    entry_telefono.grid(row=2, column=1, **pad)

    label_correo.grid(row=3, column=0, **pad)
    entry_correo.grid(row=3, column=1, **pad)

    label_direccion.grid(row=4, column=0, **pad)
    entry_direccion.grid(row=4, column=1, **pad)



btn_agregar_cliente = tk.Button(main, text="Agregar Cliente", command=agregar_cliente)
btn_agregar_cliente.pack(pady=20)




main.mainloop()