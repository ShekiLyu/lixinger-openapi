'''
原始接口
'''
# -*- coding: utf-8 -*-
from . import baseapi

STOCK_FUNDAMENTAL_INFO_URL = "https://www.lixinger.com/api/open/a/stock/fundamental-info"
STOCK_FS_INFO_URL = "https://www.lixinger.com/api/open/a/stock/fs-info"
INDICE_FUNDAMENTAL_INFO_URL = "https://www.lixinger.com/api/open/a/indice/fundamental-info"

def load_token(token):
    baseapi.__token__ = token

def stock_fundamental_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    return baseapi._basic_query_info(STOCK_FUNDAMENTAL_INFO_URL, date, startDate, endDate, stockCodes, metrics)

def stock_fs_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    return baseapi._basic_query_info(STOCK_FS_INFO_URL, date, startDate, endDate, stockCodes, metrics)

def indice_fundamental_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    return baseapi._basic_query_info(INDICE_FUNDAMENTAL_INFO_URL, date, startDate, endDate, stockCodes, metrics)
