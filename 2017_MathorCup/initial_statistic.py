#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 本程序统计初始状态下各区域单车数量
# 编程环境：Python 3.5.2

import re

print('读取数据...')
f = open('附件1 骑行数据.txt', 'r')
print('读取数据完毕！')
statistic = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': 0}
lines = f.readlines()
for line in lines:
    # 将每一行的数据分割为多个字符串
    items = re.sub('\n| ', '', line)
    items = re.split(',:', items)
    # print(items)
    # 统计出发前各区域单车数量
    if items[0] == '自行车序号':
        i = items[3]
        statistic[i] = statistic[i] + 1
print('结果如下：')
for i in range(10):
    index = str(i + 1)
    num = statistic[index]
    print('区域' + str(i + 1) + '：' + str(num) + '辆车')
