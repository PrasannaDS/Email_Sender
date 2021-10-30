import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'python.prasanna@gmail.com'
email['to'] = 'satya.bhaskar@gmail.com'
email['subject'] = 'Helloooo Bhaskar!! lol!!!! from me'
email.set_content(html.substitute({'name':'Basi','new':'\n'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('python.prasanna@gmail.com', '12thMay2017')
    smtp.send_message(email)
    print('all good!!')