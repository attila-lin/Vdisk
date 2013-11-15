#!/usr/bin/env python
# encoding: utf-8

import sys
import time
import os
import wx

reload(sys)
sys.setdefaultencoding('utf-8')

import Vfunc 

class CheckDialog(wx.MessageDialog):
    """docstring for ClassName"""
    def __init__(self, parent, message):
        wx.MessageDialog.__init__(self, parent, message, caption="验证", style= wx.YES_NO|wx.ICON_QUESTION)
       

import threading
class MyThread(threading.Thread):
    def run(self):
        # begin to do 
        # 
        import monitor
        notifier = Notifier(wm, PFilePath())
        wdd = wm.add_watch('.', mask, rec=True)
     
        while True:
            # print 'MyThread extended from Thread'
            try :
                notifier.process_events()
                if notifier.check_events():
                    notifier.read_events()
            except KeyboardInterrupt:
                notifier.stop()
                break

            # 普通授权：30 次/分钟
            time.sleep(5)
            
            

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
        self.Bind(wx.EVT_BUTTON, self.Save2Path, self.setOKbutton)


    def Check(self, event):
        myid = Vfunc.getid()
        weburl = Vfunc.geturl(myid)
        Vfunc.openbrowser(weburl)
        
        dlg = CheckDialog(parent = None, message = "是否验证成功，如果成功请按确定，如果失败请按失败")
        if dlg.ShowModal() == wx.ID_YES:
            mycode = Vfunc.getcode(myid)
            Vfunc.ACCESSVAL, Vfunc.ACCEXPIRE, Vfunc.ACCUID, Vfunc.ACCFRESH = Vfunc.getaccess(mycode)
            Vfunc.saveattributes( Vfunc.ACCESSVAL, Vfunc.ACCEXPIRE, Vfunc.ACCFRESH)
            Vfunc.CLIENT = Vfunc.getClient()
            self.firststep.SetBackgroundColour('GREEN')
        dlg.Destroy()


    def SetPath(self, event):
        # print "SetPath()"
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*" 
        # 选择文件夹
        dlg = wx.DirDialog(
                            None, 
                            message="请选择Vdisk的目录", 
                            defaultPath="/home/whatever/Dropbox/code/VDISK/test", 
                            style=wx.DD_DEFAULT_STYLE, 
                            # pos=DefaultPosition, size=DefaultSize, name=DirDialogNameStr
                            )
        if dlg.ShowModal() == wx.ID_OK:
            self.dirpath = dlg.GetPath()
            self.pathText.AppendText(self.dirpath)
            self.secondstep.SetBackgroundColour('GREEN')
            print self.dirpath
            dlg.Destroy()

    def Save2Path(self, event):
        info = Vfunc.CLIENT.account_info(Vfunc.ACCESSVAL)
        print Vfunc.ACCESSVAL
        print info
        # for test,have to use sandbox
        Vfunc.CLIENT.setRoot("sandbox")
        # print Vfunc.CLIENT.delta(Vfunc.ACCESSVAL)
        t = MyThread()
        t.start()
        self.Destroy()
       
        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Shell(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
