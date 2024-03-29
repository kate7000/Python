#The result is a text file with a list of addresses to which it was not possible to send an email


import datetime
import email
import imaplib
import re
import datetime


EMAIL_ACCOUNT = "my_mail@may_domen.com"
PASSWORD = "**********"

mail = imaplib.IMAP4_SSL('mail.my_domen.com')
mail.login(EMAIL_ACCOUNT, PASSWORD)
mail.list()
mail.select('name_folder')
# (ALL/UNSEEN)
result, data = mail.uid('search', None, '(HEADER Subject "Undelivered Mail Returned to Sender")')
i = len(data[0].split())

for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    # result, email_data = conn.store(num,'-FLAGS','\\Seen')
    # this might work to set flag to seen, if it doesn't already
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    # Header Details
    date_tuple = email.utils.parsedate_tz(email_message['Date'])
    if date_tuple:
        local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
        local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
        subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

    # Body details
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            body1 = part.get_payload(decode=True).decode(encoding='UTF-8', errors="ignore")
            result = re.search(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', body1)

            if result is not None:
                emails = str(result)
                email_result = re.search(r'[\w\.-]+@[\w\.-]+', emails)
                print(email_result.group(0))
                dt_now = datetime.date.today()
                file_name = "emails_" + str(dt_now) + ".txt"
                output_file = open(file_name, 'a')
                output_file.write("%s\n" %(email_result.group(0)))
                output_file.close()
        else:
            continue
