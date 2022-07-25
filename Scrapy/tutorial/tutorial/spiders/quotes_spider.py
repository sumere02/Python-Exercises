import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    quote_count = 1
    start_urls = ['https://quotes.toscrape.com/page/1/']
    file = open("quotes.txt","a",encoding="utf-8")
    def parse(self, response):
        for quote in response.css("div.quote"):
            title = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()                
            tags = quote.css("div.tags a.tag::text").getall()
            self.file.write(str(self.quote_count)+"\n")
            self.file.write("*********************************\n")
            self.file.write("Title:{}\n".format(title))
            self.file.write("Author:{}\n".format(author))
            self.file.write("Tags: {}\n".format(str(tags)))
            self.file.write("*********************************\n")
            self.quote_count += 1
        next_url = response.css("li.next a::attr(href)").get()
        if next_url is None:
            self.file.close()
        else:
            next_url = "https://quotes.toscrape.com" + next_url
            yield scrapy.Request(url = next_url,callback=self.parse)
"""   
    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
"""
    