#! python
# -*- coding:utf-8 -*-

import os
import sys
import json
from writer import *

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

class JsonarrayWriter(Writer):
    # 文件后缀
    def suffix(self):
        return ".json"

    # 文件内容(字符串)
    def context(self,ctx):
        return json.dumps(ctx,ensure_ascii=False,\
            indent=4,sort_keys=True,separators=(',', ':') )



