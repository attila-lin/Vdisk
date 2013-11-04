# -*- coding: utf-8 -*-

import urllib
import cookielib, urllib2
import re						#
import string
import time
import httplib2
import hmac
import hashlib
import time
import webbrowser
import rsa
import base64
import binascii


http = httplib2.Http('.cache')


def authorize():
	authorizeurl = 'https://auth.sina.com.cn/oauth2/authorize?client_id=1734683723&redirect_uri=http://10.214.9.220/&response_type=token'
	
	# headers = {}
	# headers['Content-Type'] = 'text/html,application/xhtml+xml,application/xml'
	# response, content = http.request(authorizeurl, 'GET', headers=headers)
	# print response

	webbrowser.open(authorizeurl)
	
	#print content


def access_token():
	gettokenurl = 'https://auth.sina.com.cn/oauth2/access_token' 

	body = {
		'client_id': client_id, 
		'client_secret': client_secret,
		'grant_type': 'refresh_token',
	}

	body=urllib.urlencode(body)

	headers = {'Content-Type': 'text/html,application/xhtml+xml,application/xml'}
	response, content = http.request(gettokenurl, 'POST', headers=headers, body=body)

	print response
	print content


def keep():
	keepurl = 'http://api.weipan.cn/?a=keep'

# 	{
#     "err_code":0,
#     "err_msg":"success",
#     "dologid":"72824",
#     "dologdir":[0,70203,103730]
# }

# 0: success.
# 602: dolog old

	body = {
		token: token,
		dologid: dologid
	}

	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	#text/html,application/xhtml+xml,application/xml
	response, content = http.request(keepurl, 'POST', headers=headers, body=urllib.urlencode(body))


def keeptoken():
	keeptokenurl = 'http://api.weipan.cn/?m=user&a=keep_token'

# 0: success
# 702: invalid token.
# 900: 超出了请求限制

	body = {
		token: token,
		dologid: dologid
	}
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	#text/html,application/xhtml+xml,application/xml
	response, content = http.request(keeptokenurl, 'POST', headers=headers, body=urllib.urlencode(body))

def uploadfile():
	uploadurl = 'http://api.weipan.cn/?m=file&a=upload_file'
	body = {
		token: token,
		dir_id: dir_id,  #目录的id, 0为根目录
		cover: 'yes', #重名时是否覆盖, yes或no
		file: file,    #文件
		dologid: dologid  #参考dolog机制
	}

def info():
	url = "https://api.weipan.cn/2/account/info"
	response, content = http.request(keeptokenurl, 'POST', headers=headers, body=urllib.urlencode(body))

authorize()
