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
m=set()
for i in s:
    num1=0
    num2=0
    for curdir,roots,files in os.walk(apath+'/'+i):
        for file in files:
            if not 'flow' in file:
                num1=num1+1
    for curdir,roots,files in os.walk(bpath+'/'+i):
        for file in files:
            num2=num2+1
    if not num1==num2:
        m.add(i)
    print(num1, num2)
cpath=r"/home/chenj0g/rgb_flow/video"#要筛选的.mp4路径
epath=r"/home/chenj0g/rgb_flow/pipei_queshi"#要存放筛选完mp4的路径
for i in m:
    print(cpath+"/"+i+'.mp4',epath+"/"+i+'.mp4')
    # shutil.move(cpath+"/"+i+'.mp4',epath+"/"+i+'.mp4')