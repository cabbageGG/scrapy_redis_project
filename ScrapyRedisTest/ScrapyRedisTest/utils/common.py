# -*- coding: utf-8 -*-

# 2017/11/7 下午3:57

__author__ = 'li yangjin'

import hashlib, re

def get_md5(url):
    m = hashlib.md5()
    if isinstance(url, str):
        url = url.encode('utf-8')
    m.update(url)
    return m.hexdigest()

def extract_num(text):
    #从字符串中提取出数字
    match_re = re.match(".*?(\d+).*", text)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

if __name__ == '__main__':
    url = '11qddfrffgt'
    id = get_md5(url)
    print (id)




