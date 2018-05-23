# -*- coding: utf-8 -*-

import lixinger_openapi as lo
lo.load_token("f723c869-4afd-4a59-ab06-47813995e4ed")

df = lo.json.indice_fundamental_info(date='2018-05-21', stockCodes=['000300','000905'], metrics=['pe_ttm','pb'])

print(df)
