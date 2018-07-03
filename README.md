# lixinger-openapi

## 简介
本Python包是[理杏仁开放平台](https://www.lixinger.com/open/api)WEB API的非官方Python封装，目的是方便Python量化分析者使用理杏仁开放平台数据。

## 版本更新内容
### 版本0.2.2
修复使用错误的查询条件无返回结果的BUG

### 版本0.2.1
适配新的返回结构。新返回结构将数据放到'data'字段里，新增'code'返回值，和'msg'返回消息。

### 版本0.2.0
适配港股接口，原有A股接口不变

更新文档，添加港股查询示例

### 版本0.1.1
适配pip版本10.0

### 版本0.1.0
初始版本，支持A股数据查询，支持json和dataframe格式

## 接口列表
包                     | 接口名                        | 接口功能
---------------------- | ----------------------------- | -------------------------
lixinger\_openapi      | load\_token                   | 加载token
lixinger\_openapi.json | stock\_fundamental\_info      | A股公司基本面数据(json格式)
lixinger\_openapi.json | stock\_fs\_info               | A股公司财务数据(json格式)
lixinger\_openapi.json | indice\_fundamental\_info     | A股指数基本面数据(json格式)
lixinger\_openapi.json | hk\_stock\_fundamental\_info  | 港股公司基本面数据(json格式)
lixinger\_openapi.json | hk\_stock\_fs\_info           | 港股公司财务数据(json格式)
lixinger\_openapi.json | hk\_indice\_fundamental\_info | 港股指数基本面数据(json格式)
lixinger\_openapi.data | stock\_fundamental\_info      | A股公司基本面数据(dataframe格式)
lixinger\_openapi.data | stock\_fs\_info               | A股公司财务数据(dataframe格式)
lixinger\_openapi.data | indice\_fundamental\_info     | A股指数基本面数据(dataframe格式)
lixinger\_openapi.data | hk\_stock\_fundamental\_info  | 港股公司基本面数据(dataframe格式)
lixinger\_openapi.data | hk\_stock\_fs\_info           | 港股公司财务数据(dataframe格式)
lixinger\_openapi.data | hk\_indice\_fundamental\_info | 港股指数基本面数据(dataframe格式)

参数列表和理杏仁开放平台完全一致，详细参数介绍见理杏仁开放平台。

## 安装
### 从PyPI安装
`pip install lixinger-openapi`

### 从Github安装
`pip install git+http://github.com/ShekiLyu/lixinger-openapi.git`

### 从PyPI更新版本
`pip install --upgrade lixinger-openapi`

### 从Github更新版本
`pip install --upgrade git+http://github.com/ShekiLyu/lixinger-openapi.git`

## 使用示例

详细使用方法请参考[用户使用指南](https://github.com/ShekiLyu/lixinger-openapi/blob/master/doc/user_guide.ipynb)。
