# -*- coding:utf-8 -*-
from multiprocessing import Pool
import os, pymysql, binascii


def how_task(conn, uid):
    print conn;
    #根据uid获取jfz_account_info_*表的数据
    cursor = conn.cursor()

    table_id = int(float(uid) % 10)
    if table_id == 0:
        table_id = 10
    getUserInfoSql = "select * from jfz_account_info_" + str(table_id) + " where uid =" + uid
    #print (getUserInfoSql)
    cursor.execute(getUserInfoSql)
    data = cursor.fetchone()
    phone = data[2]
    print(phone)
    accountComp = phone + "_1"
    account_id = int('0x%x' % (binascii.crc32(accountComp) & 0xffffffff), 16) % 10
    if account_id == 0:
        account_id = 10

    getAccountInfoSql =  "insert into jfz_accountt_indicator_" + str(account_id) + " select * from jfz_account_indicator_" + str(account_id) + " where uid =" + uid+";"
    #jfz_account_info_＊信息倒入新库
    getUserInfoSql = "insert into jfz_accountt_info_" + str(table_id) + " select * from jfz_account_info_" + str(table_id) + " where uid =" + uid + ";"
    try:
        #print "sql: "+getUserInfoSql
        #print "sql: "+getAccountInfoSql
        cursor.execute(getUserInfoSql)
        cursor.execute(getAccountInfoSql)
        conn.commit()
    except:
        conn.rollback()
        print "err"+uid

    cursor.close()
    conn.close()

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(200)
    conn = pymysql.connect(host='10.1.2.250', port=3306, user='root', passwd='', db='jfz_account_test')
    with open(os.path.dirname(__file__) + '/1.csv', 'r') as f:
        for line in f.readlines():
            uid = line.strip()  # 把末尾的'\n'删掉
            if uid == "":
                continue
            p.apply_async(how_task, args=(conn, uid,))

    p.close()
    p.join()

    print("end process")
