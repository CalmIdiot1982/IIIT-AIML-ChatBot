'''
send_mail : python module that uses flask to send email.
call method mail_results with parameters:
emailid : emailid for the recipient
html_msg: the html body of the email 
'''
from flask import Flask
from flask_mail import Mail,Message
import os
app = Flask(__name__)

mail_setting = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_PORT" : 465,
    "MAIL_USERNAME":"skpandaupgrad@gmail.com",
    "MAIL_PASSWORD":"Cobol1982$",
}
app.config.update(mail_setting)
mail = Mail(app)

def mail_results(emailid, html_msg):
    msg = Message(sender=app.config.get("MAIL_USERNAME"), recipients=[emailid])
    msg.subject = "Foodie Search Results"
    msg.html = html_msg
    mail.send(msg)