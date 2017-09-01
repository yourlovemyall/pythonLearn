getUserInfoSql = "insert into jfz_accountt_info_" + str(table_id) + " select * from jfz_account_info_" + str(table_id) + " where uid =" + uid
print (getUserInfoSql)
getAccountInfoSql = ""
try:
    res = cursor.execute(getUserInfoSql)
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
except:
    print ('sql err.')