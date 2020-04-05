# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from coupang.items import CoupangItem

class coupang_spider(scrapy.Spider):
    name = "coupang_spider"
    allowed_domains = ["coupang.com"]
    target = input("输入你想要爬取的信息")
    target_url = 'http://www.coupang.com/' + "np/search?q=" +str(target)+"&channel=recent"
    print(target_url)
    start_urls = (
        target_url,
    )
    def get_page(self,response):
        item = CoupangItem()
        item["name"] = response.xpath("//*[@id='contents']/div[1]/div/div[3]/div[3]/h2/text()").extract()
        item["price"] = response.xpath(
            "//*[@id='contents']/div[1]/div/div[3]/div[5]/div[1]/div/div[2]/span[1]/strong/text()").extract()
        try:
            item["single_price"] = response.xpath(
                "//*[@class='unit-price']/text()").extract()
        except:
            item["single_price"] = "null"
        item["comment_number"] = response.xpath("//*[@id='prod-review-nav-link']/span[2]/text()").extract()
        item["comment_star"] = response.xpath("//*[@id='prod-review-nav-link']/span[1]/span/@style").extract()
        item["other_info"] = response.xpath("//*[@id='contents']/div[1]/div/div[3]/div[15]/ul/li/text()").extract()
        yield item



    def parse(self, response):
        page_urls = response.xpath("//*[@id='productList']/li/a/@href").extract()
        # print("=================", page_urls)
        for i in page_urls:
            # 单个页面中每个商品的链接
            every_items_url = "http://www.coupang.com" + i
            yield scrapy.Request(every_items_url, callback=self.get_page)
        # 获取下一页
        try:
            next_page = response.xpath("//*[@class='btn-next']/@href").extract()
        except:
            pass
        else:
            next_page_url = "http://www.coupang.com" + next_page[0]
            yield scrapy.Request(next_page_url, callback=self.parse)

# 测试请求头
# class test_spider(scrapy.Spider):
#     name = "test_spider"
#     allowed_domains = ["httpbin.org"]
#     start_urls = (
#         # 请求的链接
#         "https://httpbin.org/get?show_env=1",
#     )
#
#     def parse(self, response):
#         # 打印出相应结果
#         print(response.text)








# if __name__ == '__main__':
#     from scrapy import cmdline
#
#     cmdline.execute("scrapy crawl coupang_spider -o result.csv".split())
