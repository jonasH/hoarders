from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from coolstuff.items import CoolstuffItem
import codecs


class TraderaSpider(CrawlSpider):
    name = 'tradera'
    allowed_domains = ['tradera.com']
    start_urls = ['http://www.tradera.com/spel-gb-c3_300201']

    rules = (
        Rule(SgmlLinkExtractor(allow=('.*',), restrict_xpaths=('//a[@class="nextPageBtn"]',)),callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=('.*',), restrict_xpaths=('//a[@class="ObjectHeadline"]',)),callback='parse_add', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        #get all the text
        items = hxs.select('//div[@class="ObjectHeadline"]/a/text()').extract()
        output_file = codecs.open("/home/jonas/data/scrapy/tradera.txt",
                                  encoding='utf-8', mode='a')


        for item in items:
            output_file.write(item + '\n')

        output_file.close()

    def parse_add(self, response):
        pass
        

    def parse(self, response):
        self.parse_item(response)
        
