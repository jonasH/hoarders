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
        """A callback function"""
        hxs = HtmlXPathSelector(response)


    def getStringFromArray(self, array):
        result = u""
        for item in array:
            result = result + u" " + item.strip()

        return result
            

    def parse_item2(self, response):
        """A callback function that produces traderaItems from auction html"""
        hxs = HtmlXPathSelector(response)
        traderaItem = TraderaItem()

        traderaItem['itemHeading'] = self.getStringFromArray(hxs.select('//h1[@class="auction_headline"]/text()').extract())
        traderaItem['leadingBid'] = self.getStringFromArray(hxs.select('//label[@id="leadingBidAmount"]/text()').extract())
        traderaItem['bids'] = self.getStringFromArray(hxs.select('//h5[@id="numberOfBids"]/text()').extract())
        traderaItem['remainingTime'] = self.getStringFromArray(hxs.select('//label[@id="timeLeftLabel"]/text()').extract())
        traderaItem['itemText'] = self.getStringFromArray(hxs.select('//div[@class="description"]/p/text()').extract())
        traderaItem['seller'] = self.getStringFromArray(hxs.select('//a[@class="blueLink"]/b/text()').extract())
        traderaItem['sellerRating'] = self.getStringFromArray(hxs.select('//div[@class="rightSideInfoInBoxG-bottomLine"]/a[@class="DSRMedium"]/text()').extract())
        if  len(hxs.select('//div[@class="objectInfoOnTop"]/text()')) == 3:
            traderaItem['publiced'] = hxs.select('//div[@class="objectInfoOnTop"]/text()').extract()[1].strip()
            traderaItem['objectID'] = hxs.select('//div[@class="objectInfoOnTop"]/text()').extract()[2].strip()


        
        return traderaItem
