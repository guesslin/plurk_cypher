#!/usr/bin/env python
# -*- coding: utf-8 -*-


NUMBERS = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
CARRY = ['整', '十', '百', '千', '萬', '億']  # 後面三個不確定用不用得到，但總之先留著
TIMES = ['點', '分']
PREFIX = '瀟笑'


def enc(s):
    ''' 在加密完之後要加上密文開頭代表碼
    >>> print enc('這是測試密文')
    瀟笑這是測試密文
    '''
    return '{}{}'.format(PREFIX, s)


def dec(s):
    ''' 在解密之前要把密文開頭代表碼拿掉
    >>> print dec(enc('這是測試密文'))
    這是測試密文
    >>> print dec(enc('這是測試密文瀟笑的密文'))
    這是測試密文瀟笑的密文
    '''
    return ''.join(s.split(PREFIX, 1)[1:])


def timeToChinese(t):
    ''' 輸入時間格式 hhmm
    07:00 => 七點整
    19:56 => 十九點五十六分
    >>> print timeToChinese('07:00')
    七點整
    >>> print timeToChinese('19:56')
    十九點五十六分
    '''
    res = []
    splitTime = t.split(':')
    hours = int(splitTime[0])
    hourTen = hours / 10
    if hourTen not in (0, 1):
        res.append(NUMBERS[hourTen])
        res.append(CARRY[1])  # 十
    elif hourTen is 1:
        res.append(CARRY[1])  # 十
    hour = hours % 10
    res.append(NUMBERS[hour])
    res.append(TIMES[0])
    mins = int(splitTime[1])
    if mins == 0:
        res.append(CARRY[0])
    else:
        minTen = mins / 10
        if minTen is not 0:
            res.append(NUMBERS[minTen])
            res.append(CARRY[1])
        minn = mins % 10
        res.append(NUMBERS[minn])
        res.append(TIMES[1])
    return ''.join(res)


def isSecret(s):
    ''' 檢查是否為加密密文
    >>> isSecret('瀟笑的秘聞')
    True
    >>> isSecret('隨便啦！')
    False
    >>> isSecret('不是瀟笑的密文')
    False
    '''
    return s.startswith(PREFIX)


if __name__ == '__main__':
    pass
