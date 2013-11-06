#!/usr/bin/env python
# encoding: utf-8
# author: cookpan001

import sys
import logging
import time
import mimetypes
import urllib
import urllib2

from vdisksdk import *

oauth2 = OAuth2('1734683723', '9a60088a5b1d27e261ef532c551a3298', 'http://localhost/vdisk/getcode.php')

response = urllib2.urlopen('http://localhost/vdisk/getlastid.php')
myid = response.read()
print myid

# gain weburl

print oauth2.authorize(state = myid)

# code = '5dea2d25032d83522c0f6a7d56563907'
# print oauth2.access_token(code = code)

# string = '{"access_token":"938aeb6662f5c9H1ToytJ3KZkzHeb753","expires_in":1383806180,"time_left":86400,"uid":"2055149073","refresh_token":"75e36b6662f5c9H1ToytJ3KZkzH6bf0e"}'

# acc = eval(string)
# print acc['access_token']


# client = Client()
# info = client.account_info(acc['access_token'])
# print info

# {"uid":"1764170","sina_uid":"2055149073","quota_info":{"quota":"96292831232","consumed":"2090080985"},"verified":false,"screen_name":"\u660a\u58a8\u662f\u4e2a\u51b7\u573a\u5e1d","user_name":"\u660a\u58a8\u662f\u4e2a\u51b7\u573a\u5e1d","location":"\u6d59\u6c5f \u5b81\u6ce2","profile_image_url":"http:\/\/tp2.sinaimg.cn\/2055149073\/50\/40031506387\/1","avatar_large":"http:\/\/tp2.sinaimg.cn\/2055149073\/180\/40031506387\/1","gender":"m"}