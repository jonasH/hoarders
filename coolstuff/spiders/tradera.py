from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from coolstuff.items import TraderaItem
import codecs


class TraderaSpider(CrawlSpider):
    name = 'tradera'
    allowed_domains = ['tradera.com']
    start_urls = ['http://www.tradera.com/spel-gb-c3_300201']

    rules = (
        Rule(SgmlLinkExtractor(allow=('.*',), restrict_xpaths='//a[@class="nextPageBtn"]'),callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=('.*',), restrict_xpaths=('//div[@class="ObjectHeadline"]',)),callback='parse_item2', follow=True),
    )
#        
    def parse_item(self, response):

        hxs = HtmlXPathSelector(response)
        traderaItems = []
        #get all the text
        items = hxs.select('//div[@class="ObjectHeadline"]/a/@href').extract()
        output_file = codecs.open("/home/jonas/data/scrapy/tradera.txt",
                                  encoding='utf-8', mode='a')

        for item in items:
            output_file.write('www.tradera.com' + item + '\n')
            ad = TraderaItem(testField=item)
            traderaItems.append(ad)

        output_file.close()
        return traderaItems

    def parse_item2(self, response):
        self.log('afasdfaehh')
        

    # def parse(self, response):
    #     self.parse_item(response)
        
