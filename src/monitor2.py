#!/usr/bin/env python
#encoding=utf8
import os
import subprocess
import time
import sys
from  pyinotify import WatchManager, Notifier,ProcessEvent,IN_DELETE, IN_CREATE,IN_MODIFY

class rsync_file_cmd():
    def __init__(self,src_file,dst,dst_file):
        self.src_file=src_file
        self.dst=dst
        self.dst_file=dst_file
        self.cmd='rsync -arz --timeout=60 -e "ssh -p 22" %s %s:%s' %(self.src_file,self.dst,self.dst_file)
        self.del_cmd='ssh -p 22  %s "rm -rf %s"' % (self.dst,self.dst_file)

class EventHandler(ProcessEvent):
    """Handle"""
    def process_IN_CREATE(self, event):
        if event.name.startswith('.') or event.name.endswith('~') or event.name=='4913':
            pass
        else:
            create_sync=rsync_file_cmd(str(event.pathname),'root@198.72.107.18',str(event.pathname))
            subprocess.call(create_sync.cmd,shell=True)
    def process_IN_DELETE(self, event):
        if event.name.startswith('.') or event.name.endswith('~') or event.name=='4913':
            pass
        else:
            delete_sync=rsync_file_cmd(str(event.pathname),'root@198.72.107.18',str(event.pathname))
            subprocess.call(delete_sync.del_cmd,shell=True)
    def process_IN_MODIFY(self, event):
        if event.name.startswith('.') or event.name.endswith('~') or event.name=='4913':
            pass
        else:
            modify_sync=rsync_file_cmd(str(event.pathname),'root@198.72.107.18',str(event.pathname))
            subprocess.call(modify_sync.cmd,shell=True)

def FSMonitor(path='/root/wpf'):
    wm = WatchManager()
    mask = IN_DELETE | IN_MODIFY | IN_CREATE
    notifier = Notifier(wm, EventHandler(),read_freq=10)
    notifier.coalesce_events()
    # 设置受监视的事件，这里只监视文件创建事件，（rec=True, auto_add=True）为递归处理
    wm.add_watch(path,mask,rec=True, auto_add=True)
    notifier.loop()
    
if __name__=='__main__':
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        print >>sys.stderr, 'fork failed: %d (%s)' % (e.errno, e.strerror)
        sys.exit(1)
    os.setsid()
    os.umask(0)
    FSMonitor()
    print 'start!'