import scrapy

class CPSDemographics(scrapy.Spider):
    name = 'cpsdemographics'
    start_urls = ['https://www.cps.edu/about/district-data/demographics/']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)