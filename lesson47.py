# Checking your Email inbox

import imapclient

# connecting to domain name based on email provider
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# login credentials
conn.login('jordan.newberry@gmail.com', 'ILov3C4ll3y!')

# selecting inbox folder with readonly state
conn.select_folder('INBOX', readonly=True)

# searching the inbox
# other search methods are on google under IMAP search keys
UIDs = conn.search(['SINCE', '01-May-2021'])

print(UIDs)

rawMessage = conn.fetch(['32820'], ['BODY[]', 'FLAGS'])

print(rawMessage)

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[32820][b'BODY[]'])

print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('bcc'))

message.text_part
message.html_part
print(message.text_part.get_payload().decode('UTF-8'))
print(message.html_part.get_payload().decode('UTF-8'))


# returns list of all folders for email account
conn.list_folders()

# to delete emails
conn.select_folder('INBOX', readonly=False)

UIDs2 = conn.search(['ON', '24-Aug-2015'])

print(UIDs2)

conn.delete_messages(['pass in UIDs to be deleted here'])

# logging out

conn.logout()


