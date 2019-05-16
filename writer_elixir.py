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

class ElixirWriter(Writer):
    # 文件后缀
    def suffix(self):
        return ".ex"

    def comment(self):
        comment = [
            '## Automatic generation from -->>'
            '\n## excel file  name: ' + self.doc_name +
            '\n## excel sheet name: ' + self.sheet_name,
            '\ndefmodule ' + self.base_name.title() + ' do\n\n'
        ]

        return "\n".join( comment )

    # 获取缩进字符串
    def indent_ctx( self,indent ):
        if indent <= 0: return ""

        if indent not in INDENT_LIST:
            INDENT_LIST[indent] = ""
        else:
            ctx = BASE_INDENT*indent
            INDENT_LIST[indent] = ctx

        return INDENT_LIST[indent]

    def dict_to_text(self, value, indent) :
        dict_text_list = []
        for k in ( value ) :
            k_indent,lk = self.to_target_lang( k,indent )
            is_indent,lv = self.to_target_lang( value[k],indent + 1 )

            comment = self.comment_text[k]

            val_type = type( lk )
            if str == val_type :
                if lk.replace(".", "").isdigit() :
                    lk.replace("\"", "")
                else :
                    lk = ':' + lk.replace("\"", "")

            key = "".join( ["    def get(",lk,") do\n"] )

            val = "".join( ["    ## ", comment, "\n", key, "        ", lv, "\n    end\n\n"] )

            dict_text_list.append( val )

        dict_str = "".join( dict_text_list )
        dict_str = dict_str + "    def get(_) do\n        :undefined\n    end\n\nend"
        return False, dict_str

    def list_to_text(self, value, indent):
        list_text_list = []
        # 先定义 struct
        struct_text_list = []
        struct_len = len(self.comment_text)
        tem_count = 0
        for k in self.comment_text :
            tem_count += 1
            comment = self.comment_text[k]
            k_indent,lk = self.to_target_lang( k,indent )
            val_type = type( lk )
            if str == val_type :
                if lk.replace(".", "").isdigit() :
                    lk.replace("\"", "")
                else :
                    lk = ':' + lk.replace("\"", "")

                if tem_count != struct_len :
                    lk = lk + ','
                else :
                    lk = lk

            if None == comment :
                comment = ""
            val = "".join( [lk.ljust(20, " "), "\t## ", comment, "\n"] )

            struct_text_list.append( val )

        struct_str = "    ".join( struct_text_list )
        end_str = "   defstruct [\n    " + struct_str + "    ]\n\n"

        list_text_list.append(end_str)

        all_key_list = []
        # 生成 get() 函数
        for i, onedict in enumerate( value ) :
            # 生成对应的 key
            key_list = []
            for k in ( onedict ) :
                if None != self.keys_list.get(k, None) :
                    is_indent,lv = self.to_target_lang( onedict[k],indent + 1 )
                    key_list.append(lv)
            all_key_list.append(key_list)

            tem = ", ".join( key_list )

            key = "".join( ["    def get(",tem,") do\n        %", self.base_name.title(), "{\n        "] )

            # 生成对应的value
            value_list = []
            onedict_len = len(onedict)
            tem_count = 0
            for k in ( onedict ) :
                tem_count += 1
                k_indent,lk = self.to_target_lang( k,indent )
                is_indent,lv = self.to_target_lang( onedict[k],indent + 1 )

                val_type = type( lk )
                if str == val_type :
                    if lk.replace(".", "").isdigit() :
                        lk.replace("\"", "")
                    else :
                        lk = ':' + lk.replace("\"", "")

                if tem_count != onedict_len :
                    oneval = "".join( [lk, " => ", lv , ",\n"] )
                    value_list.append( oneval )
                else :
                    oneval = "".join( [lk, " => ", lv , "\n"] )
                    value_list.append( oneval )

            value_list_str = "        ".join(value_list)
            end_str = "".join( [key, value_list_str, "        }\n    end\n\n"] )

            list_text_list.append( end_str )

        underline_list = []
        for i in self.keys_list :
            underline_list.append('_')

        end_str = ", ".join(underline_list)
        no_match_str = "    def get(" + end_str + ") do\n        :undefined\n    end\n\n"

        list_text_list.append(no_match_str)

        # 生成 get_all() 函数
        get_all_fun = []
        allkey_len = len(all_key_list)
        tem_count = 0
        for i, ival in enumerate(all_key_list) :
            tem_count += 1
            if tem_count != allkey_len :
                oneval = '{' + ", ".join(ival) + '},\n'
                get_all_fun.append(oneval)
            else :
                oneval = '{' + ", ".join(ival) + '}\n'
                get_all_fun.append(oneval)

        value_list_str = "        ".join(get_all_fun)
        start_str = '    def get_all() do\n        [\n        '
        end_str = "".join( [start_str, value_list_str, "        ]\n    end\n\n"] )

        list_text_list.append( end_str )

        # 生成 get_list() 函数
        get_list_fun = []
        keys_len = len(self.keys_list)
        for key in self.keys_list :
            keyindex = self.keys_list[key]
            if keyindex == 1 :
                list_text_list.append( '    def get_list() do\n        get_all()\n    end\n\n')
            elif keyindex <= keys_len :
                get_tem_dict = {}
                underline_list = []
                for i, ival in enumerate(all_key_list) :
                    key_tem_list = []
                    j = 0
                    underline_list = []
                    while j < keyindex - 1 :
                        key_tem_list.append(ival[j])
                        underline_list.append('_')
                        j += 1

                    keystr = '(' + ", ".join(key_tem_list) + ')'
                    if None != get_tem_dict.get(keystr, None) :
                        oldlist = get_tem_dict[keystr]
                        oldlist.append(ival)
                        get_tem_dict[keystr] = oldlist
                    else :
                        get_tem_dict[keystr] = [ival]

                for onekey in get_tem_dict :
                    value_tem_list = []
                    valuelist = get_tem_dict[onekey]

                    value_len = len(valuelist)
                    tem_count = 0
                    for l, lval in enumerate(valuelist) :
                        tem_count += 1
                        if tem_count != value_len :
                            oneval = '{' + ", ".join(lval) + '},\n'
                            value_tem_list.append(oneval)
                        else :
                            oneval = '{' + ", ".join(lval) + '}\n'
                            value_tem_list.append(oneval)
                    start_str = '    def get_list' + onekey + ' do\n        [\n        '
                    end_str = "".join( [start_str, "        ".join(value_tem_list), "        ]\n    end\n\n"] )
                    get_list_fun.append(end_str)
                no_match_str = "".join('    def get_list(' + ", ".join(underline_list) + ') do\n        []\n    end\n\n')
                get_list_fun.append(no_match_str)


        value_list_str = "".join(get_list_fun) + 'end'
        list_text_list.append( value_list_str )
        dict_str = "".join( list_text_list )

        return False, dict_str

    # 转换为文本数据 之前解析出来的excel数据存放方式存在LIST(array格式)和DICT(object格式)两种类型
    def to_text(self,value,indent):
        val_type = type( value )
        if dict == val_type :
           return self.dict_to_text(value, indent)
        else :
           return self.list_to_text(value, indent)

    # python的dict转换为elixir的map类型
    def dict_to_elixir(self,value,indent):
        dict_ctx_list = []

        for k in ( value ) :
            k_indent,lk = self.to_target_lang( k,indent )
            is_indent,lv = self.to_target_lang( value[k],indent + 1 )

            val_type = type( lk )
            if str == val_type :
                if lk.replace(".", "").isdigit() :
                    lk.replace("\"", "")
                else :
                    lk = ':' + lk.replace("\"", "")

            key = "".join( [lk," => "] )
            val = "".join( [key, lv] )
            dict_ctx_list.append(val)

        dict_str = ", ".join( dict_ctx_list )
        return False,"".join( ["%{",dict_str,"}"] )

    # python的list转换为elixir的list类型
    def list_to_elixir(self,value,indent):
        list_ctx_list = []
        for v in value :
            is_indent,lv = self.to_target_lang( v,indent + 1 )
            list_ctx_list.append( lv )


        list_str = ", ".join( list_ctx_list )
        return False,"".join( ["[",list_str,"]"] )

    # python的tuple转换为elixir的tuple类型
    def tuple_to_elixir(self,value,indent):
        tuple_ctx_list = []

        for v in value :
            is_indent,lv = self.to_target_lang( v,indent + 1 )
            tuple_ctx_list.append( lv )

        # 返回 {a,b,c}这种不换行的格式
        list_str = ", ".join( tuple_ctx_list )
        return False,"".join( ["{",list_str,"}"] )


    # 变量转换到目标语言字符串
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
            return self.tuple_to_elixir(value,indent)
        elif dict == val_type :
            return self.dict_to_elixir(value,indent)
        elif list == val_type :
            return self.list_to_elixir(value,indent)
        else :
            raise Exception( "invalid type",val_type )

    #文件内容
    def context(self,ctx):
        is_indent,str_ctx = self.to_text( ctx,0 )
        return "".join( [self.comment(),"",str_ctx] )
