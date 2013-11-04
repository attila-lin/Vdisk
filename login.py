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


client_secret = '9a60088a5b1d27e261ef532c551a3298'
client_id = '1734683723'

http = httplib2.Http('.cache')

url = "http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js"
response, content = http.request(url, 'GET')


servertime = content[content.find("servertime")+12:content.find(",\"pcid")]
pcid = content[content.find("pcid")+7:content.find("\",\"nonce")]
print pcid
nonce = content[content.find("nonce")+8:content.find("\",\"pubkey")]
print "nonce = " + nonce
pubkey = content[content.find("pubkey")+9:content.find("\",\"rs")]

# sinaSSOController.preloginCallBack({
# 	"retcode":0,
# 	"servertime":1369217685,
# 	"pcid":"yf-4d246eb08235f2151d0e8296b5352981d4d6",
# 	"nonce":"2HX83A",
# 	"pubkey":"EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443",
# 	"rsakv":"1330428213","exectime":1})


username = raw_input('username:')
password = raw_input('password:')
username = urllib.quote(username)
username = base64.encodestring(username)[:-1]

rsaPublickey = int(pubkey, 16)
key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
passwd = rsa.encrypt(message, key) #加密
passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。

print username
print passwd

def login():
	loginurl = 'http://login.sina.com.cn/sso/login.php'
	# http://login.sina.com.cn/sso/login.php?
	# entry=weibo&
	# gateway=1&
	# from=&
	# savestate=7&
	# useticket=0&
	# pagerefer=&
	# vsnf=1&
	# su=Nzk5NzU4NzMwJTQwcXEuY29t&
	# service=miniblog&
	# servertime=1369212875&
	# nonce=FEIDKX&
	# pwencode=rsa2&
	# rsakv=1330428213&
	# sp=341de811b5df77022ebf0542774e64aa0d8291ef75aa85e1ee09bc48e9de63a01910af8091670f15fe65aaff54d7168893b66b6a3bd9674caf225c91da5fddf72915fed0e0733c07abfa59d63b72394c9abf817f22e256d53045ca0f142de83e4917327086134e5fcfcaf64697e97d715180d9b10592521f68b789ba54d62d5f&
	# encoding=UTF-8&
	# callback=sinaSSOController.loginCallBack&
	# cdult=3&
	# domain=sina.com.cn&
	# prelt=89&
	# returntype=TEXT&
	# client=ssologin.js(v1.4.5)&
	# _=1369212860662
	postPara = {
		'entry': 'weibo',
		'gateway': '1',
		'from': '',
		'savestate': '7',
		'userticket': '0',
		'ssosimplelogin': '1',
		'vsnf': '1',
		'vsnval': '',
		'su': encodedUserName,
		'service': 'miniblog',
		'servertime': serverTime,
		'nonce': nonce,
		'pwencode': 'rsa2',
		'sp': encodedPassWord,
		'encoding': 'UTF-8',
		'prelt': '115',
		'rsakv' : rsakv,
		'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
		'returntype': 'META'
	}
	response, content = http.request(gettokenurl, 'POST', headers=headers, body=body)

