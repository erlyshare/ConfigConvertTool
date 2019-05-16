%% Automatic generation from -->>
%% excel file  name : A_object表示例--cfg_object
%% excel sheet name : 武器(这个sheet就不会附加到导出名后部分)

-module(cfg_object).

-compile(export_all).

%% 开放等级
get('open_level') ->
    90;

%% 额外添加属性值1
get('add_value1') ->
    100.1;

%% 额外添加属性值2
get('add_value2') ->
    100;

%% 活动id
get('act_id') ->
    1001;

%% 开始时间
get('open') ->
    "18:00:0";

%% 错误信息
get(10000) ->
    "前面字段为errorID,这里是错误描述，是的object配置的server,client字段名还支持数字作为key(但是转出格式为xml和jsonarray时就不支持了)";

%% 奖励1
get('award1') ->
    [[1001, 20], {1002, 20}, [1003, 30]];

%% 奖励2
get('award2') ->
    {{1001, 10}, [1002, 20]};

%% 奖励3(这条转成xml是就会报错）
get('award3') ->
    #{1 => #{'res' => 1001, 'id' => 10001, 'count' => 1}, 2 => #{'res' => [1002, 1], 'id' => 10001, 'count' => 1}};

%% 奖励4
get('award4') ->
    #{'rr' => [1001, 20], 'ff' => [3006, 99], 'aa' => [7003, 1], 'test' => "这就是一个测试"};

%% 奖励5
get('award5') ->
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9];

%% 奖励
get('award6') ->
    [[1001, 20], [3006, 99], [7003, 1], #{'jsonobject' => [12356, 654321]}];

get(_) ->
    undefined.