# py_exceltools
python3 基于openpyxl的excel转换工具。支持xlsx文件转换为erlang,elixir,lua,json,xml,python等配置文件。

关于openpyxl库：https://pypi.python.org/pypi/openpyxl。

## python和openpyxl安装
linux安装  
    apt-get install python-pip
    pip install openpyxl

win安装 

    安装python(同时安装pip并添加到Path)
    安装openpyxl, 在安装python后在cmd中运行: pip install openpyxl

# 使用
    lancher.bat(win)和lancher.sh(linux)为对应运行脚本。
    当前配置了用于参考的参数来转换example.xlsx，
    可在对应server、client输出文件夹查看生成配置效果。

    参数：
    --input   ：需要转换的excel文件所在目录
    --srv     : 服务端配置文件输出目录
    --clt     : 客户端配置文件输出目录
    --timeout : 需要转换的excel文件最后更新时间距当前时间秒数。-1转换所有
    --suffix  ：excel文件后缀，通常为.xlsx 
    --swriter : 服务端配置文件转换器，可以指定为: erlanghrl,erlangerl,elixir,lua,jsonarray,jsonobject,xml,python
    --cwriter : 客户端配置文件转换器，可以指定为: erlanghrl,erlangerl,elixir,lua,jsonarray,jsonobject,xml,python

    注：对于client和server，如果未配置输出目录或转换器，则不会导出。

# 数据类型
    支持int(int64), number(float), string, tuple, list, dict, json、lua
    其中tuple, list, dict 为 python原生数据结构 json 为json数据类型 Lua为 lua table
# 数据格式示范(可以参考本工具自带的示例配置表)
    int 整数 1,2,1000 64位
    number 整数或者小数都OK
    string 字符串 excel表中配置时不需要额外加双引号
    tuple  (元素, 元素， ...) 元素可以为 int number string tuple list dict
    list   [元素, 元素， ...] 元素可以为 int number string tuple list dict
    dict   [key：value, key：value， ...] key可以为 int number string tuple value可以为 int number string tuple list dict
        特别注意该类型的使用 因为在一些语言中 对应dict类似的类型的key不支持 int 比如 jsonarray和xml，如果在转成jsonarray和xml时key不能配置为int和number
    json   {key：value, key：value， ...}该类型为json的对象类型 Key为字符串， Value可以为任意Json数据类型即可以是对象，数字，基本数据类型。
    lua    该类型为lua的table类型  
    其中 list dict json 三种数据格式可以互相嵌套
    转换时会将这些数据类型转换为其他语言支持的数据类型，另外注意点是一些其他语言的一些限制 
    比如 json不能用数字做为对象的Key(), xml的也不能用数字作为标签， 在配置的时候需要注意
    而且导出xml和jsonjsonarray都是用的库，出错的时候不太好找到对应配置错误的数据，需要配置前
    就额外注意，以免不必要的懵逼和浪费时间，策划不太明白的可以请教程序或者百度

# 打包exe
部署时，可以将python打包成exe。建议使用pyinstaller。
pyinstaller3.2.1尚不支持python3.6.1，建议使用python 3.5。

    pip install pyinstaller
    pyinstaller -F -c ConfigConvertTool.py

excel文件名命名格式
    为了表名的可视化和可理解性，文件命名支持 MMM-NNN.xlsx的方式。MMM可以是任意字符(一般为文件中文名，但是不用下划线结尾)，
    作为文件名的注释性描述。NNN只能是数字,字母和下划线(不能以下划线开头和数字开头)，作为导出的配置以NNN做为表名前缀
excel sheet命名格式
    为了考虑策划会使用一个excel配置同一的功能的多个配置子表，且方便导出和查看，sheet命名为YYY-XXX或者 YYY+XXX， 
    或者YYY (里面不包含 "+"""-"),  YYY可以为任意字符(一般为中文描述),XXX为导出配置的表名后缀，
    当sheet命名为 YYY-XXX或者 YYY+XXX时 导出文件名为： NNN_XXX.lang(此种命名一般用于 一个excel配置多个需要导出的sheet页签)
    当sheet命名为 YYY 时 导出文件名为： NNN.lang （此种命名用法仅仅用于一个excel只配置一个需要导出的sheet页签）
    lang为目标语言的后缀名
 具体示例
    A_arrary表示例--cfg_array.xlsx 前缀Y可以用方便排序显示 更多具体参见配置excel示例
* 在string中无法直接使用换行等特殊称号。请用\n等转义字符替代。
* 由于xml并不存在数组等结构，不建议使用。
* 工具会检测server和client标识。如果不存在，则不导出些表。方便策划做备注
