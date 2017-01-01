#!/usr/bin/env python
# -*- coding: utf-8 -*-


NUMBERS = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
CARRY = ['整', '十', '百', '千', '萬', '億']  # 後面三個不確定用不用得到，但總之先留著
TIMES = ['時', '分']
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
    0700 => 七點整
    1956 => 十九點五十六分
    >>> print timeToChinese('0700')
    七點整
    >>> print timeToChinese('1956')
    十九點五十六分
    '''
    return t


def isSecret(s):
    ''' 檢查是否為加密密文
    >>> isSecret('瀟笑的秘聞')
    True
    >>> isSecret('隨便啦！')
    False
    '''
    return s.startswith(PREFIX)


if __name__ == '__main__':
    pass
