import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import qrcode
import io

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    return img

def send_email(correo_persona, id_cliente, id_proyecto, id_sprint):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    sender_email = 'correo@gmail.com'
    password = 'password'
    recipient_email = correo_persona

    subject = 'Encuesta de Satisfacción - Apiux Tecnología'
    
    # Generar la URL del código QR con los parámetros dinámicos
    qr_url = f"https://url/{id_cliente}/{id_proyecto}/{id_sprint}"

    # Generar el código QR
    qr_img = generate_qr_code(qr_url)
    img_byte_arr = io.BytesIO()
    qr_img.save(img_byte_arr)
    img_byte_arr = img_byte_arr.getvalue()

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Template</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                color: #333333;
            }}
            .email-container {{
                max-width: 600px;
                margin: auto;
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
            }}
            .header {{
                background-color: #f6f6f6;
                padding: 20px;
                text-align: center;
                border-bottom: 3px solid #f0ad4e;
            }}
            .content {{
                padding: 20px;
            }}
            .footer {{
                background-color: #f6f6f6;
                padding: 10px 20px;
                font-size: 12px;
                text-align: center;
                border-top: 1px solid #e0e0e0;
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <!-- Place your image here as an <img> tag -->
                <img src="https://github.com/rodrigog898/Imagenes-Web-Pruebas/assets/82234888/70644cf1-1b74-4299-8b74-5259e2b6de7f" alt="Inspiring Conversations" style="max-width: 100%; height: auto;">
            </div>
            <div class="content">
                <h1>¡Hola Yellowers!</h1>
                <p>Estamos realizando una encuesta para conocer tu opinión sobre nuestros servicios y mejorar continuamente. Por favor, sigue las instrucciones cuidadosamente para completarla correctamente.</p>
                <h2>Instrucciones de la encuesta</h2>
                <ol>
                    <li>Por favor, responde a todas las preguntas de manera honesta y detallada.</li>
                    <li>La encuesta es anónima y tus respuestas serán tratadas con la máxima confidencialidad.</li>
                    <li>El puntaje de satisfacción debe estar en una escala del 1 al 5, donde 1 representa muy insatisfecho y 5 representa muy satisfecho.</li>
                </ol>
                <p>Si tienes alguna pregunta antes de comenzar, no dudes en contactarnos. ¡Te agradecemos mucho tu colaboración!</p>
                <h3>Es muy importante que completes esta encuesta lo antes posible.</h3>
                <!-- QR Code -->
                <div style="text-align: center; margin: 20px;">
                    <img src="cid:qr_code" alt="Código QR para la encuesta" style="max-width: 200px; height: auto;">
                </div>
            </div>
            <div class="footer">
                Staffing<br>
                Empresa de  Tecnología
            </div>
        </div>
    </body>
    </html>
    """

    body = html_content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'html'))
    image = MIMEImage(img_byte_arr, name='qr_code.png')
    image.add_header('Content-ID', '<qr_code>')
    message.attach(image)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            server.send_message(message)
        print("Correo enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {str(e)}")

# Ejemplo de uso con parámetros
send_email('correo_persona@gmail.com', '1', '2', '1')
