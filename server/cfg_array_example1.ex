## Automatic generation from -->>
## excel file  name: A_array表示例--cfg_array
## excel sheet name: 示例1-example1

defmodule Cfg_Array_Example1 do

   defstruct [
    :id,                	## 唯一id
    :str,               	## 佩戴位置
    :level,             	## 等级
    :sub_level,         	## 等级
    :name,              	## 装备名字
    :attr,              	## 装备增加属性
    :desc1              	## 装备来源描述
    ]

    def get(1001, "pos1", 88, 1) do
        %Cfg_Array_Example1{
        :id => 1001,
        :str => "pos1",
        :level => 88,
        :sub_level => 1,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 900]],
        :desc1 => "从小城镇"
        }
    end

    def get(1001, "pos1", 88, 2) do
        %Cfg_Array_Example1{
        :id => 1001,
        :str => "pos1",
        :level => 88,
        :sub_level => 2,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 900]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1001, "pos1", 89, 89) do
        %Cfg_Array_Example1{
        :id => 1001,
        :str => "pos1",
        :level => 89,
        :sub_level => 89,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 900]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1001, "pos2", 88, 88.9) do
        %Cfg_Array_Example1{
        :id => 1001,
        :str => "pos2",
        :level => 88,
        :sub_level => 88.9,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 900]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1001, "pos2", 89, 89) do
        %Cfg_Array_Example1{
        :id => 1001,
        :str => "pos2",
        :level => 89,
        :sub_level => 89,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 900]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1002, "pos1", 88, 88) do
        %Cfg_Array_Example1{
        :id => 1002,
        :str => "pos1",
        :level => 88,
        :sub_level => 88,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 901]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1002, "pos1", 89, 89) do
        %Cfg_Array_Example1{
        :id => 1002,
        :str => "pos1",
        :level => 89,
        :sub_level => 89,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 900]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1002, "pos1", 90, 90) do
        %Cfg_Array_Example1{
        :id => 1002,
        :str => "pos1",
        :level => 90,
        :sub_level => 90,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 901]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1002, "pos2", 88, 88) do
        %Cfg_Array_Example1{
        :id => 1002,
        :str => "pos2",
        :level => 88,
        :sub_level => 88,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 901]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1002, "pos2", 89, 89) do
        %Cfg_Array_Example1{
        :id => 1002,
        :str => "pos2",
        :level => 89,
        :sub_level => 89,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 900]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1002, "pos2", 90, 90) do
        %Cfg_Array_Example1{
        :id => 1002,
        :str => "pos2",
        :level => 90,
        :sub_level => 90,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 901]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1003, "pos1", 85, 85) do
        %Cfg_Array_Example1{
        :id => 1003,
        :str => "pos1",
        :level => 85,
        :sub_level => 85,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 902]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(1004, "pos1", 80, 80) do
        %Cfg_Array_Example1{
        :id => 1004,
        :str => "pos1",
        :level => 80,
        :sub_level => 80,
        :name => "黑切+蓝盾",
        :attr => [[1, 700], [2, 800], [3, 903]],
        :desc1 => "有钱就可以买"
        }
    end

    def get(_, _, _, _) do
        :undefined
    end

    def get_all() do
        [
        {1001, "pos1", 88, 1},
        {1001, "pos1", 88, 2},
        {1001, "pos1", 89, 89},
        {1001, "pos2", 88, 88.9},
        {1001, "pos2", 89, 89},
        {1002, "pos1", 88, 88},
        {1002, "pos1", 89, 89},
        {1002, "pos1", 90, 90},
        {1002, "pos2", 88, 88},
        {1002, "pos2", 89, 89},
        {1002, "pos2", 90, 90},
        {1003, "pos1", 85, 85},
        {1004, "pos1", 80, 80}
        ]
    end

    def get_list() do
        get_all()
    end

    def get_list(1001) do
        [
        {1001, "pos1", 88, 1},
        {1001, "pos1", 88, 2},
        {1001, "pos1", 89, 89},
        {1001, "pos2", 88, 88.9},
        {1001, "pos2", 89, 89}
        ]
    end

    def get_list(1002) do
        [
        {1002, "pos1", 88, 88},
        {1002, "pos1", 89, 89},
        {1002, "pos1", 90, 90},
        {1002, "pos2", 88, 88},
        {1002, "pos2", 89, 89},
        {1002, "pos2", 90, 90}
        ]
    end

    def get_list(1003) do
        [
        {1003, "pos1", 85, 85}
        ]
    end

    def get_list(1004) do
        [
        {1004, "pos1", 80, 80}
        ]
    end

    def get_list(_) do
        []
    end

    def get_list(1001, "pos1") do
        [
        {1001, "pos1", 88, 1},
        {1001, "pos1", 88, 2},
        {1001, "pos1", 89, 89}
        ]
    end

    def get_list(1001, "pos2") do
        [
        {1001, "pos2", 88, 88.9},
        {1001, "pos2", 89, 89}
        ]
    end

    def get_list(1002, "pos1") do
        [
        {1002, "pos1", 88, 88},
        {1002, "pos1", 89, 89},
        {1002, "pos1", 90, 90}
        ]
    end

    def get_list(1002, "pos2") do
        [
        {1002, "pos2", 88, 88},
        {1002, "pos2", 89, 89},
        {1002, "pos2", 90, 90}
        ]
    end

    def get_list(1003, "pos1") do
        [
        {1003, "pos1", 85, 85}
        ]
    end

    def get_list(1004, "pos1") do
        [
        {1004, "pos1", 80, 80}
        ]
    end

    def get_list(_, _) do
        []
    end

    def get_list(1001, "pos1", 88) do
        [
        {1001, "pos1", 88, 1},
        {1001, "pos1", 88, 2}
        ]
    end

    def get_list(1001, "pos1", 89) do
        [
        {1001, "pos1", 89, 89}
        ]
    end

    def get_list(1001, "pos2", 88) do
        [
        {1001, "pos2", 88, 88.9}
        ]
    end

    def get_list(1001, "pos2", 89) do
        [
        {1001, "pos2", 89, 89}
        ]
    end

    def get_list(1002, "pos1", 88) do
        [
        {1002, "pos1", 88, 88}
        ]
    end

    def get_list(1002, "pos1", 89) do
        [
        {1002, "pos1", 89, 89}
        ]
    end

    def get_list(1002, "pos1", 90) do
        [
        {1002, "pos1", 90, 90}
        ]
    end

    def get_list(1002, "pos2", 88) do
        [
        {1002, "pos2", 88, 88}
        ]
    end

    def get_list(1002, "pos2", 89) do
        [
        {1002, "pos2", 89, 89}
        ]
    end

    def get_list(1002, "pos2", 90) do
        [
        {1002, "pos2", 90, 90}
        ]
    end

    def get_list(1003, "pos1", 85) do
        [
        {1003, "pos1", 85, 85}
        ]
    end

    def get_list(1004, "pos1", 80) do
        [
        {1004, "pos1", 80, 80}
        ]
    end

    def get_list(_, _, _) do
        []
    end

end