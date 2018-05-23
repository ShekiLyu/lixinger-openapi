# -*- coding: utf-8 -*-

__token__ = None

def load_token(token):
    '''
    加载token
    '''
    global __token__
    __token__ = token

def get_token():
    return __token__
