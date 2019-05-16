#! python
# -*- coding:utf-8 -*-

import os
import sys
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

class ErlanghrlWriter(Writer):
    # 文件后缀
    def suffix(self):
        return ".hrl"

    def comment(self):
        comment = [
            '%% Automatic generation from -->>'             
            '\n%% excel file  name : ' + self.doc_name +
            '\n%% excel sheet name : ' + self.sheet_name,
            '\n-record(' + self.base_name + ', {\n    '
        ]

        return "\n".join( comment )

    # 获取缩进字符串
    def indent_ctx( self,indent ) :
        if indent <= 0: return ""

        if indent not in INDENT_LIST :
            INDENT_LIST[indent] = ""
        else :
            ctx = BASE_INDENT*indent
            INDENT_LIST[indent] = ctx

        return INDENT_LIST[indent]

    def list_to_text(self, value, indent):
        list_text_list = []
        for k in self.comment_text :
            comment = self.comment_text[k]
            k_indent,lk = self.to_target_lang( k,indent )
            val_type = type( lk )
            if str == val_type :
                lk = lk.replace("\"", "\'")
            if None == comment :
                comment = ""
            val = "".join( [lk.ljust(20, " "), "\t%% ", comment, "\n"] )

            list_text_list.append( val )

        list_str = "    ,".join( list_text_list )
        list_str = list_str + "    })."
        return False, list_str

    # 转换为文本数据 之前解析出来的excel数据存放方式存在LIST(array格式)和DICT(object格式)两种类型
    def to_text(self,value,indent):
        val_type = type( value )
        if list == val_type :
           return self.list_to_text(value, indent)
        else :
            return False, None

    # python的dict转换为erlang的map类型
    def dict_to_erlang(self,value,indent):
        dict_ctx_list = []

        for k in ( value ) :
            k_indent,lk = self.to_target_lang( k,indent )
            is_indent,lv = self.to_target_lang( value[k],indent + 1 )

            val_type = type( lk )
            if str == val_type :
                lk = lk.replace("\"", "\'")
            key = "".join( [lk," => "] )
            val = "".join( [key, lv] )
            dict_ctx_list.append(val)

        dict_str = ",".join( dict_ctx_list )
        return False,"".join( ["#{",dict_str,"}"] )

    # python的list转换为erlang的list类型
    def list_to_erlang(self,value,indent):
        list_ctx_list = []
        for v in value :
            is_indent,lv = self.to_target_lang( v,indent + 1 )
            list_ctx_list.append( lv )


        list_str = ",".join( list_ctx_list )
        return False,"".join( ["[",list_str,"]"] )

    # python的tuple转换为erlang的tuple类型
    def tuple_to_erlang(self,value,indent):
        tuple_ctx_list = []

        for v in value :
            is_indent,lv = self.to_target_lang( v,indent + 1 )
            tuple_ctx_list.append( lv )

        # 返回 {a,b,c}这种不换行的格式
        list_str = ",".join( tuple_ctx_list )
        return False,"".join( ["{",list_str,"}"] )

    # 变量转换到目标语言的字符串
    def to_target_lang(self,value,indent):
        val_type = type( value )
        if int == val_type :
            return False,str( value )
        elif long == val_type :
            return False,str( value )
        elif float == val_type :
            # 1001.0 -->> 001 去除多余小数点
            if int( value ) == value :
                return False,str( int(value) )
            return False,str( value )
        elif str == val_type or unicode == val_type:
            return False, "".join(["\"",value,"\""])
        elif tuple == val_type :
            return self.tuple_to_erlang(value,indent)
        elif dict == val_type :
            return self.dict_to_erlang(value,indent)
        elif list == val_type :
            return self.list_to_erlang(value,indent)
        else :
            raise Exception( "invalid type",val_type )

    #文件内容
    def context(self,ctx):
        is_indent,str_ctx = self.to_text( ctx,0 )
        if None != str_ctx :
            return "".join( [self.comment(),"",str_ctx] )
        else :
            return None
