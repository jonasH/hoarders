from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

import codecs


class EulerproblemsSpider(CrawlSpider):
    name = 'eulerproblems'
    allowed_domains = ['projecteuler.net']
    start_urls = ['http://www.projecteuler.net/problems']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'problem='), callback='parse_item', follow=False),
    )

    def print_to_file(self, text):
        output_file = codecs.open("/home/jonas/data/scrapy/euler.html",
                                  encoding='utf-8', mode='a')
        output_file.write(text + '\n')
        output_file.close()

    def in_file(self, url):
        output_file = codecs.open("/home/jonas/data/scrapy/euler.html",
                                  encoding='utf-8', mode='r')
        for line in output_file:
            if "<h1>" + url + "</h1>" == line:
                output_file.close()
                return True
        output_file.close()
        return False

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        if not self.in_file(response.url):
            self.print_to_file("<h1>" + response.url + "</h1>")
            self.print_to_file( hxs.select('//div[@class="problem_content"]').extract()[0])

        self.log(response.url)
        

