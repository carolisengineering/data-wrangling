import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request

#PATH_PREFIX = '/globalassets/cps-pages/about-cps/district-data/demographics/'

# class FilesItem(scrapy.Item):
#      file_urls = scrapy.Field()
#      files = scrapy.Field

class CPSDemographics(scrapy.Spider):
    name = 'cpsdemographics'
    allowed_domains = ['www.cps.edu']
    start_urls = ['https://www.cps.edu/about/district-data/demographics']

    file_directory = 'files/'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        page = response.url.split("/")[-2]
        filename = f'{self.file_directory}{self.name}-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        demographic_file_links = response.css('a.primary-link::attr(href)')
        for file in demographic_file_links:
            file_url = file.get()
            full_url=response.urljoin(file_url)
            yield Request(url=full_url, callback=self.save_file)

    def parse_item(self, response):
        item = CPSDemographicsItem()
        item['file_url'] = file_url
        yield item

    def save_file(self, response):
        filename = response.url.split('/')[-1]
        filepath = f'{self.file_directory}{filename}'
        self.logger.info('Saving File %s', filename)
        with open(filepath, 'wb') as f:
            f.write(response.body)

