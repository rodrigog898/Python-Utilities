import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(correo_persona):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    sender_email = 'correo@gmail.com'
    password = 'password'
    recipient_email = correo_persona

    subject = 'Confirmacion dsdsdse Participacion'
    
    html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apiux Awards 2025</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; color: #333;">
    <div style="max-width: 600px; margin: 20px auto; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
        <div style="text-align: center;">
            <img src="https://github.com/user-attachments/assets/81db5782-8d6a-42fd-9bdd-85121ee44308" alt="Título Apiux Awards 2025" style="width: 100%; display: block;">
        </div>
        <div style="padding: 20px; text-align: center;">
            <h2 style="color: #222;">¡Hola, Rodrigo!</h2>
            <p>¡Tu participación en los <strong>Apiux Awards 2025</strong> ha sido confirmada con éxito!</p>
            <p><strong>🌟 Una Noche Especial 🌟</strong></p>
            <p>Te esperamos para disfrutar juntos de una experiencia única que celebra el trabajo, la innovación y el compromiso.</p>
            <div style="display: flex; justify-content: center; margin: 20px 0; flex-wrap: wrap;">
                <div style="text-align: center; margin: 10px; width: 30%;">
                    <img src="https://github.com/user-attachments/assets/6ab6edff-21d2-4a8e-8d56-f5c8c071503c" alt="Fecha" style="width: 50px; margin-bottom: 5px;">
                    <p><strong>Fecha:</strong><br>09 de Enero</p>
                </div>
                <div style="text-align: center; margin: 10px; width: 30%;">
                    <img src="https://github.com/user-attachments/assets/ed05c885-492d-47b1-b3dc-8feabb852294" alt="Hora" style="width: 50px; margin-bottom: 5px;">
                    <p><strong>Hora:</strong><br>19:00 hrs</p>
                </div>
                <div style="text-align: center; margin: 10px; width: 30%;">
                    <img src="https://github.com/user-attachments/assets/f384f521-e1c8-4889-90cb-2e6dd3a7bb07" alt="Lugar" style="width: 50px; margin-bottom: 5px;">
                    <p><strong>Lugar:</strong><br>Piso 18, DoubleTree by Hilton, Av Vitacura 2727, Las Condes</p>
                </div>
            </div>
            <h3 style="margin-top: 20px;">Experiencia del evento</h3>
            <div style="display: flex; justify-content: center; margin: 20px 0; flex-wrap: wrap;">
                <div style="text-align: center; margin: 10px; width: 25%;">
                    <img src="https://github.com/user-attachments/assets/a4aedabb-bf5a-41b9-b5f9-858315282eb3" alt="Recap" style="width: 50px; margin-bottom: 5px;">
                    <p>Recap 2024</p>
                </div>
                <div style="text-align: center; margin: 10px; width: 25%;">
                    <img src="https://github.com/user-attachments/assets/f92e1b49-f1d0-43e4-b206-85f34a001244" alt="Desafíos" style="width: 50px; margin-bottom: 5px;">
                    <p>Desafíos 2025</p>
                </div>
                <div style="text-align: center; margin: 10px; width: 25%;">
                    <img src="https://github.com/user-attachments/assets/b922b164-3036-44cc-a2cd-7f629e0c81b8" alt="Premiación" style="width: 50px; margin-bottom: 5px;">
                    <p>Premiación</p>
                </div>
                <div style="text-align: center; margin: 10px; width: 25%;">
                    <img src="https://github.com/user-attachments/assets/64423860-5904-4f68-bfcb-315c43757bbb" alt="Sorpresas" style="width: 50px; margin-bottom: 5px;">
                    <p>Sorpresas</p>
                </div>
            </div>
        </div>
        <div style="background: #f1f1f1; text-align: center; padding: 30px 20px; font-size: 14px; color: #666;">
            <img src="https://github.com/user-attachments/assets/eb22db29-a2bc-46af-9039-b09b7579215c" alt="Apiux Logo" style="width: 150px; margin-bottom: 15px;">
            <p>Si tienes dudas, comentarios o sugerencias, <a href="#" style="color: #5a00e0; text-decoration: none;">Contáctanos</a>.</p>
            <div style="margin: 10px 0;">
                <a href="#" style="font-size: 24px; margin: 0 5px; color: #333; text-decoration: none;"><i class="fab fa-instagram"></i></a>
                <a href="#" style="font-size: 24px; margin: 0 5px; color: #333; text-decoration: none;"><i class="fab fa-linkedin"></i></a>
                <a href="#" style="font-size: 24px; margin: 0 5px; color: #333; text-decoration: none;"><i class="fas fa-globe"></i></a>
            </div>
            <p style="margin-top: 10px;">Copyright 2024 Apiux Tech, All rights reserved.<br>Chile - Colombia - España - Perú - Estados Unidos</p>
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

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            server.send_message(message)
        print("Correo enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {str(e)}")

# Ejemplo de uso
send_email('rodrigo.aravena@api-ux.com')
