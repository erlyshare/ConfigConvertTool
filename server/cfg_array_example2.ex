## Automatic generation from -->>
## excel file  name: A_array表示例--cfg_array
## excel sheet name: 示例2+example2

defmodule Cfg_Array_Example2 do

   defstruct [
    :id,                	## 英雄id
    :name,              	## 英雄名字
    :material,          	## 合成消耗
    :attr,              	## 属性
    :award1,            	## 奖励1
    :award2             	## 奖励2
    ]

    def get(1) do
        %Cfg_Array_Example2{
        :id => 1,
        :name => "examp1001",
        :material => [%{:res => 1, :id => 10001, :count => 1}, %{:res => 1, :id => 10001, :count => 1}],
        :attr => [[1, 700], [2, 800], [3, 900], %{:add => [4, 100]}],
        :award1 => {1, 2, 3},
        :award2 => %{:id => 1, :type => 2, :num => 3}
        }
    end

    def get(2) do
        %Cfg_Array_Example2{
        :id => 2,
        :name => "examp1002",
        :material => %{:res => 1, :id => 10001, :count => 1},
        :attr => [[1, 700], [2, 800], [3, 901], %{:add => [5, 100]}],
        :award1 => {1, 2, 3},
        :award2 => %{:id => 1, :type => 2, :num => 3}
        }
    end

    def get(3) do
        %Cfg_Array_Example2{
        :id => 3,
        :name => "examp1003",
        :material => [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        :attr => [[1, 700], [2, 800], [3, 902], %{:add => [6, 100]}],
        :award1 => {1, 2, 3},
        :award2 => %{:id => 1, :type => 2, :num => 3}
        }
    end

    def get(4) do
        %Cfg_Array_Example2{
        :id => 4,
        :name => "examp1004",
        :material => ["测试数据", "测试数据2", "测试数据3"],
        :attr => [[1, 700], [2, 800], [3, 903], %{:add => [7, 100]}],
        :award1 => {1, 2, 3},
        :award2 => %{:id => 1, :type => 2, :num => 3}
        }
    end

    def get(5) do
        %Cfg_Array_Example2{
        :id => 5,
        :name => "examp1004",
        :material => ["test"],
        :attr => [[1, 700], [2, 800], [3, 903], %{:add => [7, 100]}],
        :award1 => {1, 2, 3},
        :award2 => %{:id => 1, :type => 2, :num => 3}
        }
    end

    def get(_) do
        :undefined
    end

    def get_all() do
        [
        {1},
        {2},
        {3},
        {4},
        {5}
        ]
    end

    def get_list() do
        get_all()
    end

end