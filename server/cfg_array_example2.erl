%% Automatic generation from -->>
%% excel file  name : A_array表示例--cfg_array
%% excel sheet name : 示例2+example2

-module(cfg_array_example2).

-include("cfg_array_example2.hrl").
-compile(export_all).

get(1) ->
    #cfg_array_example2{
    'id' = 1
    ,'name' = "examp1001"
    ,'material' = [#{'res' => 1, 'id' => 10001, 'count' => 1}, #{'res' => 1, 'id' => 10001, 'count' => 1}]
    ,'attr' = [[1, 700], [2, 800], [3, 900], #{'add' => [4, 100]}]
    ,'award1' = {1, 2, 3}
    ,'award2' = #{'id' => 1, 'type' => 2, 'num' => 3}
    };

get(2) ->
    #cfg_array_example2{
    'id' = 2
    ,'name' = "examp1002"
    ,'material' = #{'res' => 1, 'id' => 10001, 'count' => 1}
    ,'attr' = [[1, 700], [2, 800], [3, 901], #{'add' => [5, 100]}]
    ,'award1' = {1, 2, 3}
    ,'award2' = #{'id' => 1, 'type' => 2, 'num' => 3}
    };

get(3) ->
    #cfg_array_example2{
    'id' = 3
    ,'name' = "examp1003"
    ,'material' = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    ,'attr' = [[1, 700], [2, 800], [3, 902], #{'add' => [6, 100]}]
    ,'award1' = {1, 2, 3}
    ,'award2' = #{'id' => 1, 'type' => 2, 'num' => 3}
    };

get(4) ->
    #cfg_array_example2{
    'id' = 4
    ,'name' = "examp1004"
    ,'material' = ["测试数据", "测试数据2", "测试数据3"]
    ,'attr' = [[1, 700], [2, 800], [3, 903], #{'add' => [7, 100]}]
    ,'award1' = {1, 2, 3}
    ,'award2' = #{'id' => 1, 'type' => 2, 'num' => 3}
    };

get(5) ->
    #cfg_array_example2{
    'id' = 5
    ,'name' = "examp1004"
    ,'material' = ["test"]
    ,'attr' = [[1, 700], [2, 800], [3, 903], #{'add' => [7, 100]}]
    ,'award1' = {1, 2, 3}
    ,'award2' = #{'id' => 1, 'type' => 2, 'num' => 3}
    };

get(_) ->
    undefined.

get_all() ->
    [
    {1}
    ,{2}
    ,{3}
    ,{4}
    ,{5}
    ].

get_list() ->
    get_all().

