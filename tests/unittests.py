from SMTPEmail import User
import pytest

def test_user():
	user = User(SMTP_server='test_user')