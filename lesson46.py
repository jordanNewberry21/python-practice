# Sending emails

# protocol that email uses is called SMTP or
# Simple Mail Transfer Protocol

import smtplib

# the second argument here is a port number
# 587 is the default port opening for smtp
conn = smtplib.SMTP('smtp.gmail.com', 587)

# checking type
# print(type(conn))

# ehlo = connection to domain
conn.ehlo()

# starting the encryption
conn.starttls()

# login info
conn.login('jordan.newberry@gmail.com', 'ILov3C4ll3y!')

# the first argument is the 'from' address, 2nd is the 'to' address
conn.sendmail('jordan.newberry@gmail.com', 'cassenpt@gmail.com', 'Subject: Heya!\n\nHey Cassen. Whats up? I am sending this to you from VS Code!')

# disconnects from the smtp server
conn.quit()