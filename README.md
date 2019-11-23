[![Build Status](https://travis-ci.org/Weizhang2017/SMTPEmail.svg?branch=master)](https://travis-ci.org/Weizhang2017/SMTPEmail)

#### A simple script to send MIME message via SMTP server and retrieve messages via POP3

#### Installation 
```shell
pip install SMTPEmail
```
#### Install using Git
```shell
git clone https://github.com/Weizhang2017/SMTPEmail.git
cd SMTPEmail
python install setup.py
```

#### Usage

##### Sending email via SMTP

```python
from SMTPEmail import SMTP
client = SMTP(
	SMTP_server=<domain> or <IP_address>,
	SMTP_account=<account_name>,
	SMTP_password=<SMTP_password>
	)
client.create_mime(
	recipient_email_addr='Jane.Doe@jane.com',
	sender_email_addr='John.Doe@john.com',
	subject='subject',
	sender_display_name='John Doe',
	recipient_display_name='Jane Doe',
	content_html='<p>hello world</p>',
	content_text='hello world'
)
   
client.send_msg()
```  
##### Add customized email header
```python
custom_header = {'Sender': 'john@abc.com'}
client.create_mime(
	recipient_email_addr='Jane.Doe@jane.com',
	sender_email_addr='John.Doe@john.com',
	subject='subject',
	sender_display_name='John Doe',
	recipient_display_name='Jane Doe',
	content_html='<p>hello world</p>',
	content_text='hello world',
	custom_header=custom_header
)
```

#### Retrieve email via POP3  

messages will be returned in byte object

```python
from SMTPEmail import POP3
client = POP3(
	POP3_server = <domain> or <IP_address>,
	POP3_account = <account_name>,
	POP3_password = <POP3_password>
)
msgs = client.retrieve_msg()

for msg in msgs:
	print(msg)

>>>print(client.mailbox_size())
{'message count': 804, 'mailbox size': 18096539}
```
#### Retrieve email via IMAP  


```python
from SMTPEmail import IMAP
client = IMAP(
	IMAP_server = <domain> or <IP_address>,
	IMAP_account = <account_name>,
	IMAP_password = <IMAP_password>
)
#you can select which mailbox to access and which email to retrieve by passing parameters 'mailbox_name' and 'msg_id'
for msg in client.retrieve_msg(mailbox_name='inbox', msg_id='1,3,5-8,11'):
    print(msg)
#'mailbox_name' and 'msg_id' are optional, the user will be promted to input the two parameters if either is missing
>>>msgs = client.retrieve_msg()
0. "INBOX"
1. "Templates"
...
Please select a mailbox:1
message id: 1 2 3 4 5 6 ...
Please select mail ID to retrieve email(e.g. 1-5,6,7): 1,3-6
```

Additonal features: 
1. Specify variable `delete=True` to delete the messages that have been retrieved, default value is `False`
2. Specify variable `msg_id='all'` to retrieve all messages

#### Search emails via IMAP  
Refer to [RFC3501](https://tools.ietf.org/html/rfc3501#section-6.4.4) for more search options
```python
>>>for msg in client.retrieve_msg(mailbox_name='inbox', search_section='body', search_text='test_search'):
		print(msg)
```


