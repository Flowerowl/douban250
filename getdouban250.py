#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sqlite3
import urllib2

from bs4 import BeautifulSoup
import simplejson as json

from utils import Request


def getmovielist():
	"""
	获取豆瓣电影250榜单电影名
	"""
	page = 0
	for i in range(10):
		link = 'http://movie.douban.com/top250?start=' + str(page) + '&filter=&format='
		source = Request.getSource(link)
		pat = re.compile(r'<img alt="(.*?)"')
		movielist = pat.findall(source)
		for movie in movielist:
			print urllib2.unquote(movie)
			dbinsert(movie)
		page += 25

def dbinsert(moviename):
	con = sqlite3.connect('/z/pj/douban250/movies.db')
	cur = con.cursor()
	cur.execute("insert into movies(title) values('%s')" % moviename)
	con.commit()

getmovielist()
