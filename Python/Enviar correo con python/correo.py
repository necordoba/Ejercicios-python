import yagmail
email = 'ensayo.345@gmail.com'
contraseña = 'ggmfbxyjtbboykkb'

yag = yagmail.SMTP(user=email, password=contraseña)

destinatarios = ['juanpazacno@gmail.com']
asunto = 'prueba de correo'
mensaje = "mensaje de prueba"

yag.send(destinatarios,asunto, mensaje)
