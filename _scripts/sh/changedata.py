import sys
import os

curpath = os.getcwd()
filepath = curpath+ "/" + sys.argv[1]
time = sys.argv[2]
print(filepath + " " + time)

data = ''
with open(filepath, 'r+', encoding='utf-8') as f:
  for line in f.readlines():
    if(line.find('date:') == 0):
      line = 'date: ' + time + '\n'
    data += line
with open(filepath, 'r+', encoding='utf-8') as f:
  f.writelines(data)