## Automatic generation from -->>
## excel file  name: A_object表示例--cfg_object1
## excel sheet name: A_object表示例--cfg_object

defmodule Cfg_Object1_Cfg_Object do

    ## 开放等级
    def get(:open_level) do
        90
    end

    ## 额外添加属性值1
    def get(:add_value1) do
        100.1
    end

    ## 额外添加属性值2
    def get(:add_value2) do
        100
    end

    ## 活动id
    def get(:act_id) do
        1001
    end

    ## 开始时间
    def get(:open) do
        "fgfdg"
    end

    ## 错误信息
    def get(10000) do
        "前面字段为errorID,这里是错误描述，是的object配置的server,client字段名还支持数字作为key(但是转出格式为xml和jsonarray时就不支持了)"
    end

    ## 奖励1
    def get(:award1) do
        [[1001, 20], {1002, 20}, [1003, 30]]
    end

    ## 奖励2
    def get(:award2) do
        {{1001, 10}, [1002, 20]}
    end

    ## 奖励3(这条转成xml是就会报错,因为KEY为数字）
    def get(:award3) do
        %{1 => %{:res => 1001, :id => 10001, :count => 1}, 2 => %{:res => [1002, 1], :id => 10001, :count => 1}}
    end

    ## 奖励4
    def get(:award4) do
        %{:rr => [1001, 20], :ff => [3006, 99], :aa => [7003, 1], :test => "这就是一个测试"}
    end

    ## 奖励5
    def get(:award5) do
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    end

    ## 奖励
    def get(:award6) do
        [[1001, 20], [3006, 99], [7003, 1], %{:jsonobject => [12356, 654321]}]
    end

    def get(_) do
        :undefined
    end

end