# Python Utilities

Este repositorio contiene una colección de utilidades en Python desarrolladas para diversas tareas, incluyendo manipulación de archivos, automatización, gestión de bases de datos y envío de correos electrónicos.

## 📂 Estructura del Proyecto

```
rodrigog898-python-utilities/
├── README.md
├── Campos_duplicados_mongo.py
├── Envio_correo_plantilla.py
├── Plantilla_correo_qr.py
├── SubirArchivoBucketgpc.py
└── Programas/
    ├── Descarga Automatizada Sii/
    │   ├── readme.md
    │   └── Descarga_archivos.py
    ├── Foliador/
    │   ├── readme.md
    │   └── Foliador.py
    └── PDF Splitter & Merge/
        ├── readme.md
        └── Merge_pdf_by_rodrigo.py
```

## 🛠 Descripción de los Scripts Principales

### 🔎 Campos_duplicados_mongo.py
Script que se conecta a una base de datos MongoDB y busca registros duplicados en la colección especificada, agrupando por `correo_persona`.

### 📧 Envio_correo_plantilla.py
Script para enviar correos electrónicos con plantillas HTML predefinidas utilizando SMTP.

### 📩 Plantilla_correo_qr.py
Genera un código QR con información dinámica y lo inserta en un correo electrónico, enviándolo al destinatario especificado.

### ☁️ SubirArchivoBucketgpc.py
Carga archivos a un bucket de Google Cloud Storage y almacena registros de la operación en una base de datos MongoDB.

## 📁 Programas

### 📥 Descarga Automatizada Sii
Automatiza la descarga de documentos desde el portal del Servicio de Impuestos Internos de Chile (SII) usando Selenium y CustomTkinter.

### 🏷️ Foliador
Genera documentos PDF con folios numerados a partir de datos ingresados por el usuario. Utiliza ReportLab y CustomTkinter.

### 📑 PDF Splitter & Merge
Herramienta gráfica basada en PyQt5 para unir y dividir archivos PDF de manera sencilla.

## 🚀 Instalación y Uso
Para ejecutar estos scripts, asegúrate de tener Python 3 instalado y las dependencias necesarias. Puedes instalar los requerimientos con:

```bash
pip install -r requirements.txt
```

Para cada módulo, revisa su respectivo `readme.md` para instrucciones más detalladas.

---
📌 **Desarrollado por:** Rodrigo Aravena

Si este proyecto te resulta útil, ¡no dudes en dejar una estrella en GitHub! ⭐

