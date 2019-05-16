%% Automatic generation from -->>
%% excel file  name : A_array表示例--cfg_array
%% excel sheet name : 示例1-example1

-module(cfg_array_example1).

-include("cfg_array_example1.hrl").
-compile(export_all).

get(1001, "pos1", 88, 1) ->
    #cfg_array_example1{
    'id' = 1001
    ,'str' = "pos1"
    ,'level' = 88
    ,'sub_level' = 1
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 900]]
    ,'desc1' = "从小城镇"
    };

get(1001, "pos1", 88, 2) ->
    #cfg_array_example1{
    'id' = 1001
    ,'str' = "pos1"
    ,'level' = 88
    ,'sub_level' = 2
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 900]]
    ,'desc1' = "有钱就可以买"
    };

get(1001, "pos1", 89, 89) ->
    #cfg_array_example1{
    'id' = 1001
    ,'str' = "pos1"
    ,'level' = 89
    ,'sub_level' = 89
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 900]]
    ,'desc1' = "有钱就可以买"
    };

get(1001, "pos2", 88, 88.9) ->
    #cfg_array_example1{
    'id' = 1001
    ,'str' = "pos2"
    ,'level' = 88
    ,'sub_level' = 88.9
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 900]]
    ,'desc1' = "有钱就可以买"
    };

get(1001, "pos2", 89, 89) ->
    #cfg_array_example1{
    'id' = 1001
    ,'str' = "pos2"
    ,'level' = 89
    ,'sub_level' = 89
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 900]]
    ,'desc1' = "有钱就可以买"
    };

get(1002, "pos1", 88, 88) ->
    #cfg_array_example1{
    'id' = 1002
    ,'str' = "pos1"
    ,'level' = 88
    ,'sub_level' = 88
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 901]]
    ,'desc1' = "有钱就可以买"
    };

get(1002, "pos1", 89, 89) ->
    #cfg_array_example1{
    'id' = 1002
    ,'str' = "pos1"
    ,'level' = 89
    ,'sub_level' = 89
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 900]]
    ,'desc1' = "有钱就可以买"
    };

get(1002, "pos1", 90, 90) ->
    #cfg_array_example1{
    'id' = 1002
    ,'str' = "pos1"
    ,'level' = 90
    ,'sub_level' = 90
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 901]]
    ,'desc1' = "有钱就可以买"
    };

get(1002, "pos2", 88, 88) ->
    #cfg_array_example1{
    'id' = 1002
    ,'str' = "pos2"
    ,'level' = 88
    ,'sub_level' = 88
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 901]]
    ,'desc1' = "有钱就可以买"
    };

get(1002, "pos2", 89, 89) ->
    #cfg_array_example1{
    'id' = 1002
    ,'str' = "pos2"
    ,'level' = 89
    ,'sub_level' = 89
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 900]]
    ,'desc1' = "有钱就可以买"
    };

get(1002, "pos2", 90, 90) ->
    #cfg_array_example1{
    'id' = 1002
    ,'str' = "pos2"
    ,'level' = 90
    ,'sub_level' = 90
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 901]]
    ,'desc1' = "有钱就可以买"
    };

get(1003, "pos1", 85, 85) ->
    #cfg_array_example1{
    'id' = 1003
    ,'str' = "pos1"
    ,'level' = 85
    ,'sub_level' = 85
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 902]]
    ,'desc1' = "有钱就可以买"
    };

get(1004, "pos1", 80, 80) ->
    #cfg_array_example1{
    'id' = 1004
    ,'str' = "pos1"
    ,'level' = 80
    ,'sub_level' = 80
    ,'name' = "黑切+蓝盾"
    ,'attr' = [[1, 700], [2, 800], [3, 903]]
    ,'desc1' = "有钱就可以买"
    };

get(_, _, _, _) ->
    undefined.

get_all() ->
    [
    {1001, "pos1", 88, 1}
    ,{1001, "pos1", 88, 2}
    ,{1001, "pos1", 89, 89}
    ,{1001, "pos2", 88, 88.9}
    ,{1001, "pos2", 89, 89}
    ,{1002, "pos1", 88, 88}
    ,{1002, "pos1", 89, 89}
    ,{1002, "pos1", 90, 90}
    ,{1002, "pos2", 88, 88}
    ,{1002, "pos2", 89, 89}
    ,{1002, "pos2", 90, 90}
    ,{1003, "pos1", 85, 85}
    ,{1004, "pos1", 80, 80}
    ].

get_list() ->
    get_all().

get_list(1001) ->
    [
    {1001, "pos1", 88, 1}
    ,{1001, "pos1", 88, 2}
    ,{1001, "pos1", 89, 89}
    ,{1001, "pos2", 88, 88.9}
    ,{1001, "pos2", 89, 89}
    ];

get_list(1002) ->
    [
    {1002, "pos1", 88, 88}
    ,{1002, "pos1", 89, 89}
    ,{1002, "pos1", 90, 90}
    ,{1002, "pos2", 88, 88}
    ,{1002, "pos2", 89, 89}
    ,{1002, "pos2", 90, 90}
    ];

get_list(1003) ->
    [
    {1003, "pos1", 85, 85}
    ];

get_list(1004) ->
    [
    {1004, "pos1", 80, 80}
    ];

get_list(_) ->
    [].

get_list(1001, "pos1") ->
    [
    {1001, "pos1", 88, 1}
    ,{1001, "pos1", 88, 2}
    ,{1001, "pos1", 89, 89}
    ];

get_list(1001, "pos2") ->
    [
    {1001, "pos2", 88, 88.9}
    ,{1001, "pos2", 89, 89}
    ];

get_list(1002, "pos1") ->
    [
    {1002, "pos1", 88, 88}
    ,{1002, "pos1", 89, 89}
    ,{1002, "pos1", 90, 90}
    ];

get_list(1002, "pos2") ->
    [
    {1002, "pos2", 88, 88}
    ,{1002, "pos2", 89, 89}
    ,{1002, "pos2", 90, 90}
    ];

get_list(1003, "pos1") ->
    [
    {1003, "pos1", 85, 85}
    ];

get_list(1004, "pos1") ->
    [
    {1004, "pos1", 80, 80}
    ];

get_list(_, _) ->
    [].

get_list(1001, "pos1", 88) ->
    [
    {1001, "pos1", 88, 1}
    ,{1001, "pos1", 88, 2}
    ];

get_list(1001, "pos1", 89) ->
    [
    {1001, "pos1", 89, 89}
    ];

get_list(1001, "pos2", 88) ->
    [
    {1001, "pos2", 88, 88.9}
    ];

get_list(1001, "pos2", 89) ->
    [
    {1001, "pos2", 89, 89}
    ];

get_list(1002, "pos1", 88) ->
    [
    {1002, "pos1", 88, 88}
    ];

get_list(1002, "pos1", 89) ->
    [
    {1002, "pos1", 89, 89}
    ];

get_list(1002, "pos1", 90) ->
    [
    {1002, "pos1", 90, 90}
    ];

get_list(1002, "pos2", 88) ->
    [
    {1002, "pos2", 88, 88}
    ];

get_list(1002, "pos2", 89) ->
    [
    {1002, "pos2", 89, 89}
    ];

get_list(1002, "pos2", 90) ->
    [
    {1002, "pos2", 90, 90}
    ];

get_list(1003, "pos1", 85) ->
    [
    {1003, "pos1", 85, 85}
    ];

get_list(1004, "pos1", 80) ->
    [
    {1004, "pos1", 80, 80}
    ];

get_list(_, _, _) ->
    [].

