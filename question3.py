#!/bin/python3

import re
dir_path = 'blocklist.xml'
with open(r"blocklist.xml","r") as f:
    file=f.read()
    x=re.findall(r'(<.*blockID="[ig]\d*".*>)\n',file)
    y=re.findall(r'(<.*id="[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\..*?)\n',file)
print('3.1-----------------------------',end='\n')
for i in x:
    print(i)
print('3.2-----------------------------',end='\n')
for i in y:
    print(i)

