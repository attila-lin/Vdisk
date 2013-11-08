#!/usr/bin/env python
# encoding: utf-8

import sys
import time
import os

reload(sys)
sys.setdefaultencoding('utf-8')


import wx

import Vfunc 

class CheckDialog(wx.MessageDialog):
    """docstring for ClassName"""
    def __init__(self, parent, message):
        wx.MessageDialog.__init__(self, parent, message, caption="验证", style= wx.YES_NO|wx.ICON_QUESTION)
       

# class SetPathFrame(wx.Frame):
#     '''
#     SetPathFrame
#         组成有：
            
#     '''
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, '设置路径',size=(300, 200))
#         self.panel = wx.Panel(self)

#         self.beginlabel = wx.StaticText(self.panel, -1, "Begin:", (70, 20))
#         self.begintext = wx.TextCtrl(self.panel, -1, style=wx.TE_LEFT, pos=(140, 20))  



class Shell(wx.Frame):
    '''
    主窗口
        组成有：
            
    '''
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Vdisk',size=(350, 420))
        self.panel = wx.Panel(self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.firststep = wx.StaticBox(self.panel, label = "第一步" )
        self.FirstSizer = wx.StaticBoxSizer(self.firststep, wx.VERTICAL) 
        self.checkbutton = wx.Button(self.panel, label = "验证", size = (50, 30))
        self.FirstSizer.Add(self.checkbutton)

        self.secondstep = wx.StaticBox(self.panel, label = "第二步" )
        self.SecondSizer = wx.StaticBoxSizer(self.secondstep, wx.VERTICAL)
        self.setPathbutton = wx.Button(self.panel, label = "设置路径", size = (100, 30))
        self.pathText = wx.TextCtrl(self.panel, -1, "", size=(300,30))
        self.SecondSizer.Add(self.setPathbutton)
        self.SecondSizer.Add(self.pathText)

        self.thirdstep = wx.StaticBox(self.panel, label = "第三步" )
        self.ThirdSizer = wx.StaticBoxSizer(self.thirdstep, wx.VERTICAL)
        self.setOKbutton = wx.Button(self.panel, label = "启用Vdisk，并将云端文件下载到本地", size = (250, 30))
        
        self.ThirdSizer.Add(self.setOKbutton)

        self.sizer.Add(self.FirstSizer, proportion=1, flag=wx.ALL|wx.EXPAND, border=2)
        self.sizer.Add(self.SecondSizer, proportion=1, flag=wx.ALL|wx.EXPAND, border=2)
        self.sizer.Add(self.ThirdSizer, proportion=1, flag=wx.ALL|wx.EXPAND, border=2)

        self.panel.SetSizer(self.sizer)

        self.Bind(wx.EVT_BUTTON, self.Check, self.checkbutton)
        self.Bind(wx.EVT_BUTTON, self.SetPath, self.setPathbutton)


    def Check(self, event):
        myid = Vfunc.getid()
        weburl = Vfunc.geturl(myid)
        Vfunc.openbrowser(weburl)
        
        dlg = CheckDialog(parent = None, message = "是否验证成功，如果成功请按确定，如果失败请按失败")
        if dlg.ShowModal() == wx.ID_YES:
            mycode = Vfunc.getcode(myid)
            acc_access_val, acc_expire_val, acc_uid_val, acc_refresh_token = Vfunc.getaccess(mycode)
            client = Vfunc.getClient(acc_access_val)
            self.firststep.SetBackgroundColour('GREEN')
        dlg.Destroy()

    def SetPath(self, event):
        print "setPath"
        # setpathframe = SetPathFrame(parent=None, id=-1)
        # setpathframe.Show()
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*" 
        # 选择文件夹
        dlg = wx.DirDialog(
                            None, 
                            message="请选择Vdisk的目录", 
                            defaultPath="", 
                            style=wx.DD_DEFAULT_STYLE, 
                            # pos=DefaultPosition, size=DefaultSize, name=DirDialogNameStr
                            )
        if dlg.ShowModal() == wx.ID_OK:
            self.dirpath = dlg.GetPath()
            self.pathText.AppendText(self.dirpath)
            self.secondstep.SetBackgroundColour('GREEN')
            print self.dirpath
            dlg.Destroy()



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Shell(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
