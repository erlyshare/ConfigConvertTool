#! python
# -*- coding:utf-8 -*-

import os
import sys
from xml.dom.minidom import Document
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

class JsonWriter(Writer):
    # 文件后缀
    def suffix(self):
        return ".json"

    # 文件内容(字符串)
    def context(self,ctx):
        return json.dumps(ctx,ensure_ascii=False,\
            indent=4,sort_keys=True,separators=(',', ':') )


class XmlWriter(Writer):
    # 文件后缀
    def suffix(self):
        return ".xml"
    # 注释开始
    def comment_start(self):
        return "<!--"
    # 注释结束
    def comment_end(self):
        return "-->"

    #创建根元素
    def root_element(self):
        root = self.doc.createElement( self.base_name )
        return root

    # dict类型转换为xml
    def dict_to_xml(self,root,value):
        # 需要对key排序，不然每次导出的xml字段是乱的，对版本管理不友好
        for k in sorted( value ) :
            v = value[k]
            sub_root = self.doc.createElement( k )

            self.to_xml( sub_root,v )
            root.appendChild( sub_root )

    # list类型转换为xml
    def list_to_xml(self,root,value):
        for k,v in enumerate( value ) :
            # xml中并不支持array，用item来命名，外加一个index属性
            sub_root = self.doc.createElement( "item" )
            sub_root.setAttribute( "index",str( k ) )

            self.to_xml( sub_root,v )
            root.appendChild( sub_root )
    # tuple类型转换为xml
    def tuple_to_xml(self,root,value):
        valueList = list(value)
        for k,v in enumerate( valueList ) :
            # xml中并不支持array，用item来命名，外加一个index属性
            sub_root = self.doc.createElement( "item" )
            sub_root.setAttribute( "index",str( k ) )

            self.to_xml( sub_root,v )
            root.appendChild( sub_root )

    # 转换为xml节点
    def to_xml(self,root,value):
        sub_node = None
        val_type_str = None
        val_type = type( value )
        if int == val_type :
            # python3中没有Long类型，int64也用int表示
            val_type_str = "int64"
            sub_node = self.doc.createTextNode( str( value ) )
        elif long == val_type :
            val_type_str = "int64"
            sub_node = self.doc.createTextNode( str( value ) )
        elif float == val_type :
            val_type_str = "number"
            # 去除带小数时的小数点，100.0 ==>> 100
            if long( value ) == float( value ) :
                sub_node = self.doc.createTextNode( str( long( value ) ) )
            else:
                sub_node = self.doc.createTextNode( str( value ) )
        elif str == val_type or unicode == val_type :
            val_type_str = "string"
            sub_node = self.doc.createTextNode( value )
        elif tuple == val_type :
            self.tuple_to_xml( root,value )
        elif dict == val_type :
            self.dict_to_xml( root,value )
        elif list == val_type :
            self.list_to_xml( root,value )
        else :
            raise Exception( "invalid type",val_type )

        # 类型为dict或者list的，没有这个type属性
        if val_type_str : root.setAttribute( "type",val_type_str )
        if sub_node : root.appendChild( sub_node )

    # 文件内容
    def context(self,ctx):
        #创建DOM文档对象
        self.doc = Document()
        root = self.root_element()

        self.to_xml( root,ctx )
        self.doc.appendChild( root )

        return self.comment() + self.doc.toprettyxml( indent="   " )


