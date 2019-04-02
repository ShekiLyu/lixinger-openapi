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
        #你可以在这里运行一次set_token，写入token.cfg文件，然后再删除token值，这样有了cfg文件以后都不用set_token了。
        #set_token("")

    def test_query_json_001(self):
        rlt = query_json('a.stock', {
            "industryType": "bank"
        })
        self.assertEqual(0, rlt['code'])
        self.assertEqual("success", rlt['msg'])
        self.assertEqual("000001", rlt['data'][0]['stockCode'])

    def test_query_dataframe_001(self):
        rlt = query_dataframe('a.stock', {
            "industryType": "bank"
        })
        self.assertEqual(0, rlt['code'])
        self.assertEqual("success", rlt['msg'])
        self.assertEqual("000001", rlt['data'].loc[0, 'stockCode'])

    def test_query_json_002(self):
        rlt = query_json('a.stock.indice', {
            "stockCode": "000028"
        })
        self.assertEqual(0, rlt['code'])
        self.assertEqual("success", rlt['msg'])
        self.assertEqual("cn", rlt['data'][0]['areaCode'])
        self.assertEqual("399348", rlt['data'][0]['stockCode'])
    
    def test_query_json_003(self):
        rlt = query_json('a.stock.industry', {
            "stockCode": "000028"
        })
        self.assertEqual(0, rlt['code'])
        self.assertEqual("success", rlt['msg'])
        self.assertEqual("cn", rlt['data'][0]['areaCode'])
        self.assertEqual("C05", rlt['data'][0]['stockCode'])

    def test_query_json_004(self):
        rlt = query_json('a.indice.fundamental', {
            "date": "2018-01-19",
            "stockCodes": ["000016"],
            "metrics": [
                "pe_ttm.y_10.weightedAvg",
                "pe_ttm.weightedAvg",
                "mc"
            ]
        })
        self.assertEqual(0, rlt['code'])
        self.assertEqual("success", rlt['msg'])
        self.assertEqual("2018-01-19", rlt['data'][0]['date'][:10])
        self.assertLess(12, rlt['data'][0]['pe_ttm']['weightedAvg'])

    def test_query_json_005(self):
        rlt = query_json('a.indice.samples', {
            "date": "2017-09-30",
            "stockCodes": ["000016"]
        })
        self.assertEqual(0, rlt['code'])
        self.assertEqual("success", rlt['msg'])
        self.assertEqual("000016", rlt['data'][0]['stockCode'])
        self.assertEqual("600000", rlt['data'][0]['samples'][0])

if __name__ == '__main__':
    unittest.main()
