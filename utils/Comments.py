#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import urllib2

import simplejson as json
from bs4 import BeautifulSoup

import pyunescape
from database import db
import Request

sys.path.insert(0, r'..')
reload(sys)
sys.setdefaultencoding('utf-8')


class Comments(object):
    """
    从各大视频网站播放地址提取评论
    """
    @classmethod
    def getCommentSohu(cls, playlink, moviename):
        if playlink != '':
            source = Request.getSource(playlink)
            if source is not None:
                m = re.search(r'vid\s*=\s*[\"\']\w+[\"\']', source)
                vid = m.group(0).split('"')[1]
                n = re.search(r'playlistId\s*=\s*[\"\']\w+[\"\']', source)
                playlistid = n.group(0).split('"')[1]
                jslink = 'http://access.tv.sohu.com/reply/list/1000_' + \
                    str(playlistid) + '_' + str(vid) + '_0_2000.js'
                commentsource = Request.getSource(jslink)
                try:
                    comments = re.search(r'\[.*\]', commentsource)
                    comments = comments.group(0).replace("'",'"')
                    pat = re.compile(r'content":"(.*?)"')
                    commentlist = pat.findall(comments)
                    for comm in commentlist:
                        unescomm = pyunescape.pyunescape(comm)
                        if unescomm is not None and unescomm != "":
                            db.insert((moviename, 'sohu', unescomm))
                except:
                    pass

    @classmethod
    def getCommentYouku(cls, playlink, moviename):
        if playlink != '':
            vid = playlink.split('_')[-1].split('.')[0]
            for page in range(1, 100):
                jslink = 'http://comments.youku.com/comments/~ajax/vpcommentContent.html?__ap={%22videoid%22:%22'+vid+'%22,'+'%22page%22:'+str(page)+'}'
                commentsource = Request.getSource(jslink)
                try:
                    pat = re.compile(r'content_(.*?)<br')
                    commentlist = pat.findall(commentsource)
                    for comm in commentlist:
                        comm = comm.split('">')
                        unescomm = pyunescape.pyunescape(comm[2])
                        if unescomm is not None and unescomm != "":
                            db.insert((moviename, 'youku', unescomm))
                except:
                    continue

    @classmethod
    def getCommentFunshion(cls, playlink, moviename):
        if playlink != '':
            vid = playlink.split('/')[-2]
            for page in range(1, 31):
                jslink = 'http://q.funshion.com/ajax/get_comment/media/'+vid+'/all?pg='+str(page)
                source = Request.getSource(jslink)
                try:
                    pat = re.compile(r'content":"(.*?)"')
                    commentlist = pat.findall(source)
                    for comm in commentlist:
                        unescomm = pyunescape.pyunescape(comm)
                        if unescomm is not None and unescomm != "":
                            db.insert((moviename, 'funshion', unescomm))
                except:
                    continue

    @classmethod
    def getCommentTudou(cls, playlink, moviename):
        jslink = 'http://www.tudou.com/comments/itemnewcomment.srv?jsoncallback=__Cmt_getCmt&tm=50013876&method=getCmt&iid=130785660&page=5&rows=50&charset=utf-8'

    @classmethod
    def getCommentLetv(cls, playlink, moviename):
        if playlink != '':
            vid = playlink.split('/')[-1].split('.')[0]
            for i  in range(1, 120):
                jslink = 'http://api.my.letv.com/vcm/api/g?type=video&xid='+str(vid)+'&page='+str(i)
                source = Request.getSource(jslink)
                try:
                    pat = re.compile(r'content":"(.*?)"')
                    commentlist = pat.findall(source)
                    for comm in commentlist:
                        unescomm = pyunescape.pyunescape(comm)
                        if unescomm is not None and unescomm != "":
                            db.insert((moviename, 'letv', unescomm))
                except:
                    continue

    @classmethod
    def getCommentIqiyi(cls, playlink, moviename):
        if playlink != '':
            source = Request.getSource(playlink)
            if source is not None:
                m = re.search(r'qitanid="\w+"', source)
                vid = m.group(0).split('"')[1]
                for page in range(1, 50):
                    jslink = 'http://api.t.iqiyi.com/qx_api/comment/get_video_comments?page='+str(page)+'&qitanid='+str(vid)
                    commentsource = Request.getSource(jslink)
                    pat = re.compile(r'content":"(.*?)"')
                    try:
                        commentlist = pat.findall(commentsource)
                        for comm in commentlist:
                            unescomm = pyunescape.pyunescape(comm)
                            if unescomm is not None and unescomm != "":
                                db.insert((moviename, 'iqiyi', unescomm))
                    except:
                        continue
