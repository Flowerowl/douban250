#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import sqlite3

import xlwt

reload(sys)
sys.setdefaultencoding('utf-8')


def createxls():
	con = sqlite3.connect('/z/pj/douban250/ask.db')
	cur = con.cursor()
	cur.execute('select * from movies')
	result = cur.fetchall()
	wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
	sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)
	for i, row in enumerate(result):
		for j, col in enumerate(row):
			sheet.write(i, j, col)
	wbk.save('/z/pj/douban250/ask.xls')

createxls()
