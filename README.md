# lixinger-openapi

## 简介
本Python包是[理杏仁开放平台](https://www.lixinger.com/open/api)WEB API的非官方Python封装，目的是方便Python量化分析者使用理杏仁开放平台数据。

## 功能
查询理杏仁开放平台数据，返回json或dataframe

### 接口列表
- lixinger\_openapi.load\_token 加载token
- lixinger\_openapi.json.stock\_fundamental\_info 公司基本面数据(json格式)
- lixinger\_openapi.json.stock\_fs\_info 公司财务数据(json格式)
- lixinger\_openapi.json.indice\_fundamental\_info 指数基本面数据(json格式)
- lixinger\_openapi.data.stock\_fundamental\_info 公司基本面数据(dataframe格式)
- lixinger\_openapi.data.stock\_fs\_info 公司财务数据(dataframe格式)
- lixinger\_openapi.data.indice\_fundamental\_info 指数基本面数据(dataframe格式)

参数列表和理杏仁开放平台完全一致，详细参数介绍见理杏仁开放平台。

## 安装
> pip install git+http://github.com/ShekiLyu/lixinger-openapi.git

## 使用示例
> import lixinger\_openapi as lo
>
> lo.load\_token("your\_token")
>
> json\_rlt = lo.json.indice\_fundamental\_info(date='2018-05-21', stockCodes=['000300','000905'], metrics=['pe\_ttm', 'pb'])

json格式返回结果为Python数组，结构与网站返回的json相同:

[{'date': '2018-05-20T16:00:00.000Z', 'pe\_ttm': {'weightedAvg': 13.22568765724127, 'median': 24.726652058696498, 'equalAvg': 18.250245261066897, 'avg': 28.26107455983107, 'y\_10': {'weightedAvg': {'latestVal': 13.22568765724127, 'latestValPos': 0.5004111842105263, 'minVal': 8.011307841787573,......

> df = lo.data.indice\_fundamental\_info(date='2018-05-21', stockCodes=['000300','000905'], metrics=['pe\_ttm', 'pb'])

dataframe格式返回结果的表头:

Index(['date', 'pb.avg', 'pb.equalAvg', 'pb.median', 'pb.weightedAvg',
       'pb.y_10.avg.chanceVal', 'pb.y_10.avg.latestVal',
       'pb.y_10.avg.latestValPos', 'pb.y_10.avg.maxPositiveVal',
       'pb.y_10.avg.maxVal',
       ...
       'pe_ttm.y_5.weightedAvg.chanceVal', 'pe_ttm.y_5.weightedAvg.latestVal',
       'pe_ttm.y_5.weightedAvg.latestValPos',
       'pe_ttm.y_5.weightedAvg.maxPositiveVal',
       'pe_ttm.y_5.weightedAvg.maxVal', 'pe_ttm.y_5.weightedAvg.medianVal',
       'pe_ttm.y_5.weightedAvg.minVal', 'pe_ttm.y_5.weightedAvg.riskVal',
       'stockCnName', 'stockCode'],
      dtype='object', length=139)

结果里包含139列数据，分别对应理杏仁返回的json数据进行扁平化处理后的结果，嵌套的数据用key1.key11.key111的方式作为列名。
