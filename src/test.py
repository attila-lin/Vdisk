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

oauth2 = OAuth2('1734683723', '9a60088a5b1d27e261ef532c551a3298', 'http://10.214.9.220/')

# print oauth2.authorize()

# code = '729d580421625fca46273609aca3d582'
# print oauth2.access_token(code = code)

string = '{"access_token":"6df7806662f5c9H1ToytJ3KZkzH80b52","expires_in":1383674205,"time_left":85780,"uid":"2055149073","refresh_token":"75e36b6662f5c9H1ToytJ3KZkzH6bf0e"}'
acc = eval(string)
print acc['access_token']

# {
# 	"access_token":"6df7806662f5c9H1ToytJ3KZkzH80b52",
# 	"expires_in":1383674205,
# 	"time_left":85780,
# 	"uid":"2055149073",
# 	"refresh_token":"75e36b6662f5c9H1ToytJ3KZkzH6bf0e"
# }

client = Client()
info = client.account_info(acc['access_token'])


# {"uid":"1764170","sina_uid":"2055149073","quota_info":{"quota":"96292831232","consumed":"2090080985"},"verified":false,"screen_name":"\u660a\u58a8\u662f\u4e2a\u51b7\u573a\u5e1d","user_name":"\u660a\u58a8\u662f\u4e2a\u51b7\u573a\u5e1d","location":"\u6d59\u6c5f \u5b81\u6ce2","profile_image_url":"http:\/\/tp2.sinaimg.cn\/2055149073\/50\/40031506387\/1","avatar_large":"http:\/\/tp2.sinaimg.cn\/2055149073\/180\/40031506387\/1","gender":"m"}