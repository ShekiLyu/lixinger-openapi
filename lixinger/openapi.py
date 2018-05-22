'''
原始接口
'''
# -*- coding: utf-8 -*-
import json
import requests

STOCK_FUNDAMENTAL_INFO_URL = "https://www.lixinger.com/api/open/a/stock/fundamental-info"
STOCK_FS_INFO_URL = "https://www.lixinger.com/api/open/a/stock/fs-info"
INDICE_FUNDAMENTAL_INFO_URL = "https://www.lixinger.com/api/open/a/indice/fundamental-info"

__token__ = None

def load_token(token):
    __token__ = token

def _basic_query_info(url, date, startDate, endDate, stockCodes, metrics):
    if __token__ is None or metrics is None:
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
    query["token"] = __token__
    query["metrics"] = metrics
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, data=json.dumps(query), headers=headers)
    if response.status_code != 200:
        return None
    return response.json()

def stock_fundamental_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    return _basic_query_info(STOCK_FUNDAMENTAL_INFO_URL, date, startDate, endDate, stockCodes, metrics)

def stock_fs_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    return _basic_query_info(STOCK_FS_INFO_URL, date, startDate, endDate, stockCodes, metrics)

def indice_fundamental_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    return _basic_query_info(INDICE_FUNDAMENTAL_INFO_URL, date, startDate, endDate, stockCodes, metrics)
