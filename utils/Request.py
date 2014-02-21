#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from gzip import GzipFile
from StringIO import StringIO


def getRequest(url):
    '''
    包装urllib2的请求
    '''
    encoding_support = ContentEncodingProcessor
    opener = urllib2.build_opener(encoding_support, urllib2.HTTPHandler)
    req = urllib2.Request(url)
    req.add_header(
        'User-Agent', 'Mozilla/5.0 (Windows;U;Windows NT 5.1;zh-CN;rv:1.9.2.9)Gecko/2010824Firefox/3.6.9')
    return req, opener


'''
支持gzip,defalte,加快加载速度
ref:http://www.pythonclub.org/python-network-application/observer-spider
'''


class ContentEncodingProcessor(urllib2.BaseHandler):

    """A handler to add gzip capabilities to urllib2 requests """

    # add headers to requests
    def http_request(self, req):
        req.add_header("Accept-Encoding", "gzip, deflate")
        return req

    # decode
    def http_response(self, req, resp):
        old_resp = resp
        # gzipπ
        if resp.headers.get("content-encoding") == "gzip":
            gz = GzipFile(
                fileobj=StringIO(resp.read()),
                mode="r"
            )
            resp = urllib2.addinfourl(
                gz, old_resp.headers, old_resp.url, old_resp.code)
            resp.msg = old_resp.msg
      # deflate
        if resp.headers.get("content-encoding") == "deflate":
            gz = StringIO(deflate(resp.read()))
            resp = urllib2.addinfourl(
                gz, old_resp.headers, old_resp.url, old_resp.code)  # 'class to add info() and
            resp.msg = old_resp.msg
            return resp

# deflate support
import zlib
# zlib only provides the zlib compress format, not the deflate format;


def deflate(data):
    try:               # so on top of all there's this workaround:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)

def getSource(url):
    """
    获取链接源码
    """
    # req, opener = getRequest(url)
    # # try:
    # #     urlopen = opener.open(req, timeout=10)
    # #     source = urlopen.read()
    # #     print source
    # #     return source
    # # except Exception:
    # #     print '获取网页源码失败'
    # urlopen = opener.open(req, timeout=10)
    # source = urlopen.read()
    try:
        urlopen = urllib2.urlopen(url, timeout = 20)
        source = urlopen.read()
        return source
    except:
        return None


