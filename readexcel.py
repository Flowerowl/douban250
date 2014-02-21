#encoding:utf-8
import sys

import xlwt

reload(sys)
sys.setdefaultencoding('utf-8')


wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = wbk.add_sheet('sheet 1', cell_overwrite_ok=True)
sheet.write(0,0,'lazynight')

wbk.save('/z/pj/result.xls')
