@echo off

:python ConfigConvertTool.py --input ./config_excel --srv server/ --clt client/ --timeout -1 --suffix .xlsx --swriter lua --cwriter lua
:python ConfigConvertTool.py --input ./config_excel --srv server/ --clt client/ --timeout -1 --suffix .xlsx --swriter erlanghrl
:python ConfigConvertTool.py --input ./config_excel --srv server/ --clt client/ --timeout -1 --suffix .xlsx --swriter erlangerl
:python ConfigConvertTool.py --input ./config_excel --srv server/ --clt client/ --timeout -1 --suffix .xlsx --swriter elixir
:python ConfigConvertTool.py --input ./config_excel --srv server/ --clt client/ --timeout -1 --suffix .xlsx --swriter jsonobject
:python ConfigConvertTool.py --input ./config_excel --srv server/ --clt client/ --timeout -1 --suffix .xlsx --cwriter jsonarray
python ConfigConvertTool.py --input ./config_excel --srv server/ --clt client/ --timeout -1 --suffix .xlsx --swriter elixir --cwriter xml


pause
