'''
基础操作
'''
# -*- coding: utf-8 -*-
import json
import requests
from pandas.io.json import json_normalize
__token__ = None

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
    return json_normalize(response.json())
