# <------CoDed By AnonCODER------>
# <------v3.2----->
# <------Now PyLe needs your support with its release------>
# <------PyLe in Github : https://github.com/AnonC0DER/PyLe------>
##################################################################
import smtplib

# Send Email with PyLe Email Address
class withPyLe_email():

	def __init__(self, Message):
		self.Message = Message
	
	def send_PyLeEmail(self):
		USER = 'pylesend.emails@gmail.com'
		# Please Don't Change the Password, it's for sending emails
		PASS = 'it3N0tAPassword'

		FROM = USER
		# My Email Address :
		To = ['anoncoder@tutanota.com']
		# Message : 
		message_text = f'{self.Message}'
		
		server = smtplib.SMTP('smtp.gmail.com')
		server.connect('smtp.gmail.com',587)
		server.starttls()
		server.login(USER,PASS)
		server.sendmail(FROM, To, message_text)
		server.quit()
	
# Send Email with Your own Email Address
class yourOwn_email():

	def __init__(self, User, Password, Message):
		self.User = User
		self.Password = Password
		self.Message = Message
	
	def send_email(self):
		# Get email
		USER = f'{self.User}'
		# Get password
		PASS = f'{self.Password}'

		FROM = USER
		# My Email Address :
		To = ['anoncoder@tutanota.com']
		# Message : 
		message_text = f'{self.Message}'

		server = smtplib.SMTP('smtp.gmail.com')
		server.connect('smtp.gmail.com',587)
		server.starttls()
		server.login(USER,PASS)
		server.sendmail(FROM, To, message_text)
		server.quit()
##################################
# <------CoDed By AnonCODER------>
# <------v3.2----->
# <------Now PyLe needs your support with its release------>
# <------PyLe in Github : https://github.com/AnonC0DER/PyLe------>