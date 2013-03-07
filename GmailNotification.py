#!/usr/local/bin/ python
#!coding:utf-8
import imaplib
import codecs
import commands
import sys


mail=imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(sys.argv[1],sys.argv[2])
mail.list()
mail.select("INBOX")
status,maillist=mail.search(None,"(UNSEEN)")

f=codecs.open('GmailNotification.cache','w','utf-8')

if(status=="OK"):
    if maillist[0] is not '':
       f.write("New got Mail")
       commands.getoutput(" terminal-notifier -message 新着メッセージが来ております -title 新着のGmail")
    else:
       f.write("Not Mail")
f.close()
