#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import sqlite3

# def getask():
# 	con = sqlite3.connect('/z/pj/douban250/ask.db')
# 	cur = con.cursor()
# 	f = open('/z/pj/douban250/newlist.py')
# 	for moviename in f.readlines():
# 		cur.execute("insert into movies(title) values('%s')" % moviename)
# 	con.commit()



getask()