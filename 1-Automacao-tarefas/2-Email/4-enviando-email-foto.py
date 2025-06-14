from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = open('senha/senha.txt', 'r', encoding='utf-8').read().replace(" ", "")
from_email = 'paulobueninhosilva@gmail.com'
to_email = 'paulosilvabuenoo@gmail.com'
subject = 'Equipe XP' #Assunto
#Enviando e-mail de acordo com um arquivo!
#No body podemos utilizar o documento ou criarmos somente uma string nossa!
body = open('files/ativos.txt', 'r', encoding="utf-8").read()

#1 - Estruturando a mensagem via e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)
safe = ssl.create_default_context()

#2 - Adicionando Anexo
anexo = 'bb.preco.png'
print(mimetypes.guess_type(anexo))
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a: #Usando o open com rb(rebase) para reler o arquivo e nessa releitura adicionar os arquivos em message
    #Adicionando anexo com o comando add_attachment
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )

#3 - Enviando Email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )