# -*- coding: utf-8 -*-
'''
token全局管理
'''
import os

__token__ = None

def set_token(token, write_token = True):
    '''
    加载token
    '''
    global __token__
    __token__ = token
    if write_token:
        token_cfg = os.getcwd() + '/token.cfg'
        with open(token_cfg, 'w') as f:
                f.write(token)

def get_token():
    '''
    获取token
    '''
    global __token__
    if __token__ is None:
        token_cfg = os.getcwd() + '/token.cfg'
        if os.path.exists(token_cfg):
            with open(token_cfg, 'r') as f:
                __token__ = f.read().strip()
    return __token__
