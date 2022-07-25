import smtplib
import random
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import json
from my_params import *

    
with open("quotes_bank.json", "r") as file:
    all_quotes = json.loads(file.read())
with open("emoji_bank.json", "r") as file:
    all_emoji = json.loads(file.read())

quote_of_the_day = random.choice(all_quotes)
emoji_of_the_day = random.choice(all_emoji)

msg = EmailMessage()
msg.set_content(f"{quote_of_the_day}\n{emoji_of_the_day}")
msg["To"] = "kamil.testenv@yahoo.com"
msg["From"] = my_email
msg['Subject'] = "Motivational Mail!"

image_cid = make_msgid(domain='gmail.com')
msg.add_alternative(f"""\
<html>
    <body>
        <img src="cid:{image_cid}">
        <p>{quote_of_the_day}<br>
            {emoji_of_the_day}
        </p>
        
    </body>
</html>
""".format(image_cid=image_cid[1:-1]), subtype='html')

with open('motivational_mail.png', 'rb') as img:

    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

    msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.send_message(msg)
