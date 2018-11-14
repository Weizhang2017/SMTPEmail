#Sending an Email through an SMTP server
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid, localtime
import smtplib
import poplib

class FieldMissing(Exception):
	def __init__(self, missing_field):
		self.err_msg = '{} is missing'.format(missing_field)
	def __str__(self):
		return self.err_msg


class Message(object):

	def create_mime(self, **kwargs):
		'''create a mine message'''

		if not kwargs.get('recipient_email_addr'):
			raise FieldMissing('recipient_email_addr')
		if not kwargs.get('sender_email_addr'):
			raise FieldMissing('sender_email_addr')

		subject = kwargs.get('subject') or ''
		sender_display_name = kwargs.get('sender_display_name') or ''
		sender_email_addr = kwargs['sender_email_addr']
		recipient_display_name = kwargs.get('recipient_display_name') or ''
		recipient_email_addr = kwargs['recipient_email_addr']
		content_html = kwargs.get('content_html') or ''
		content_text = kwargs.get('content_text') or ''
		custom_header = kwargs.get('custom_header') # a dictionary containing customized headers

		message_id = make_msgid(domain =sender_email_addr.split('@')[1])

		self.msg = EmailMessage()
		self.msg['Subject'] = subject
		self.msg['From'] = Address(display_name=sender_display_name, addr_spec=sender_email_addr)
		self.msg['To'] = Address(display_name=recipient_display_name, addr_spec=recipient_email_addr)
		self.msg['Date'] = localtime()
		self.msg.add_header('Message-Id', message_id[1:-1])
		if custom_header:
			for key, value in custom_header.items():
				self.msg.add_header(key, value)
		if content_text:
			self.msg.set_content(content_text)
			if content_html:
				self.msg.add_alternative(content_html, subtype='html')
		else:
			self.msg.set_content(content_html,subtype='html')
		
		return self.msg

	def __str__(self):
		return str(self.msg)

class User(object):
	def __init__(self, **kwargs):

		#parameters for SMTP server
		self.SMTP_server = kwargs.get('SMTP_server')
		self.SMTP_account = kwargs.get('SMTP_account')
		self.SMTP_password = kwargs.get('SMTP_password')
		self.SMTP_server = kwargs.get('SMTP_server')

		#parameters for POP3 server
		self.POP3_server = kwargs.get('POP3_server')
		self.POP3_password = kwargs.get('POP3_password')
		self.POP3_account = kwargs.get('POP3_account')
		
class SMTP(Message, User):

	def __init__(self, SMTP_port=25, **kwargs):
		'''default port = 25'''
		self.port = SMTP_port
		super().__init__(**kwargs)
		if not self.SMTP_server:
			raise FieldMissing('SMTP_server')
		if not self.SMTP_account:
			raise FieldMissing('SMTP_account')
		if not self.SMTP_password:
			raise FieldMissing('SMTP_password')


	def send_msg(self):
		'''connect to SMTP server and send the message'''
		with smtplib.SMTP(self.SMTP_server, self.port) as server:
			server.starttls()
			server.login(self.SMTP_account, self.SMTP_password) 
			server.set_debuglevel(False)
			server.send_message(self.msg)
		return 'Success'

class POP3(User):

	def __init__(self, POP3_port=995, **kwargs):
		self.port = POP3_port
		super().__init__(**kwargs)
		if not self.POP3_server:
			raise FieldMissing('POP3_server')
		if not self.POP3_account:
			raise FieldMissing('POP3_account')
		if not self.POP3_password:
			raise FieldMissing('POP3_password')

	def retrieve_msg(self):
		mailbox = poplib.POP3_SSL(self.POP3_server, self.port) 
		mailbox.user(self.POP3_account)
		mailbox.pass_(self.POP3_password)
		num_msg = len(mailbox.list()[1])
		for i in range(num_msg):
			for msg in mailbox.retr(i+1)[1]:
				yield msg
		mailbox.quit()

	def mailbox_size(self):
		mailbox = poplib.POP3_SSL(self.POP3_server, self.port)
		mailbox.user(self.POP3_account)
		mailbox.pass_(self.POP3_password)
		stat = mailbox.stat()
		size = {'message count': stat[0], 'mailbox size': stat[1]}
		mailbox.quit()
		return size


