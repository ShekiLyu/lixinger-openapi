# lixinger-openapi

## 简介
本Python包是[理杏仁开放平台](https://www.lixinger.com/open/api)WEB API的非官方Python封装，目的是方便Python量化分析者使用理杏仁开放平台数据。

## 功能
查询理杏仁开放平台数据，返回dataframe
### 接口列表
- lixinger.openapi.load\_token 加载token
- lixinger.openapi.stock\_fundamental\_info 公司基本面数据
- lixinger.openapi.stock\_fs\_info 公司财务数据
- lixinger.openapi.indice\_fundamental\_info 指数基本面数据

参数列表和理杏仁开放平台完全一致，详细参数介绍见理杏仁开放平台。

## 安装
> pip install git+http://github.com/ShekiLyu/lixinger-openapi.git

## 使用示例
> import lixinger.openapi as lo
>
> lo.load\_token("your\_token")
>
> df = lo.indice\_fundamental\_info(date='2018-05-21', stockCodes=['000300','000905'], metrics=['pe\_ttm', 'pb'])

返回结果：

                       date    pb.avg  pb.equalAvg  pb.median  pb.weightedAvg  \

  2018-05-20T16:00:00.000Z  2.887583     1.901159   2.194927        1.580795   

  2018-05-20T16:00:00.000Z  2.820360     2.093375   2.389658        2.322455   

   pb.y\_10.avg.chanceVal  pb.y\_10.avg.latestVal  pb.y\_10.avg.latestValPos  \

               2.518319               2.887583                  0.377056   

               2.789697               2.820360                  0.219984   

   pb.y\_10.avg.maxPositiveVal  pb.y\_10.avg.maxVal    ...      \

                    5.916331            5.916331    ...       

                    7.456632            7.456632    ...       

   pe\_ttm.y\_5.weightedAvg.chanceVal  pe\_ttm.y\_5.weightedAvg.latestVal  \

                          9.091297                         13.225688   

                         29.042320                         26.351689   

   pe\_ttm.y\_5.weightedAvg.latestValPos  pe\_ttm.y\_5.weightedAvg.maxPositiveVal  \

                             0.625616                              19.012193   

                             0.026273                              81.439281   

   pe\_ttm.y\_5.weightedAvg.maxVal  pe\_ttm.y\_5.weightedAvg.medianVal  \

                      19.012193                         12.731516   

                      81.439281                         34.676320   

   pe\_ttm.y\_5.weightedAvg.minVal  pe\_ttm.y\_5.weightedAvg.riskVal  stockCnName  \

                       8.011308                       14.071742        沪深300   

                      24.950110                       47.816678        中证500   

   stockCode  

     000300  

     000905 

