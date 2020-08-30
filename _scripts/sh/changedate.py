import sys
import os
import time

curpath = os.getcwd()
#filepath = curpath+ "/" + sys.argv[1]
filepath = sys.argv[1]
#t = time.localtime(os.path.getctime(filepath))
date = time.strftime("%Y-%m-%d %H:%M:%S %z")

print("文件路径:" + filepath)
print("获取的时间为:" + date)

data = ''
with open(filepath, 'r+', encoding='utf-8') as f:
  for line in f.readlines():
    if(line.find('date:') == 0):
      line = 'date: ' + date + '\n'
    data += line
with open(filepath, 'r+', encoding='utf-8') as f:
  f.writelines(data)