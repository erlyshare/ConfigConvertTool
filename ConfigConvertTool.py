#! python
# -*- coding:utf-8 -*-

import os
import time
from writer import *
from writer_erlang_erl import *
from writer_erlang_hrl import *
from writer_elixir import *
from writer_lua import *
from writer_xml import *
from writer_json_object import *
from writer_json_array import *
from writer_python import *
from optparse import OptionParser

from decoder import ExcelDoc

class Reader:
    # @input_path:excel文件所在目录
    # @srv_path  :server输出目录
    # @clt_path  :客户端输出目录
    # @timeout   :只处理文档最后更改时间在N秒内的文档
    # @suffix    :excel文件后缀
    def __init__(self,input_path,
        srv_path,clt_path,timeout,suffix,srv_writer,clt_writer):
        self.input_path = input_path
        self.srv_path   = srv_path
        self.clt_path   = clt_path
        self.timeout    = timeout
        self.suffix     = suffix

        self.srv_writer = None
        self.clt_writer = None

        if None != srv_writer :
            self.srv_writer = eval( srv_writer.capitalize() + "Writer" )
        if None != clt_writer :
            self.clt_writer = eval( clt_writer.capitalize() + "Writer" )

    def attention(self):
        print("*****************************开始导表*****************************\n")

    def can_read(self,file,abspath):
        if not os.path.isfile( abspath ): return False
        # ~开头的excel文件是临时文件，linux下wps临时文件以.~开头
        if file.startswith( "~" ) \
            or file.startswith( "." ) or file.startswith( "$" ): return False
        if "" != self.suffix and not file.endswith( self.suffix ): return False

        if self.timeout > 0:
            now = time.time()
            mtime = os.path.getmtime( abspath )

            if now - mtime > self.timeout: return False

        return True

    def read(self):
        if self.timeout > 0 :
            print("read %s files from %s modified \
                within %d seconds" % (self.suffix,self.input_path,self.timeout))
        else :
            print("read %s files from %s" % (self.suffix,self.input_path))

        if None != self.srv_path and not os.path.exists( self.srv_path ) :
            os.makedirs( self.srv_path )
        if None != self.clt_path and not os.path.exists( self.clt_path ) :
            os.makedirs( self.clt_path )

        now = time.time()
        file_list = os.listdir( options.input_path )
        for file in file_list:
            abspath = os.path.join( self.input_path,file )
            if self.can_read( file,abspath ) :
                self.read_one( file,abspath )

        print( "done,%d seconds elapsed" % ( time.time() - now ) )

    def read_one(self,file,abspath):
        doc = ExcelDoc( file,abspath )
        doc.decode( self.srv_path,
            self.clt_path,self.srv_writer,self.clt_writer )

if __name__ == '__main__':

    parser = OptionParser()

    parser.add_option( "-i", "--input", dest="input_path",
                     default="xls/",
                     help="read all files from this path" )
    parser.add_option( "-s", "--srv", dest="srv_path",
                     help="write all server file to this path" )
    parser.add_option( "-c", "--clt", dest="clt_path",
                     help="write all client file to this path" )
    parser.add_option( "-t", "--timeout", dest="timeout",type="int",
                     default="-1",
                     help="only converte files modified within seconds" )
    parser.add_option( "-f", "--suffix", dest="suffix",
                     default="",
                     help="what type of file will be readed.empty mean all files" )
    parser.add_option( "-w","--swriter", dest="srv_writer",
                     help="which server writer you wish to use:lua xml json" )
    parser.add_option( "-l","--cwriter", dest="clt_writer",
                     help="which client writer you wish to use:lua xml json" )

    options, args = parser.parse_args()

    reader = Reader( options.input_path,options.srv_path,options.clt_path,
        options.timeout,options.suffix,options.srv_writer,options.clt_writer )
    reader.attention()
    reader.read()