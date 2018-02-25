#coding:utf-8
import MySQLdb
class   GetMySql():
    def test(self):
        mydb={}
        mydb['host']    =   ""
        mydb['user']    =   ""      #用户名
        mydb['passwd']  =   ""      #密码
        mydb['db']      =   ""      #数据库名称
        conn  =   MySQLdb.connect(mydb)
        cursor = conn.cursor()
        cursor.execut("SELECT VERSION()")
        row = cursor.fetchone()
        print row[0]
        cursor.close()
        conn.close()

if  __name__=="__main__":
    GetMySql().test()