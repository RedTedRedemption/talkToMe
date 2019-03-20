import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import select
from systemd import journal

import rule
import rules


credsfile = open("/etc/talkToMe/creds", 'r')
creds = credsfile.read().split(":")

mailListfile = open('/etc/talkToMe/maillist', 'r')
mailList = mailListfile.read().split(",")

credsfile.close()
mailListfile.close()

j = journal.Reader()
j.log_level(journal.LOG_INFO)

j.seek_tail()
j.get_previous()

p = select.poll()

p.register(j, j.get_events())


def loadConfig():

	credsfile = open("/etc/talkToMe/creds", 'r')
	creds = credsfile.read().split(":")

	mailListfile = open('/etc/talkToMe/maillist', 'r')
	mailList = mailListfile.read().split(",")

	credsfile.close()
	mailListfile.close()

loadConfig()


server = smtplib.SMTP(creds[2] + ":587")
server.ehlo()
server.starttls()
print("SMTP login successful")

server.login(creds[0], creds[1])


def connect():
	server = smtplib.SMTP(creds[2] + ":587")
	server.ehlo()
	server.starttls()
	print("SMTP login successful")

	server.login(creds[0], creds[1])

def sendMessage(msg):
    mailListfile = open('/etc/talkToMe/maillist', 'r')
    mailList = mailListfile.read().split(",")
    mailListfile.close()
    
    for recipiant in mailList:
        server.sendmail(creds[0], recipiant, msg)

def close():
	server.quit()

loadConfig()

sendMessage("talkToMe service has started")

while p.poll():
    

    for entry in j:
        for testRule in rule.Rule.rules:
            if testRule.test(entry):

               message = MIMEMultipart("alternative")
               message["Subject"] = "Email alert from talkToMe - %s" % testRule.subject
               
               text = testRule.message + "\n" + entry["MESSAGE"] + "\n\n" + str(entry)

               plainText = MIMEText(text, "plain")

               message.attach(plainText)

               sendMessage(message.as_string())
               print(str(entry))
        

    j.process()




