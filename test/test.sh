sudo apt-get install inotify-tools

inotifywatch -v -e access -e modify -e open -e moved_to -e create -e delete -t 20 -r ~/Dropbox/code/VDISK


whatever@whatever:~/Dropbox/code/VDISK$ inotifywatch -v -e access -e modify -e open -e moved_to -e create -e delete -t 20 -r ~/Dropbox/code/VDISK
Establishing watches...
Setting up watch(es) on /home/whatever/Dropbox/code/VDISK
OK, /home/whatever/Dropbox/code/VDISK is now being watched.
Total of 39 watches.
Finished establishing watches, now collecting statistics.
Will listen for events for 20 seconds.
total  access  open  moved_to  create  filename
26     7       18    0         1       /home/whatever/Dropbox/code/VDISK/src/
19     8       10    1         0       /home/whatever/Dropbox/code/VDISK/
2      0       2     0         0       /home/whatever/Dropbox/code/VDISK/src/Untitled Folder/
