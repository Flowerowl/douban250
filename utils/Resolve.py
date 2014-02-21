#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

import Request
import Comments


class Resolve(object):
    """
    从各大视频网站的搜索页提取电影播放地址
    """
    @classmethod
    def resolveSohu(cls, movielink, moviename):
        """
        sohu:从电影搜索页提取该搜索结果的播放页地址
        """
        try:
            f = Request.getSource(movielink)
            source = BeautifulSoup(f)
            links = source.find_all('a', title='点击观看')
            playurl = links[0].get('href')
            Comments.Comments.getCommentSohu(playurl, moviename)
        except:
            pass
        # try:
        #     f = getSource(movielink)
        #     source = BeautifulSoup(f)
        #     links = source.find_all('a', title='点击观看')
        #     playurl = links[0].get('href')
        #     print playurl
        # except:
        #     print '从搜索结果提取播放地址失败'

    @classmethod
    def resolveYouku(cls, movielink):
        """
            youku:从电影搜索页提取该搜索结果的播放页地址
            去掉重定向到其他视频网站的链接，以及不存在的链接
        """
        try:
            f = Request.getSource(movielink)
            source = BeautifulSoup(f)
            links = source.find_all('div', "btnplay_s")
            if(len(links) != 0):
                playurl = links[0].find('a').get('href')
                if playurl[:7] != '/search':
                    print playurl
        except:
            print '从搜索结果提取播放地址失败'

    @classmethod
    def resolveFunshion(cls, movielink):
        """
        funshion:从电影搜索页提取该搜索结果的播放页地址
        """
        try:
            f = Request.getSource(movielink)
            source = BeautifulSoup(f)
            links = source.find_all('ul', "search_list")
            if(len(links) != 0):
                playurl = 'http://www.funshion.com' + \
                    links[0].find('a').get('href')
                print playurl
        except:
            print '从搜索结果提取播放地址失败'

    @classmethod
    def resolveTudou(cls, movielink):
        """
        tudou:从电影搜索页提取该搜索结果的播放页地址
        和优酷一样，都是从搜库提取数据，忽略之
        """
        try:
            f = Request.getSource(movielink)
            source = BeautifulSoup(f)
            links = source.find_all('div', "btnplay_s")
            if(len(links) != 0):
                playurl = links[0].find('a').get('href')
                # if playurl[:7] != '/search':
                print playurl
        except:
            print '从搜索结果提取播放地址失败'
