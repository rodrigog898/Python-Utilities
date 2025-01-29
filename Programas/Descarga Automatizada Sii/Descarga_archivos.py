import os
import time
import requests
import customtkinter
import tkinter
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x500")
app.title('Automatización de Descarga')
app.configure(bg="black")

# Variables globales
driver = None
companies_list = []

def init_webdriver():
    global driver
    current_dir = os.getcwd()  # Utilizamos la carpeta de ejecución

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    prefs = {
        "download.default_directory": current_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# --- Etapa 1: Pantalla de Login ---
login_frame = customtkinter.CTkFrame(master=app, width=400, height=300, corner_radius=15)
login_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label_login = customtkinter.CTkLabel(master=login_frame, text="Inicia Sesión", font=('Century Gothic', 20))
label_login.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

entry_username = customtkinter.CTkEntry(master=login_frame, width=220, placeholder_text='RUT')
entry_username.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

entry_password = customtkinter.CTkEntry(master=login_frame, width=220, placeholder_text='Contraseña', show="*")
entry_password.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label_login_foot = customtkinter.CTkLabel(master=login_frame, text="Desarrollado por Rodrigo Aravena", font=('Century Gothic', 10))
label_login_foot.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

def handle_login():
    """Acción del botón Login."""
    rut = entry_username.get()
    clave = entry_password.get()
    
    init_webdriver()
    
    # 3. Ir a la página de inicio de sesión
    driver.get("https://zeusr.sii.cl/AUT2000/InicioAutenticacion/IngresoRutClave.html?https://misiir.sii.cl/cgi_misii/siihome.cgi")

    # 4. Iniciar sesión
    username_field = driver.find_element(By.ID, "rutcntr")
    password_field = driver.find_element(By.ID, "clave")
    username_field.send_keys(rut)
    password_field.send_keys(clave)
    password_field.submit()

    time.sleep(5)  # Espera la redirección
    
    # 5. Seleccionar empresa
    driver.get("https://www1.sii.cl/cgi-bin/Portal001/mipeSelEmpresa.cgi?DESDE_DONDE_URL=OPCION%3D1%26TIPO%3D4")
    select_element = driver.find_element(By.NAME, "RUT_EMP")
    select = Select(select_element)

    global companies_list
    companies_list = [option.text.strip() for option in select.options]

    # Pasar a la siguiente etapa de la interfaz
    show_company_selector()

button_login = customtkinter.CTkButton(master=login_frame, text="Login", command=handle_login)
button_login.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# --- Etapa 2: Pantalla de Selección de Empresa y Descarga ---
def show_company_selector():
    """Muestra la segunda pantalla para seleccionar empresa y filtrar por fecha."""
    login_frame.destroy()

    second_frame = customtkinter.CTkFrame(master=app, width=400, height=400, corner_radius=15)
    second_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    label_title = customtkinter.CTkLabel(master=second_frame, text="Selecciona Empresa y Fecha", font=('Century Gothic', 20))
    label_title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    dropdown_empresa = customtkinter.CTkComboBox(master=second_frame, values=companies_list, width=220)
    dropdown_empresa.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    entry_fecha = customtkinter.CTkEntry(master=second_frame, width=220, placeholder_text='Fecha (YYYY-MM-DD)')
    entry_fecha.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
    label_footer = customtkinter.CTkLabel(master=second_frame, text="Desarrollado por Rodrigo Aravena", font=('Century Gothic', 10))
    label_footer.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    # --- Label para indicar el estado de la descarga ---
    status_label = customtkinter.CTkLabel(master=second_frame, text="", font=('Century Gothic', 12))
    status_label.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def run_automation():
        """Ejecuta la lógica de Selenium para filtrar y descargar documentos en PDF."""
        try:
            # Muestra mensaje de inicio de descarga
            status_label.configure(text="Descargando datos, por favor espere...")
            app.update_idletasks()  # Actualiza la interfaz antes de comenzar

            selected_empresa = dropdown_empresa.get()
            fecha_deseada = entry_fecha.get()

            # Seleccionar la empresa en Selenium usando el texto visible
            select_element = driver.find_element(By.NAME, "RUT_EMP")
            select = Select(select_element)
            select.select_by_visible_text(selected_empresa)
            
            submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
            submit_button.click()

            time.sleep(5)
            print("Título de la página después de enviar:", driver.title)

            # 6. Filtrar documentos por fecha
            tabla = driver.find_element(By.ID, "tablaDatos")
            filas = tabla.find_elements(By.TAG_NAME, "tr")

            documentos = []
            for fila in filas[1:]:
                columnas = fila.find_elements(By.TAG_NAME, "td")
                if len(columnas) > 0:
                    fecha_emision = columnas[5].text.strip()
                    if fecha_emision == fecha_deseada:
                        enlace = columnas[0].find_element(By.TAG_NAME, "a").get_attribute("href")
                        razon_social = columnas[2].text.strip()
                        folio = columnas[4].text.strip()
                        documentos.append((enlace, razon_social, folio))

            # 7. Descargar cada documento PDF
            for enlace, razon_social, folio in documentos:
                print(f"Abriendo documento: {enlace}")
                driver.get(enlace)
                time.sleep(3)

                boton_pdf = driver.find_element(By.XPATH, '//a[contains(text(), "VISUALIZACIÓN DOCUMENTO (pdf)")]')
                pdf_url = boton_pdf.get_attribute("href")
                print(f"Descargando documento PDF desde: {pdf_url}")

                # Crear sesión con las cookies del navegador
                session = requests.Session()
                for cookie in driver.get_cookies():
                    session.cookies.set(cookie['name'], cookie['value'])

                response = session.get(pdf_url)
                if response.status_code == 200:
                    # Guardamos el PDF en el directorio de trabajo
                    current_dir = os.getcwd()
                    nombre_archivo = f"{razon_social}_{folio}.pdf"
                    # Evitamos caracteres ilegales en el nombre de archivo
                    for char in r'\/:*?"<>|':
                        nombre_archivo = nombre_archivo.replace(char, "-")
                    ruta_archivo = os.path.join(current_dir, nombre_archivo)
                    with open(ruta_archivo, "wb") as f:
                        f.write(response.content)
                    print(f"Documento guardado como: {ruta_archivo}")
                else:
                    print(f"Error al descargar el PDF desde: {pdf_url}")

                time.sleep(2)

            # Descarga finalizada
            status_label.configure(text="Descarga de documentos finalizada.")
            app.update_idletasks()
        finally:
            driver.quit()

    button_run = customtkinter.CTkButton(master=second_frame, text="Ejecutar Automatización", command=run_automation)
    button_run.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

app.mainloop()
