import smtplib
from email.mime.text import MIMEText

# setamos algumas constantes
SERVER = "localhost"
PORT = 8025
FROM = "eu@server.com"
TO = ["destino@outroserver.com", "outro@server.com"]
SUBJECT = "Assunto do e-mail"
TEXT = "Este é meu e-mail enviado via Python no terminal :)"

message = MIMEText(TEXT, "html")
message["Subject"] = SUBJECT
message["From"] = FROM
message["To"] = ", ".join(TO)

# with smtplib.SMTP(host=SERVER, port=PORT) as server:
#     server.sendmail(FROM, TO, message.as_string())

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("83f1618af77272", "ff77c56ae6ef22")
    server.sendmail(FROM, TO, message.as_string())