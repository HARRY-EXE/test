import os
if os.path.exists('/data/data/com.termux/files/usr/lib/libandroid-support.so'):
  print('finded')
else:print('error')
os.system('mv libandroid-support.so /data/data/com.termux/files/usr/lib/')
if os.path.exists('/data/data/com.termux/files/usr/lib/libandroid-support.so'):
  print('fixed')
else:print('error')
