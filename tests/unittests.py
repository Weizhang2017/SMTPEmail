from SMTPEmail import POP3
# import pytest

def test_user():
	pop3 = POP3(POP3_server='sagepool.site',
				POP3_account='info@sagepool.site',
				POP3_password='123welcome123')

	for msg in pop3.retrieve_entire_msg():
		print('+'*128)
		print(msg)

if __name__ == '__main__':
	test_user()
