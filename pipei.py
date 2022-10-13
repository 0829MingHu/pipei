import os
import shutil

num=0
apath=r"/home/chenj0g/rgb_flow/rgbflow"#1
bpath=r"/home/chenj0g/rgb_flow/move/rgb"#2

s=set()
flag=False
for curdir,roots,files in os.walk(apath):
    if flag==False:
        flag=True
        continue
    s.add(curdir.split('/')[-1])
print(s)
m=set()
for i in s:
    num=0
    for curdir,roots,files in os.walk(apath+'/'+i):
        for file in files:
            num=num+1
    for curdir,roots,files in os.walk(bpath+'/'+i):
        for file in files:
            num=num-1
    if not num==0:
        m.add(i)
print(m)
cpath=r"/home/chenj0g/rgb_flow/video"#要筛选的.mp4路径
epath=r"/home/chenj0g/rgb_flow/pipei_queshi"#要存放筛选完mp4的路径
for i in m:
    print(cpath+"/"+i+'.mp4',epath+"/"+i+'.mp4')
    # shutil.move(cpath+"/"+i+'.mp4',epath+"/"+i+'.mp4')