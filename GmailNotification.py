#!/usr/local/bin/ python
#!coding:utf-8
import imaplib
import codecs
import commands
import sys
import datetime

mail=imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(sys.argv[1],sys.argv[2])
mail.list()
mail.select("INBOX")
status,maillist=mail.search(None,"(UNSEEN)")

f=codecs.open('GmailNotification.cache','w','utf-8')
f=codecs.open('GmailNotification.cache','w','utf-8')
now=datetime.datetime.now()
if(status=="OK"):
    if maillist[0] is not '':
       writestring="You got Mail"+now
       f.write(writestring)
    else:
       writestring=""
       f.write(writestring)
f.close()
