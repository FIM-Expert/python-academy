import scrapy
from scrapy.crawler import CrawlerProcess

class First_Crawler(scrapy.Spider):
    name = 'datacamp_courses'
    
    def start_requests(self):
        yield scrapy.Request(url="https://apps.bea.gov/iTable/iTable.cfm?ReqID=19&step=2#reqid=19&step=2&isuri=1&1921=underlying", callback=self.parse)
    
    def parse(self, response):
        courses = response.url
        print(courses)
        
process = CrawlerProcess()
process.crawl(First_Crawler)
process.start()