#! python
# -*- coding:utf-8 -*-

import os
import sys
import json
from xml.dom.minidom import Document

try:
    basestring
except NameError:
    basestring = str

try:
    long
except NameError:
    long = int

# python3中没有unicode了
try:
    unicode
except NameError:
    unicode = str

# 加上不确定的层级缩进，60比较合适
BASE_LENGTH = 60
BASE_INDENT = "    "
INDENT_LIST = {}

class Writer(object):
    def __init__(self,doc_name,sheet_name, base_name, keys_list, comment_text):
        # 文件名包含中文则需要转unicode
        #self.doc_name   = unicode(doc_name, "utf-8")
        self.doc_name   = doc_name
        self.sheet_name = sheet_name
        self.base_name  = base_name
        self.keys_list   = keys_list
        self.comment_text   = comment_text

    # 文件后缀
    def suffix(self):
        pass
    # 文件内容
    def context(self,ctx):
        pass
    # 注释开始
    def comment_start(self):
        pass
    # 注释结束
    def comment_end(self):
        pass
    # 文件注释(千万不要加时间，影响svn)
    def comment(self):
        comment = []
        return "".join( comment )

