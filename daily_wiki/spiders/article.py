# -*- coding: utf-8 -*-
import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/']

    # Enable Feed Storage
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'file:///tmp/featured-articles-%(time)s.json'
    }

    def parse(self, response):
        host = self.allowed_domains[0]
        for link in response.css(".featured_article_metadata > a"):
            yield Article(
                title = link.attrib.get("title"),
                link = f"https://{host}{link.attrib.get('href')}"
            )
