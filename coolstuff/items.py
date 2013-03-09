# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TraderaItem(Item):
    
    itemHeading = Field()
    leadingBid = Field()
    bids = Field()
    remainingTime = Field()
    finishTime = Field()
    itemText = Field()
    publiced = Field()
    objectID = Field()
    visitors = Field()
    postage = Field()
    startBid = Field()
    seller = Field()
    sellerRating = Field()
