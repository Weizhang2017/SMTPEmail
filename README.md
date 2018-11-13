## A simple script to send MIME message via SMTP server

### Usage

```shell
>>>from SMTPEmail import SMTP
>>>client = SMTP(
			SMTP_server = <domain> or <IP_address>,
			SMTP_account = <account_name>,
			password = <password>
			)
>>>client.create_mime(
					recipient_email_addr='Jane.Doe@jane.com',
					sender_email_addr='John.Doe@john.com',
					subject='subject',
					sender_display_name='John Doe',
					recipient_display_name='Jane Doe',
					content_html='<p>hello world</p>',
					content_text='hello world'
					)
   
>>>print(client) #print the message

Subject: subject
From: John Doe <John.Doe@John.com>
To: Jane Doe <Jane.Doe@jane.com>
Date: Tue, 13 Nov 2018 17:52:01 +0800
Message-Id: 154210272151.1976.14038029430513051529@Jane.com
MIME-Version: 1.0
Content-Type: multipart/alternative;
 boundary="===============0340024224523524971=="

--===============0340024224523524971==
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

hello world

--===============0340024224523524971==
Content-Type: text/html; charset="utf-8"
Content-Transfer-Encoding: 7bit
MIME-Version: 1.0

<p>hello world</p>

--===============0340024224523524971==--

>>>client.send_msg()
```