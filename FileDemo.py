# -*- coding:utf-8 -*-
import os;
#写文件
with open(os.path.dirname(__file__)+'/1.txt', 'w') as f:
    f.write('Hello World');

#追加写文件
with open(os.path.dirname(__file__)+'/1.txt', 'a') as f:
    f.write('22Hello World');

#读文件
with open(os.path.dirname(__file__) + '/1.txt', 'r') as f:
    print (f.read());
