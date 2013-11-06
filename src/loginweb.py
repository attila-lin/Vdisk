#!/usr/bin/env python
# encoding: utf-8

import wx 
import wx.html 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
 

# class MyHtmlFrame(wx.Frame): 
#     def __init__(self, parent, title): 
#         wx.Frame.__init__(self, parent, -1, title, size=(600,400)) 
#         html = wx.html.HtmlWindow(self) 
#         wx.CallAfter(html.LoadPage, "http://www.baidu.com") 
 
# app = wx.PySimpleApp() 
# frm = MyHtmlFrame(None, "Simple HTML Browser") 
# frm.Show() 
# app.MainLoop() 

import webbrowser
webbrowser.open_new_tab("http://www.google.com")