#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload( sys )
sys.setdefaultencoding('utf-8')

import urllib2
import simplejson as json

def pyunescape(jsescapse):
    """
    python解析经javascrpt的escapse()加密的字符串
    """
    try:
        unescaped = json.loads('"'+urllib2.unquote(jsescapse.replace('%u','\\u'))+'"')
        return unescaped
    except:
        return None
