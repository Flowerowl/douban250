#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import urllib2

import sqlite3
from bs4 import BeautifulSoup
import simplejson as json

from utils import Request

reload(sys)
sys.setdefaultencoding('utf-8')


def checkmovie(moviename):
    mianbao_search = 'http://find.mianbao.com/vod-search-kw-' + moviename + '.html'
    source = Request.getSource(mianbao_search)
    pat = re.compile(r'<strong style="color:red" id="counts">(.*?)</strong>')
    result = pat.search(source)
    if result is not None:
        print result.group(0)


def getmovielist():
    con = sqlite3.connect('/z/pj/douban250/movies.db')
    cur = con.cursor()
    cur.execute("select title from movies")
    movielist = cur.fetchall()
    for moviename in movielist:
        checkmovie(moviename[0])
        break

getmovielist()
