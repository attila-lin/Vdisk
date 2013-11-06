#!/usr/bin/env python
# encoding: utf-8

import sys
import time
import os

reload(sys)
sys.setdefaultencoding('utf-8')

from vdisksdk import *

# Application API
app_key = '1734683723'
app_secret = '9a60088a5b1d27e261ef532c551a3298'
call_back_url = 'http://localhost/vdisk/addcode.php'


# 1. get ID from servers
response = urllib2.urlopen('http://localhost/vdisk/getmyid.php')
myid = response.read()
print myid


# 2. get authenticate web url
# myid = '1'
oauth2 = OAuth2(app_key, app_secret, call_back_url)
#post id
weburl = oauth2.authorize(state = myid)


# 3. open a browser with the authenticate web
import webbrowser
webbrowser.open_new_tab(weburl)


# 4. waiting and ask whether you accept it with a dialog
# In the servers first I get the code with call_back_url.
# Then, store it with the myid(state)
# TODO
# 

import wx
class MessageDialog(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        wx.FutureCall(5000, self.ShowMessage)

        self.Centre()
        self.Show(True)

    def ShowMessage(self):
        wx.MessageBox('Download completed', 'Info')

app = wx.App()
MessageDialog(None, -1, 'MessageDialog')
app.MainLoop()


# 5. if accepted, get code with post myid to 'getcode.php'
# else ...


#TODO
import urllib2, urllib
# myid = 4
data = {
        'id' : myid,
        }
f = urllib2.urlopen(
        url     = 'http://localhost/vdisk/getcode.php',
        data    = urllib.urlencode(data)
    )
code = f.read()
print code



# 6. After getting code we can get access_token
access_token_str =  oauth2.access_token(code = code)
access_token_dir = eval(access_token_str)

print access_token_dir

acc_access_val = access_token_dir['access_token']
acc_expire_val = access_token_dir['expires_in']
acc_uid_val    = access_token_dir['uid']
acc_refresh_token = access_token_dir['refresh_token']

print acc_expire_val

# 7. use the sdk 
client = Client()
info = client.account_info(access_token_dir['access_token'])

print info
