# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host = '10.1.2.250', port = 3306, user = 'root', passwd='', db='gunxueqiu');
cursor = conn.cursor();
phone = '15618879681';
cursor.execute("select * from gxq_user where phone ='"+phone+"'");

data = cursor.fetchall();
print(data);
# 提交，不然无法保存新建或者修改的数据
conn.commit();
cursor.close();
conn.close();