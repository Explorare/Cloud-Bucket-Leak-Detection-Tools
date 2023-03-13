#!/usr/bin/python3.8.4 (python版本)
# -*- coding: utf-8 -*-
# @Author  : UzJu@菜菜狗
# @Email   : UzJuer@163.com
# @Software: PyCharm
# @Time    : 2022/7/3 13:31
# @File    : results.py

import os
import csv
import pandas as pd
from config.conf import NowTime


def aliyun_save_file(target, BucketHijack, GetBucketObjectList, PutBucketObject, GetBucketAcl, PutBucketAcl, GetBucketPolicy):
    filepath = f'{os.getcwd()}/results/{NowTime}.csv'
    rows = [
        [f"{target}", BucketHijack, GetBucketObjectList, PutBucketObject, GetBucketAcl, PutBucketAcl, GetBucketPolicy]
    ]
    if not os.path.isfile(filepath):
        headers = ['Bucket', 'BucketHijack', 'GetBucketObjectList', 'PutBucketObject', 'GetBucketAcl', 'PutBucketAcl', 'GetBucketPolicy']
        with open(filepath, 'a+', newline='') as f:
            f = csv.writer(f)
            f.writerow(headers)
            f.writerows(rows)
    else:
        with open(filepath, 'a+', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(rows)

