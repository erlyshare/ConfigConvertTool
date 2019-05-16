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
BASE_INDENT = "  "
INDENT_LIST = {}

class LuaWriter(Writer):
    # 文件后缀
    def suffix(self):
        return ".lua"

    def comment(self):
        comment = [
            '-- Automatic generation from -->>'
            '\n-- excel file  name: ' + self.doc_name +
            '\n-- excel sheet name: ' + self.sheet_name,
            '\nlocal ' + self.base_name + ' =\n'
        ]
        return "\n".join( comment )

    # 获取缩进字符串
    def indent_ctx( self,indent ):
        if indent <= 0: return ""

        if indent not in INDENT_LIST:
            ctx = BASE_INDENT*indent
            INDENT_LIST[indent] = ctx

        return INDENT_LIST[indent]

    def dict_to_text(self, value, indent) :
        dict_ctx_list = []

        cur_indent = self.indent_ctx(indent)
        next_indent = self.indent_ctx(indent + 1)

        tem_count = 0
        total_len = len(value)
        for k in ( value ) :
            tem_count += 1
            k_indent,lk = self.to_target_lang( k,indent )
            is_indent,lv = self.to_target_lang( value[k],indent + 1 )

            comment = self.comment_text[k]
            val = '-- ' + comment + '\n'
            dict_ctx_list.append(val)

            val_type = type( lk )
            if str == val_type :
                if lk.replace(".", "").isdigit() :
                    key = "".join( ["[",lk,"]"] )
                else :
                    key = lk.replace("\'", "")
            if tem_count != total_len :
                val = "".join( [cur_indent, key," =", lv, ",\n\n", cur_indent] )
            else :
                val = "".join( [cur_indent, key," = ",lv] )

            dict_ctx_list.append( val )
        dict_str = "".join( dict_ctx_list )

        return False,"".join( ["{\n", cur_indent, dict_str, "\n}"] )

    def list_to_dit(self, cur_key_index, total_key_cnt, onedict, storge_dict) :
        for k in ( onedict ) :
            key_index = self.keys_list.get(k, None)
            if None != key_index and key_index == cur_key_index :
                lv = onedict[k]
                if cur_key_index == total_key_cnt :
                    storge_dict[lv] = onedict
                else :
                    if None != storge_dict.get(lv, None) :
                        olddict = storge_dict[lv]
                        new_storge_dict = olddict
                        self.list_to_dit(cur_key_index + 1, total_key_cnt, onedict, new_storge_dict)
                    else :
                        storge_dict[lv] ={}
                        new_storge_dict = storge_dict[lv]
                        self.list_to_dit(cur_key_index + 1, total_key_cnt, onedict, new_storge_dict)

    def list_to_text(self, value, indent):
        list_text_list = []

        # 先把各个字段的注释放在前面
        comment_text_list = []
        for k in self.comment_text :
            comment = self.comment_text[k]
            k_indent,lk = self.to_target_lang( k,indent )

            lk = lk.replace("\'", "")

            if None == comment :
                comment = ""
            val = "".join( [ '--:  ', lk.ljust(20, " "), "\t## ", comment, "\n"] )

            comment_text_list.append( val )

        comment_str = "".join( comment_text_list )

        list_text_list.append(comment_str)

        ##  处理多个key的情况
        key_value_list = {}
        key_cnt = len(self.keys_list)
        for i, onedict in enumerate( value ) :
            self.list_to_dit(1, key_cnt, onedict, key_value_list)

        is_indent,lv = self.to_target_lang( key_value_list, 0 )
        list_str = "".join( lv )
        list_text_list.append(list_str)
        return False,"".join( list_text_list )

    # 转换为文本数据 之前解析出来的excel数据存放方式存在LIST(array格式)和DICT(object格式)两种类型
    def to_text(self,value,indent):
        val_type = type( value )
        if dict == val_type :
            return self.dict_to_text(value, indent)
        else :
            return self.list_to_text(value, indent)

    # dict转换为lua类型
    def dict_to_lua(self,value,indent):
        dict_ctx_list = []
        if indent % 2 != 0 :
            indent += 1
        cur_indent = self.indent_ctx(indent)
        next_indent = self.indent_ctx(indent + 1)

        dict_len = len(value)
        tem_count = 0
        for k in ( value ) :
            lvalue = value[k]
            lvalue_type = type(lvalue)
            if tuple != lvalue_type and dict != lvalue_type and list != lvalue_type :
                tem_count += 1
                k_indent,lk = self.to_target_lang( k,indent )
                is_indent,lv = self.to_target_lang( value[k],indent + 1 )

                if lk.replace(".", "").isdigit() :
                    key = "".join( ["[",lk,"]"] )
                else :
                    key = lk.replace("\'", "")

                if tem_count != dict_len :
                    val = "".join( [ next_indent, key + " = " + lv + ',\n' ] )
                else :
                    val = "".join( [ next_indent, key + " = " + lv ])
                dict_ctx_list.append( val )

        for k in ( value ) :
            lvalue = value[k]
            lvalue_type = type(lvalue)
            if tuple == lvalue_type or dict == lvalue_type or list == lvalue_type :
                tem_count += 1
                k_indent,lk = self.to_target_lang( k,indent )
                is_indent,lv = self.to_target_lang( value[k],indent + 1 )

                if lk.replace(".", "").isdigit() :
                    key = "".join( ["[",lk,"]"] )
                else :
                    key = lk.replace("\'", "")

                if tem_count != dict_len :
                    val = "".join( [ next_indent, key + " = " + lv + ',\n' ] )
                else :
                    val = "".join( [ next_indent, key + " = " + lv ])
                dict_ctx_list.append( val )

        dict_str = "".join(dict_ctx_list)
        return True,"".join(['\n', cur_indent,"{\n" , dict_str, "\n",cur_indent,"}"] )

    # list转换为lua类型
    def list_to_lua(self,value,indent):
        list_ctx_list = []
        if indent % 2 != 0 :
            indent += 1
        cur_indent = self.indent_ctx(indent)
        next_indent = self.indent_ctx(indent + 1)

        index_cnt = 1
        list_len = len(value)
        tem_count = 0
        for v in value :
            tem_count += 1
            is_indent,lv = self.to_target_lang( v,indent + 1 )
            if tem_count != list_len :
                val = "".join( [ next_indent, "[" + str(index_cnt) + "] = " + lv + ',\n' ] )
            else :
                val = "".join( [ next_indent, "[" + str(index_cnt) + "] = " + lv ])
            list_ctx_list.append( val )
            index_cnt += 1

        list_str = "".join(list_ctx_list)
        return True,"".join(['\n', cur_indent,"{\n" , list_str, "\n",cur_indent,"}"] )

     # tuple转换为lua类型
    def tuple_to_lua(self,value1,indent):
        value = list(value1)
        list_ctx_list = []
        if indent % 2 != 0 :
            indent += 1
        cur_indent = self.indent_ctx(indent)
        next_indent = self.indent_ctx(indent + 1)

        index_cnt = 1
        list_len = len(value)
        tem_count = 0
        for v in value :
            tem_count += 1
            is_indent,lv = self.to_target_lang( v,indent + 1 )
            if tem_count != list_len :
                val = "".join( [ next_indent, "[" + str(index_cnt) + "] = " + lv + ',\n' ] )
            else :
                val = "".join( [ next_indent, "[" + str(index_cnt) + "] = " + lv ])
            list_ctx_list.append( val )
            index_cnt += 1

        list_str = "".join(list_ctx_list)
        return True,"".join(['\n', cur_indent,"{\n" , list_str, "\n",cur_indent,"}"] )


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
            # 字符串要用单引号，因为Lua里单引号级别比双引号高
            return False,"".join(["'",value,"'"])
        elif tuple == val_type :
            return self.tuple_to_lua(value,indent)
        elif dict == val_type :
            return self.dict_to_lua(value,indent)
        elif list == val_type :
            return self.list_to_lua(value,indent)
        else :
            raise Exception( "invalid type",val_type )

    #文件内容
    def context(self,ctx):
        is_indent,str_ctx = self.to_text( ctx,1 )
        return "".join( [self.comment(), str_ctx, "\nreturn ", self.base_name] )


