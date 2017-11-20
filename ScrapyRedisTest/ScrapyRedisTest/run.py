# -*- coding: utf-8 -*-

# 2017/11/6 下午7:32

__author__ = 'li yangjin'



from scrapy import cmdline


name = 'jobbole'

cmd = 'scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())
