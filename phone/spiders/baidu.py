# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy_splash import SplashRequest

# splash lua script
script = """
         function main(splash, args)
             assert(splash:go(args.url))
             assert(splash:wait(args.wait))
             js = string.format("document.querySelector('#kw').value=%s;document.querySelector('#su').click()", args.phone)
             splash:evaljs(js)
             assert(splash:wait(args.wait))
             return splash:html()
         end
         """

class BaiduSpider(Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    url = 'https://www.baidu.com'

    # start request
    def start_requests(self):
        yield SplashRequest(self.url, callback=self.parse, endpoint='execute',
                            args={'lua_source': script, 'phone': '13660298662', 'wait': 5})

    # parse the html content
    def parse(self, response):
        info = response.css('div.op_mobilephone_r.c-gap-bottom-small').xpath('span/text()').extract()
        print('=' * 40)
        print(''.join(info))
        print('=' * 40)
