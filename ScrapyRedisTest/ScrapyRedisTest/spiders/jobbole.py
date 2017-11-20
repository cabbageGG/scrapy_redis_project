# -*- coding: utf-8 -*-
from scrapy.http import Request
import urlparse

from ScrapyRedisTest.items import JobBoleArticleItem, JobBoleArticleItemLoader

from ScrapyRedisTest.utils.common import get_md5

from scrapy_redis.spiders import RedisSpider


class JobboleSpider(RedisSpider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    #start_urls = ['http://blog.jobbole.com/all-posts/']
    redis_key = 'jobbole:start_urls'

    def parse(self, response):
        """
        1、获取每一页的urls
        2、获取下一页的url
        """
        if response.status == 404:
            print('failed 404')

        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=urlparse.urljoin(response.url, post_url), meta={'front_image_url':image_url}, callback=self.parse_detail)

        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
           yield Request(url=urlparse.urljoin(response.url, next_url), callback=self.parse)


    def parse_detail(self, response):

        #通过item loader加载item
        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        item_loader = JobBoleArticleItemLoader(item=JobBoleArticleItem(), response=response)  #注意这里的传入参数
        item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_id", get_md5(response.url))
        item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("front_image_url", [front_image_url])
        item_loader.add_css("praise_nums", ".vote-post-up h10::text")
        item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
        item_loader.add_css("fav_nums", ".bookmark-btn::text")
        item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("content", "div.entry")

        article_item = item_loader.load_item()

        yield article_item