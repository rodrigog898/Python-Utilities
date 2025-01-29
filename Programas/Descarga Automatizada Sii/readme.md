# 🤖 Automatización de Descarga con Selenium y CustomTkinter

🚀 **Automatización de Descarga** es una aplicación en Python que permite **iniciar sesión**, **seleccionar empresas** y **descargar documentos en PDF** desde el portal del SII utilizando **Selenium** y una interfaz gráfica con **CustomTkinter**.

## 📌 Características

✔️ **Inicio de sesión automático** en el portal del SII.  
✔️ **Selección de empresa** y filtrado de documentos por fecha.  
✔️ **Automatización de descarga** de documentos en PDF.  
✔️ **Interfaz gráfica moderna** con CustomTkinter.  
✔️ **Uso de Selenium** para interacción web y descarga de datos.  

---

## 🔧 Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

1. **Python 3.7 o superior**  
2. **CustomTkinter** (para la interfaz gráfica)  
   ```bash
   pip install customtkinter
   ```
3. **Selenium** (para la automatización del navegador)  
   ```bash
   pip install selenium
   ```
4. **Pillow** (para manipulación de imágenes en Tkinter)  
   ```bash
   pip install pillow
   ```
5. **Requests** (para la descarga de archivos PDF)  
   ```bash
   pip install requests
   ```
6. **WebDriver Manager** (para gestionar ChromeDriver automáticamente)  
   ```bash
   pip install webdriver-manager
   ```

---

## 🚀 Instalación y Uso

Clona este repositorio o descárgalo:

```bash
git clone https://github.com/tuusuario/automatizacion-sii.git
cd automatizacion-sii
```

Ejecuta la aplicación:

```bash
python main.py
```

---

## 🎨 Interfaz y Funcionamiento

### 🔑 Iniciar Sesión
1. Ingresar **RUT** y **Contraseña** en la pantalla de login.
2. Pulsar **"Login"** para acceder al sistema.

### 🏢 Seleccionar Empresa y Fecha
1. Seleccionar una empresa de la lista desplegable.
2. Ingresar la fecha en formato **YYYY-MM-DD**.
3. Pulsar **"Ejecutar Automatización"**.

### 📥 Descarga de Documentos
1. La aplicación filtrará documentos por la fecha ingresada.
2. Descargará automáticamente los documentos en formato **PDF**.
3. Los archivos se guardarán en la carpeta de ejecución del script.

---

## ⚙️ Personalización

Si deseas modificar el comportamiento de la aplicación, puedes editar el código en `main.py`, ajustando:

- 📜 **URL del portal del SII** en `driver.get()`.
- 🎨 **Estilos de la interfaz** en `setStyleSheet()`.
- ⏳ **Tiempos de espera** en `time.sleep()`.
- 🖥️ **Configuraciones del WebDriver** en `chrome_options`.

---

## 🏆 Créditos

💻 **Desarrollado por**: Rodrigo Aravena  
📌 Si te gusta este proyecto, ¡no dudes en dar una ⭐ en GitHub!

---

¡Automatiza tus descargas del SII con esta poderosa herramienta! 🚀📄✨
