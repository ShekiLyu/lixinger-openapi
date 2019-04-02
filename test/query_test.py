# -*- coding: utf-8 -*-
'''
测试代码

注意：因为token值涉及账户隐私，不能在代码里写，所以请在代码所在目录下创建一个token.cfg文件，并将token值写入。token.cfg文件我已经在git里忽略，不会被上库。
'''
import sys, os
if os.path.abspath('..') not in sys.path:
    sys.path.append(os.path.abspath('..'))
import unittest

from lixinger_openapi.token import set_token
from lixinger_openapi.query import (
    query_json,
    query_dataframe,
)

class DataTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_query_json_001(self):
        rlt = query_json('a.stock', {
            "industryType": "bank"
        })
        self.assertEqual(0, rlt['code'])
        self.assertEqual("success", rlt['msg'])
        self.assertEqual("000001", rlt['data'][0]['stockCode'])

if __name__ == '__main__':
    unittest.main()
