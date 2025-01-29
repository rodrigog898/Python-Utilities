# 📜 Foliador

Este proyecto es una aplicación en Python que permite generar un documento PDF con folios numerados. Para ello, recopila información de la empresa o persona (📌 Razón Social, 📋 RUT, 📍 Dirección, etc.), define el rango de folios (🔢 Desde y Hasta) y selecciona el tamaño de página (📄 Carta u Oficio) y su orientación (🔄 Horizontal o Vertical). Finalmente, produce un PDF con toda la información en el encabezado de cada página.

## 📌 Requisitos

1. **🐍 Python 3.7 o superior**  
   Asegúrate de tener instalada una versión reciente de Python.

2. **🖥️ Tkinter**  
   Tkinter suele venir incluido con la instalación estándar de Python. Si no lo tienes, puedes instalarlo dependiendo de tu sistema operativo.

3. **🎨 CustomTkinter**  
   Es un paquete adicional para crear interfaces personalizadas con Tkinter. Instálalo con:
   ```bash
   pip install customtkinter
   ```

4. **📝 ReportLab**  
   Es la librería que se utiliza para generar archivos PDF. Instálala con:
   ```bash
   pip install reportlab
   ```

## 🚀 Uso

1️⃣ Clona o descarga este repositorio en tu computadora.

2️⃣ Instala las dependencias mencionadas en la sección anterior.

3️⃣ Ejecuta el script desde la terminal o línea de comandos:

   ```bash
   python foliador.py
   ```

   Asegúrate de que `foliador.py` sea el nombre exacto del archivo donde guardaste el código.

4️⃣ Se abrirá una interfaz gráfica con los siguientes campos para completar:

   - 🏢 **Razón Social**
   - 🆔 **RUT**
   - 📍 **Dirección**
   - 👤 **Rep. Legal**
   - 🆔 **RUT Rep. Legal**
   - 🔢 **Folio Desde** (solo números enteros)
   - 🔢 **Folio Hasta** (solo números enteros)

5️⃣ Además, podrás elegir:

   - 📄 **Tipo de Página:** Carta u Oficio
   - 🔄 **Orientación:** Horizontal o Vertical

6️⃣ Haz clic en el botón **Generar PDF**. Aparecerá un mensaje de confirmación y se creará un archivo llamado `folios_generados.pdf` en el mismo directorio donde se ejecuta el script.

## 🔥 Funcionalidades Principales

✅ **Validación de campos vacíos:** Si uno de los campos obligatorios está vacío, muestra un mensaje de error.
✅ **Rango de folios:** Valida que el folio inicial sea menor o igual al folio final.
✅ **Selección de papel y orientación:** Cambia el tamaño y orientación de la página según la opción elegida.
✅ **Encabezado personalizado:** En cada página del PDF se imprime la información de la empresa (o persona) y el folio correspondiente.
✅ **Fuente ajustada:** Usa una fuente pequeña (6 puntos) y un interlineado personalizado para aprovechar mejor el espacio.

## 🎨 Personalización

Si quieres modificar aspectos como:

🎨 **Tamaño de fuente**
📏 **Posición del texto**
🎨 **Color del tema** (por ejemplo, cambiar `ctk.set_default_color_theme("blue")` por otro)

Puedes editar las secciones correspondientes en el código fuente dentro del archivo.

## 👨‍💻 Créditos

🛠️ **Desarrollado por:** Rodrigo Aravena

Si usas o te basas en este código, considera mencionar al autor original. 🙌

📜 ¡Disfruta utilizando este foliador y ahorra tiempo en el proceso de numerar tus documentos! 🚀

