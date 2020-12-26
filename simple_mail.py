import smtplib

sender_email = "skpandaupgrad@gmail.com"
reciever_email = "soumyapanda1982@gmail.com"
password = "Cobol1982$"
message = "This message was sent from simple_email"


def mail_results(emailid,html_msg="blank message"):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	try:
		server.login(sender_email, password)
		print("got to send email: ", emailid)
		server.sendmail(sender_email,emailid,html_msg)
	except Exception as e:
		print("Exception was hit :", e)

