import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from reportlab.lib.pagesizes import letter, legal
from reportlab.lib.pagesizes import landscape, portrait
from reportlab.pdfgen import canvas

# Función para generar el PDF con los datos ingresados
def generar_pdf():
    razon_social = entry_razon_social.get()
    rut = entry_rut.get()
    direccion = entry_direccion.get()
    rep_legal = entry_rep_legal.get()
    rut_rep_legal = entry_rut_rep_legal.get()
    folio_desde = entry_folio_desde.get()
    folio_hasta = entry_folio_hasta.get()

    if not all([razon_social, rut, direccion, rep_legal, rut_rep_legal, folio_desde, folio_hasta]):
        messagebox.showerror("Error", "Por favor, rellena todos los campos.")
        return
    
    try:
        folio_desde = int(folio_desde)
        folio_hasta = int(folio_hasta)
    except ValueError:
        messagebox.showerror("Error", "Los folios deben ser números enteros.")
        return

    if folio_desde > folio_hasta:
        messagebox.showerror("Error", "El folio desde debe ser menor o igual al folio hasta.")
        return

    # Determinar el tamaño de la página y la orientación según la selección del usuario
    tipo_papel = "Carta" if var_tipo_pagina.get() == 1 else "Oficio"
    orientacion = "Horizontal" if var_orientacion.get() == 1 else "Vertical"

    if tipo_papel == "Carta":
        size = letter
    else:
        size = legal

    # Ajustar la orientación
    if orientacion == "Horizontal":
        size = landscape(size)
    else:
        size = portrait(size)

    # Crear el archivo PDF
    nombre_archivo = "folios_generados.pdf"
    c = canvas.Canvas(nombre_archivo, pagesize=size)

    # Ajustar posición y tamaño de fuente para el encabezado
    encabezado_y_position = size[1] - 30  # Cercano al borde superior
    c.setFont("Helvetica", 6)  # Tamaño de fuente a 6 puntos
    interlineado = 8 # Interlineado consistente para todas las páginas

    # Generar folios dentro del rango dado
    for folio in range(folio_desde, folio_hasta + 1):
        # Reestablecer la posición y tamaño de fuente para cada página
        c.setFont("Helvetica", 6)  # Tamaño de fuente a 6 puntos en cada página
        encabezado_y_position = size[1] - 30  # Reajustar la posición del encabezado en cada página
        
        # Aplicar el mismo formato para todas las páginas
        c.drawString(40, encabezado_y_position, f"Razón Social: {razon_social}")
        c.drawString(40, encabezado_y_position - interlineado, f"RUT: {rut}")
        c.drawString(40, encabezado_y_position - 2 * interlineado, f"Dirección: {direccion}")
        c.drawString(40, encabezado_y_position - 3 * interlineado, f"Rep. Legal: {rep_legal} - RUT: {rut_rep_legal}")
        
        # Posicionar el folio en la misma línea que Razón Social, en el borde derecho
        c.drawString(size[0] - 100, encabezado_y_position, f"FOLIO Nº{folio}")
        
        # Finalizar página actual y generar una nueva
        c.showPage()

    # Guardar el PDF
    c.save()
    messagebox.showinfo("Éxito", f"PDF generado: {nombre_archivo}")

# Crear la ventana principal con CustomTkinter
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema azul predeterminado

root = ctk.CTk()
root.title("Dev by : Rodrigo Aravena")

# Variables para los radio buttons
var_tipo_pagina = tk.IntVar(value=1)  # 1 = Carta, 2 = Oficio
var_orientacion = tk.IntVar(value=1)  # 1 = Horizontal, 2 = Vertical

# Crear un frame para agrupar los campos y los radio buttons
# Crear un frame para agrupar los campos y los radio buttons
frame = ctk.CTkFrame(root)
frame.grid(row=1, column=0, padx=20, pady=20)

# Título de la aplicación
titulo_label = ctk.CTkLabel(root, text="Foliador", font=("Arial", 20))
titulo_label.grid(row=0, column=0, padx=10, pady=10)

# Campos de entrada para los datos
ctk.CTkLabel(frame, text="Razón Social:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_razon_social = ctk.CTkEntry(frame)
entry_razon_social.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(frame, text="RUT:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_rut = ctk.CTkEntry(frame)
entry_rut.grid(row=1, column=1, padx=10, pady=10, sticky="ew")


ctk.CTkLabel(frame, text="Dirección:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_direccion = ctk.CTkEntry(frame)
entry_direccion.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(frame, text="Rep. Legal:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_rep_legal = ctk.CTkEntry(frame)
entry_rep_legal.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(frame, text="RUT Rep. Legal:").grid(row=5, column=0, padx=10, pady=10, sticky="w")
entry_rut_rep_legal = ctk.CTkEntry(frame)
entry_rut_rep_legal.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(frame, text="Folio Desde:").grid(row=6, column=0, padx=10, pady=10, sticky="w")
entry_folio_desde = ctk.CTkEntry(frame)
entry_folio_desde.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

ctk.CTkLabel(frame, text="Folio Hasta:").grid(row=7, column=0, padx=10, pady=10, sticky="w")
entry_folio_hasta = ctk.CTkEntry(frame)
entry_folio_hasta.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

# Tipo de página (Carta u Oficio)
ctk.CTkLabel(frame, text="Tipo de Página:").grid(row=8, column=0, padx=10, pady=10, sticky="w")
ctk.CTkRadioButton(frame, text="Carta", variable=var_tipo_pagina, value=1).grid(row=8, column=1, padx=10, pady=10, sticky="w")
ctk.CTkRadioButton(frame, text="Oficio", variable=var_tipo_pagina, value=2).grid(row=8, column=2, padx=10, pady=10, sticky="w")

# Orientación (Horizontal o Vertical)
ctk.CTkLabel(frame, text="Orientación:").grid(row=9, column=0, padx=10, pady=10, sticky="w")
ctk.CTkRadioButton(frame, text="Horizontal", variable=var_orientacion, value=1).grid(row=9, column=1, padx=10, pady=10, sticky="w")
ctk.CTkRadioButton(frame, text="Vertical", variable=var_orientacion, value=2).grid(row=9, column=2, padx=10, pady=10, sticky="w")

# Botón para generar el PDF
btn_generar = ctk.CTkButton(frame, text="Generar PDF", command=generar_pdf)
btn_generar.grid(row=10, column=0, columnspan=3, padx=10, pady=20)

# Añadir una etiqueta que diga que fue desarrollado por ti
ctk.CTkLabel(root, text="Desarrollado por: Rodrigo Aravena", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=10)
# Ejecutar la ventana
root.mainloop()
