'''
基础操作
'''
# -*- coding: utf-8 -*-
import json
import requests
from pandas.io.json import json_normalize
from lixinger_openapi.token import get_token

STOCK_FUNDAMENTAL_INFO_URL = "https://www.lixinger.com/api/open/a/stock/fundamental-info"
STOCK_FS_INFO_URL = "https://www.lixinger.com/api/open/a/stock/fs-info"
INDICE_FUNDAMENTAL_INFO_URL = "https://www.lixinger.com/api/open/a/indice/fundamental-info"


def basic_query_info(url, date, startDate, endDate, stockCodes, metrics):
    if get_token() is None or metrics is None:
        return None
    query = {}
    if date is not None:
        query["date"] = date
    if startDate is not None:
        query["startDate"] = startDate
    if endDate is not None:
        query["endDate"] = endDate
    if stockCodes is not None:
        query["stockCodes"] = stockCodes
    query["token"] = get_token()
    query["metrics"] = metrics
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, data=json.dumps(query), headers=headers)
    if response.status_code != 200:
        return None
    return response.json()

def basic_query_info_df(url, date, startDate, endDate, stockCodes, metrics):
    rlt = basic_query_info(url, date, startDate, endDate, stockCodes, metrics)
    if rlt is None:
        return None
    return json_normalize(rlt)
