#!/usr/bin/env python
# encoding: utf-8

import sys
import time
import os

reload(sys)
sys.setdefaultencoding('utf-8')

from vdisksdk import *

##############################################################
#                       Define Area 
#
##############################################################

# Application API const value
app_key = '1734683723'
app_secret = '9a60088a5b1d27e261ef532c551a3298'
call_back_url = 'http://localhost/vdisk/addcode.php'

# SERVER const value
getidurl = 'http://localhost/vdisk/getmyid.php'
getcodeurl = 'http://localhost/vdisk/getcode.php'

oauth2 = OAuth2(app_key, app_secret, call_back_url)

# 1. get ID from servers
def getid():
    response = urllib2.urlopen( getidurl )
    myid = response.read()
    # print myid
    return myid

# 2. get authenticate web url
def geturl(myid):
    
    #post id
    weburl = oauth2.authorize(state = myid)
    return weburl


# 3. open a browser with the authenticate web
def openbrowser(weburl):
    import webbrowser
    webbrowser.open_new_tab(weburl)


# 4. waiting and ask whether you accept it with a dialog
# In the servers first I get the code with call_back_url.
# Then, store it with the myid(state)
# TODO
# 

# import wx
# class MessageDialog(wx.Frame):
#     def __init__(self, parent, id, title):
#         wx.Frame.__init__(self, parent, id, title)
#         wx.FutureCall(5000, self.ShowMessage)
#         self.Centre()
#         self.Show(True)
#     def ShowMessage(self):
#         wx.MessageBox('Download completed', 'Info')
# app = wx.App()
# MessageDialog(None, -1, 'MessageDialog')
# app.MainLoop()


# 5. if accepted, get code with post myid to 'getcode.php'
# else ...

#TODO
import urllib2, urllib

def getcode(myid):
    data = {
            'id' : myid,
            }
    f = urllib2.urlopen(
            url     = getcodeurl,
            data    = urllib.urlencode(data)
        )
    code = f.read()
    print code
    return code



# 6. After getting code we can get access_token
def getaccess(code):
    access_token_str = oauth2.access_token(code = code)
    access_token_dir = eval(access_token_str)

    # print access_token_dir

    acc_access_val = access_token_dir['access_token']
    acc_expire_val = access_token_dir['expires_in']
    acc_uid_val    = access_token_dir['uid']
    acc_refresh_token = access_token_dir['refresh_token']

    # print acc_expire_val
    return acc_access_val, acc_expire_val, acc_uid_val, acc_refresh_token

# 7. use the sdk to get Client API
def getClient(acc_access_val):
    client = Client(acc_access_val)
    info = client.account_info(acc_access_val)

    print info
    return client
