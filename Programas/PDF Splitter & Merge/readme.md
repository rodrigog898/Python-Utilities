# 📝 PDF Merger & Splitter

🚀 **PDF Merger & Splitter** es una aplicación de escritorio en Python con PyQt5 que permite **unir** y **dividir** archivos PDF de manera sencilla.

## 📌 Características

✔️ **Unir múltiples archivos PDF** en uno solo.  
✔️ **Dividir un PDF** desde una página específica.  
✔️ **Interfaz gráfica moderna** con PyQt5.  
✔️ **Validaciones** para evitar errores en la selección de archivos y páginas.  

---

## 🔧 Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

1. **Python 3.7 o superior**  
2. **PyQt5** (para la interfaz gráfica)  
   ```bash
   pip install PyQt5
   ```
3. **PyPDF2** (para manipulación de PDFs)  
   ```bash
   pip install PyPDF2
   ```

---

## 🚀 Instalación y Uso

Clona este repositorio o descárgalo:

```bash
git clone https://github.com/tuusuario/pdf-merger-splitter.git
cd pdf-merger-splitter
```

Ejecuta la aplicación:

```bash
python main.py
```

---

## 🎨 Interfaz y Funcionamiento

### 📂 Unir PDFs
1. Haz clic en **"Seleccionar PDF para unir"** y elige los archivos.
2. Pulsa **"Unir PDFs"** y guarda el nuevo archivo.

### ✂️ Dividir un PDF
1. Haz clic en **"Seleccionar PDF para dividir"** y elige el archivo.
2. Ingresa la página desde donde dividir en el campo de texto.
3. Pulsa **"Dividir PDF"** y guarda el archivo resultante.

---

## ⚙️ Personalización

Si deseas modificar la apariencia o el comportamiento de la aplicación, puedes editar el código en `main.py`, ajustando:

- 🎨 **Colores y estilos** en `setStyleSheet()`.
- 🔠 **Fuente y tamaño de los textos** con `QFont()`.
- 📑 **Mensajes de validación** para mejorar la experiencia del usuario.

---

## 🏆 Créditos

💻 **Desarrollado por**: Rodrigo Aravena  
📌 Si te gusta este proyecto, ¡no dudes en dar una ⭐ en GitHub!

---

¡Disfruta usando **PDF Merger & Splitter** y simplifica tu trabajo con documentos! 🚀📄✨
