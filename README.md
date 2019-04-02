# lixinger-openapi

## 简介
本Python包是[理杏仁开放平台](https://www.lixinger.com/open/api)WEB API的**非官方**Python封装，目的是方便Python量化分析者使用理杏仁开放平台数据。

## 快速使用指南
1. 使用set_token设置自己的token，设置后会在当前目录生成token.cfg文件，里面保存了你的token值，这样下次在当前目录使用的时候就不需要再执行set_token了。如果不想生成文件，可以设置参数write_token=False。
2. 使用query_json获取json格式数据，使用query_dataframe获取dataframe格式数据
3. 查询入参为url_suffix和query_params
    - url_suffix是请求的API地址后缀，前面的https://open.lixinger.com/api/ 就不需要写了，比如https://open.lixinger.com/api/a/indice/samples 只需要传入'a/indice/samples'即可。
    - url_suffix还支持一种更好用的写法，就是'a.indice.samples'，底层会把.替换成/。
    - query_params 你可以认为这就是传给API的json，只是token已经设置过了，就不需要写了。
4. 返回结果
    - query_json的返回结果和网站上一模一样
    - query_dataframe的返回结果有点不同，就是data域用dataframe格式替换了。

## 版本更新内容
### 版本1.0.0
重大改版，取消了业务封装，直接使用底层api，反而更灵活

### 版本0.2.5
适配新URL

### 版本0.2.4
适配新URL，修改接口名，禁用不可用接口

### 版本0.2.3
适配新的请求URL

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
