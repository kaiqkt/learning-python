from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = ''
minha_senha = ''

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Luiz Otávio', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Kaique'
msg['to'] = meu_email  # Cliente
msg['subject'] = 'ASSUNTO DO E-MAIL'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
# with open('IMAGEM.JPG', 'rb') as img:
#     img = MIMEImage(img.read())
#     msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
