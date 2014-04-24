from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from hoarders.items import TraderaItem
import codecs

class TraderaSpider(CrawlSpider):
    name = 'tradera'
    allowed_domains = ['tradera.com']
    start_urls = ['http://www.tradera.com/nintendo-gamecube-c3_3004', 'http://www.tradera.com/playstation-psone-c3_3012', 'http://www.tradera.com/playstation-2-ps2-c3_3013', 'http://www.tradera.com/sega-dreamcast-c3_3001', 'http://www.tradera.com/xbox-c3_3016']

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
            
    def getStringFromXPath(self, hxs, xPath):
        extractedText = hxs.select(xPath).extract()
        return self.getStringFromArray(extractedText)

    def parse_item2(self, response):
        """A callback function that produces traderaItems from auction html"""
        hxs = HtmlXPathSelector(response)
        traderaItem = TraderaItem()

        traderaItem['itemHeading'] = self.getStringFromXPath(hxs, '//h1[@class="auction_headline"]/text()')
        traderaItem['leadingBid'] = self.getStringFromXPath(hxs, '//label[@id="leadingBidAmount"]/text()')
        traderaItem['bids'] = self.getStringFromXPath(hxs, '//h5[@id="numberOfBids"]/text()')
        traderaItem['remainingTime'] = self.getStringFromXPath(hxs, '//label[@id="timeLeftLabel"]/text()')
        traderaItem['itemText'] = self.getStringFromXPath(hxs, '//div[@class="description"]/p/text()')
        traderaItem['seller'] = self.getStringFromXPath(hxs, '//a[@class="blueLink"]/b/text()')
        traderaItem['sellerRating'] = self.getStringFromXPath(hxs, '//div[@class="rightSideInfoInBoxG-bottomLine"]/a[@class="DSRMedium"]/text()')
        if  len(hxs.select('//div[@class="objectInfoOnTop"]/text()')) == 3:
            traderaItem['publiced'] = hxs.select('//div[@class="objectInfoOnTop"]/text()').extract()[1].strip()
            traderaItem['objectID'] = hxs.select('//div[@class="objectInfoOnTop"]/text()').extract()[2].strip()

        return traderaItem
