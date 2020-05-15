# 用户使用指南

## 安装
### 从PyPI安装
`pip install lixinger-openapi`

### 从Github安装
`pip install git+http://github.com/ShekiLyu/lixinger-openapi.git`

### 从PyPI更新
`pip install --upgrade lixinger-openapi`

### 从Github更新
`pip install --upgrade git+http://github.com/ShekiLyu/lixinger-openapi.git`

## 接口列表
接口名               | 接口功能
------------------- | -------------------------
set\_token          | 设置token
query\_json         | 查询数据(json格式)
query\_dataframe    | 查询数据(dataframe格式)


## 使用方法

### 引入包


```python
import lixinger_openapi as lo
```

### 加载token


```python
lo.set_token("your_token")
```

set_token会目录下生成token.cfg文件保存token，所以在当前目录只需加载一次。如果不想写token.cfg文件，可以如下设置：


```python
lo.set_token("your_token", write_token=False)
```

### 查询（使用理杏仁开放平台上的示例）
#### A股公司基本面数据
##### json格式


```python
json_rlt = lo.query_json('a.stock.fundamental.non_financial', 
    {
        "date": "2018-01-19",
        "stockCodes": [
            "000028",
            "600511"
        ],
        "metricsList": [
            "pe_ttm",
            "mc"
        ]
    })
print(json_rlt)
```

    {'data': [{'date': '2018-01-19T00:00:00+08:00', 'pe_ttm': 21.046568599508507, 'stockCode': '000028', 'mc': 26663748314.4}, {'date': '2018-01-19T00:00:00+08:00', 'pe_ttm': 21.459988206744743, 'stockCode': '600511', 'mc': 20346751061}], 'code': 0, 'msg': 'success'}
    

##### dataframe格式


```python
dataframe_rlt = lo.query_dataframe('a.stock.fundamental.non_financial', 
    {
        "date": "2018-01-19",
        "metricsList": ["pe_ttm", "mc"],
        "stockCodes": ["000028", "600511"]
    })
print('code: '+ str(dataframe_rlt['code']))
print('\ndata:')
print(dataframe_rlt['data'])
print('\nmsg: ' + dataframe_rlt['msg'])
```

    code: 0
    
    data:
                            date            mc     pe_ttm stockCode
    0  2018-01-19T00:00:00+08:00  2.666375e+10  21.046569    000028
    1  2018-01-19T00:00:00+08:00  2.034675e+10  21.459988    600511
    
    msg: success
    

#### A股指数基本信息
##### json格式


```python
json_rlt = lo.query_json('a.index', {
    "stockCodes": [
        "000016"
    ]
})
print(json_rlt)
```

    {'data': [{'source': 'sh', 'cnName': '上证50', 'publishDate': '2004-01-01T16:00:00.000Z', 'stockCode': '000016', 'areaCode': 'cn', 'market': 'a'}], 'code': 0, 'msg': 'success'}
    

##### dataframe格式


```python
dataframe_rlt = lo.query_dataframe('a.index', {
    "stockCodes": [
        "000016"
    ]
})
print('code: '+ str(dataframe_rlt['code']))
print('\ndata:')
print(dataframe_rlt['data'])
print('\nmsg: ' + dataframe_rlt['msg'])
```

    code: 0
    
    data:
      areaCode cnName market               publishDate source stockCode
    0       cn   上证50      a  2004-01-01T16:00:00.000Z     sh    000016
    
    msg: success
    
