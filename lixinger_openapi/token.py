# -*- coding: utf-8 -*-
'''
token全局管理
'''
__token__ = None

def load_token(token):
    '''
    加载token
    '''
    global __token__
    __token__ = token

def get_token():
    '''
    获取token
    '''
    return __token__
