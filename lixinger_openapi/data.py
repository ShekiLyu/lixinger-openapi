# -*- coding: utf-8 -*-
'''
DataFrame接口
'''
from lixinger_openapi.baseapi import(
    STOCK_FUNDAMENTAL_INFO_URL,
    STOCK_FS_INFO_URL,
    INDICE_FUNDAMENTAL_INFO_URL,
    HK_STOCK_FUNDAMENTAL_INFO_URL,
    HK_STOCK_FS_INFO_URL,
    HK_INDICE_FUNDAMENTAL_INFO_URL,
    basic_query_info_df,
)

def stock_fundamental_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    '''
    获取A股公司基本面数据，返回DataFrame结构
    '''
    return basic_query_info_df(STOCK_FUNDAMENTAL_INFO_URL, date, startDate, endDate, stockCodes, metrics)

def stock_fs_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    '''
    获取A股公司财务数据，返回DataFrame结构
    '''
    return basic_query_info_df(STOCK_FS_INFO_URL, date, startDate, endDate, stockCodes, metrics)

def indice_fundamental_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    '''
    获取A股指数基本面数据，返回DataFrame结构
    '''
    return basic_query_info_df(INDICE_FUNDAMENTAL_INFO_URL, date, startDate, endDate, stockCodes, metrics)

def hk_stock_fundamental_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    '''
    获取港股公司基本面数据，返回DataFrame结构
    '''
    return basic_query_info_df(HK_STOCK_FUNDAMENTAL_INFO_URL, date, startDate, endDate, stockCodes, metrics)

def hk_stock_fs_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    '''
    获取港股公司财务数据，返回DataFrame结构
    '''
    return basic_query_info_df(HK_STOCK_FS_INFO_URL, date, startDate, endDate, stockCodes, metrics)

def hk_indice_fundamental_info(date=None, startDate=None, endDate=None, stockCodes=None, metrics=None):
    '''
    获取港股指数基本面数据，返回DataFrame结构
    '''
    return basic_query_info_df(HK_INDICE_FUNDAMENTAL_INFO_URL, date, startDate, endDate, stockCodes, metrics)
