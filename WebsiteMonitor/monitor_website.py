import time
import smtplib
import datetime

from email.mime.text import MIMEText

import requests

def search_website(url, keyword):
    '''Search website at url for keyword'''
    req = requests.get(url)
    return req.status_code == 200 and keyword.casefold() in req.text.casefold()

def send_email(message):
    '''Log in with hard coded credentials and send message. The message should be an email.mime.text.MIMEText object'''
    server = smtplib.SMTP('smtp.googlemail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('username', 'password')
    server.send_message(message)
    server.quit()

if __name__ == '__main__':
    URL = ""
    KEYWORD = ""

    print(f"Searching for {KEYWORD} at {URL}")
    while True:
        if search_website(URL, KEYWORD):
            print(f"Keyword found at {datetime.datetime.now()}")
            print("Sending e-mail")
            message = MIMEText(f'{KEYWORD} found at {URL}!', _charset='utf-8')
            message['from'] = 'sender@sharklasers.com'
            message['to'] = 'recipient@sharklasers.com'
            message['cc'] = ''
            message['subject'] = f'{KEYWORD} detected!'
            send_email(message)
            print("Done")
            break
        else:
            print(f"Checked at {format(datetime.datetime.now())}. Not found")
        time.sleep(60)
