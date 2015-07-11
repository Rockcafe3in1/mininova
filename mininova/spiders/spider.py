__author__ = 'liang'

from mininova.item import TorrentItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MininovaSpider(CrawlSpider):

    name = 'mininova'
    allowed_domains = ['mininova.org']
    start_urls = ['http://www.mininova.org/tor/2676093']
    rules = [Rule(LinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse_torrent(self, response):
        torrent = TorrentItem()
        torrent['url'] = response.url
        torrent['name'] = response.xpath("//div[@id='content']/h1/text()").extract()
        torrent['description'] = response.xpath("//div[@id='content']/div[@id='description']/text()").extract()
        torrent['size'] = response.xpath("//div[@id='content']/div[@id='specifications']/p[2]/text()[2]").extract()
        return torrent
