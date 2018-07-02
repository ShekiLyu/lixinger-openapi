# -*- coding: utf-8 -*-
'''
data模块测试代码
'''
import unittest
from lixinger_openapi.token import load_token
from lixinger_openapi.data import (
    indice_fundamental_info,
)

class DataTest(unittest.TestCase):
    def test_indice_fundamental_info(self):
        load_token("d6e241cb-77e6-4f2d-8e6e-565449d1f4f9")
        rlt = indice_fundamental_info(startDate='2018-01-01', endDate='2018-01-31', metrics=['pe_ttm'], stockCodes=['000300','000905'])
        self.assertEqual(1, rlt['code'])
        self.assertEqual('If get range date data, we only support single stockCode. Please change your stockCodes.', rlt['msg'])
        self.assertEqual(None, rlt['data'])

if __name__ == '__main__':
    unittest.main()
