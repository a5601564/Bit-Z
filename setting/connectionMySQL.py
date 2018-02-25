#coding:utf-8

import MySQLdb
import MySQLdb.cursors
from sshtunnel import SSHTunnelForwarder

class   connectionMySQL:
    def __init__(self):
        self.server = SSHTunnelForwarder(
                ('112.124.45.189', 22),  # B机器的配置
                ssh_password = 'penghoulei',
                ssh_username = 'penglei',
                remote_bind_address = ('127.0.0.1', 3306)  )
        self.server.start()
        self.conn = MySQLdb.connect(
                                    host='127.0.0.1',  # 此处必须是是127.0.0.1
                                    port=self.server.local_bind_port,
                                    user='root',
                                    passwd='sdfgheeccdxfdr3d',
                                    db='haiwai',
                                    cursorclass = MySQLdb.cursors.DictCursor,
                                    charset='utf8'
        )

    def GetDate(self,SQL):
        cur = self.conn.cursor()
        cur.execute(SQL)
        date = cur.fetchall()
        for value in date:
            return value     #返回查询结果
        cur.close()
        self.server.close()


