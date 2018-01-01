from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import smtplib
import os

def sendrep(vari):

        curtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        fromaddr = "jade@nextra01.xiv.ibm.com"
        toaddrs = ['borisso@tel-ad.co.il']
        subject = "Report "+ curtime
        msg = MIMEMultipart()
        msg["From"] = fromaddr
        msg["To"] = ",".join(toaddrs)
        msg["Subject"] = subject
        html = """	
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
        <strong><b>Testing mail:</b></strong>
        """ + vari + """ 
        <p><u>Testing text :</u><br>
        <a href="http://" </a> 
        <p>Using """ + os.path.realpath(__file__) +""" <p>
        <p>Generated at: """ + curtime + """
        <p>IVT Team.<br>
        All Rights Reserved © 2018 
        </body></html>
        """
        msg.attach(MIMEText(html, 'html'))
        server = smtplib.SMTP()
        server.connect('10.148.38.143')
        # server.send_message(msg)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
    # except:
    #    if ConnectionRefusedError():
    #        print('SMTP connection error, please check network and local Sendmail server')

sendrep('tst')