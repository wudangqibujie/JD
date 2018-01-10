import scrapy
from Jing_Dong.items import JingDongItem
import scrapy.shell
import lxml
import time
from bs4 import BeautifulSoup

class JD_WheelSpider(scrapy.Spider):
    name = "wheel"
    allowed_domains = ["www.jd.com"]
    start_url = ["http://www.jd.com/"]

    # start_urls =115035
    # count = 1
    search_url1 = "https://search.jd.com/Search?keyword={key}&enc=utf-8&page={page}"
    search_url2 = "https://search.jd.com/s_new.php?keyword={key}&enc=utf-8&page={page}&s=26&scrolling=y&pos=30&tpl=3_L&show_items={goods_items}"
    # shop_url = "http://mall.jd.com/index-{shop_id}.html"


    def start_requests(self):
        key = "裤子"
        for num in range(1,2):
            page1 = str(2*num-1)
            page2 = str(2*num)
            yield scrapy.Request(url=self.search_url1.format(key=key,page=page1),callback=self.parse,dont_filter = True)#后面这个参数指的是url不去重，不然会自动去掉这个重复的URL访问
            yield scrapy.Request(url=self.search_url1.format(key=key,page=page1),callback=self.get_next_half,meta={'page2':page2,'key':key},dont_filter = True)

    def get_next_half(self, response):

        try:
            print("----------^^^^^^^^^^^^^^----------")
            items = response.xpath('//div[@id="J_goodsList"]/ul/li/@data-pid').extract()
            key = response.meta['key']
            page2 = response.meta['page2']
            goods_items = ','.join(items)
            print(key)
            print(page2)
            print(items)
            yield scrapy.Request(url=self.search_url2.format(key=key,page=page2,goods_items=goods_items),callback=self.next_parse,dont_filter=True)

        except Exception as e:
            print("------------------没有数据-------------------")


    def parse(self, response):
        all_goods = response.xpath('//div[@id="J_goodsList"]/ul/li')
        for one_good in all_goods:
            item = JingDongItem()
            # try:
            data = one_good.xpath('div/div[4]/a/em')
            item['title'] = data.xpath('string(.)').extract()[0]
            item['comment_count'] = one_good.xpath('div/div[@class="p-commit"]/strong/a/text()').extract()[0]
            item['goods_url'] = one_good.xpath('div/div[1]/a/@href').extract()[0]
            # item['shop_id'] = one_good.xpath('div/div[@class="p-shop"]/')
            item['shop_url'] = 'https:'+one_good.xpath('div/div[@class="p-shop"]/span/a/@href').extract()[0]
            goods_id = one_good.xpath('div/div[2]/div/ul/li[1]/a/img/@data-sku').extract()[0]
            if goods_id:
                item['goods_id'] = goods_id
            price = one_good.xpath('div/div[3]/strong/i/text()').extract()
            if price:
                item['price'] = price[0]
            yield item
            # except Exception as e:
    def next_parse(self,response):
        print("A\nA\nA\nA\nA\nA\nA\nA\n")
        print(response.url)
        all_goods = response.xpath('/html/body/li')
        for one_good in all_goods:
            item = JingDongItem()
            # try:
            data = one_good.xpath('div/div[4]/a/em')
            item['title'] = data.xpath('string(.)').extract()[0]
            item['comment_count'] = one_good.xpath('div/div[@class="p-commit"]/strong/a/text()').extract()[0]
            item['goods_url'] = 'http:'+one_good.xpath('div/div[1]/a/@href').extract()[0]
            item['shop_url'] = 'http:'+ one_good.xpath('div/div[@class="p-shop"]/span/a/@href').extract()[0]
            goods_id = one_good.xpath('div/div[2]/div/ul/li[1]/a/img/@data-sku').extract()[0]
            if goods_id:
                item['goods_id'] = goods_id
            price = one_good.xpath('div/div[3]/strong/i/text()').extract()
            if price:
                item['price'] = price[0]

            yield item

            # print("C\nC\nC\n")
            #
            # except Exception as e:
            #     print("B\nB\nB\nB\nB\nB\nB\nB\n")


    # def next_parse(self,response):
    #     print("A\nA\nA\nA\nA\nA\nA\nA\n")
    #     all_goods = response.xpath('/html/body/li')
    #     for one_good in all_goods:
    #         try:
    #             data = one_good.xpath('div/div[4]/a/em')
    #             item['title'] = data.xpath('string(.)').extract()[0]
    #             item['comment_count'] = one_good.xpath('div/div[@class="p-commit"]/strong/a/text()').extract()[0]
    #             item['goods_url'] = 'http:'+one_good.xpath('div/div[1]/a/@href').extract()[0]
    #             item['shop_url'] = 'http:'+ one_good.xpath('div/div[@class="p-shop"]/span/a/@href').extract()[0]
    #             goods_id = one_good.xpath('div/div[2]/div/ul/li[1]/a/img/@data-sku').extract()[0]
    #             if goods_id:
    #                 item['goods_id'] = goods_id
    #             price = one_good.xpath('div/div[3]/strong/i/text()').extract()
    #             if price:
    #                 item['price'] = price[0]
    #
    #             yield item
    #
    #         except Exception as e:
    #             print("B\nB\nB\nB\nB\nB\nB\nB\n")
















