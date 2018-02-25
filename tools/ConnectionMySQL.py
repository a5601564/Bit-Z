#coding:utf-8

"""
    action:连接数据库
"""

import MySQLdb
import MySQLdb.cursors
from sshtunnel import SSHTunnelForwarder

class ConnectionMySQL(object):

    def __init__(self):
        self.server = SSHTunnelForwarder(
            ('47.96.191.134', 22),    #跳板机
            ssh_username = 'phl',
            ssh_password = 'penghoulei',
            remote_bind_address = ('127.0.0.1', 3306)
        )
        self.server.start()
        self.conn = MySQLdb.connect(
            host = '127.0.0.1',
            port = self.server.local_bind_port,
            user = 'root',
            passwd = '&s6c1JfrYqn9yj4w',
            db = 'bitz_new',
            #cursorclass = MySQLdb.cursors.DctCursor,
            charset = 'utf8'
        )

    def getDate(self,sqlshell):
        sqlshell = ""
        self.cur = self.conn.cursor()
        self.cur.execute(sqlshell)
        data = self.cur.fetchall()
        print data[0]
        print type(data[0])
        self.conn.close()#
        self.server.close()
