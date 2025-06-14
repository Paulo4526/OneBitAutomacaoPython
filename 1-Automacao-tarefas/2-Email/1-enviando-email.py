#Neste teste utilizaremos o Gmail
#Após ter criado sua conta Gmail, clique no seu perfil e gerenciar conta de e-mail(Manager your google acount)
#Após isso selecione a aba de secutiry, e ative o login com 2 fatores
#Digite na aba de pesquisa Senhas de app e crie uma senha
#Importanto as bibiliotecas!

from email.message import EmailMessage
import smtplib
import ssl

password = open('senha/senha.txt', 'r', encoding='utf-8').read().replace(" ", "")
from_email = 'paulobueninhosilva@gmail.com'
to_email = 'paulosilvabuenoo@gmail.com'
subject = 'Curso Python' #Assunto
#Enviando e-mail de acordo com um arquivo!
#No body podemos utilizar o documento ou criarmos somente uma string nossa!
body = open('files/texto-email.txt', 'r', encoding="utf-8").read()

#1 - Estruturando a mensagem via e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)
safe = ssl.create_default_context()

#2 - Enviando Email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )

