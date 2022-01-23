import scrapy

class CPSDemographics(scrapy.Spider):
    name = 'cpsdemographics'
    start_urls = ['https://www.cps.edu/about/district-data/demographics/']
    file_directory = 'files/'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        page = response.url.split("/")[-2]
        filename = f'{self.file_directory}cpsdemographics-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')