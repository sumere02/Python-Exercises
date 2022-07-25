from django.urls import clear_script_prefix
import scrapy


class BooksSpider(scrapy.Spider):
    name = "Books"
    page_count = 1
    file = open("Books.txt","a",encoding="UTF-8")
    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/category&page=1&filter_category_all=true&path=1&filter_in_stock=1&sort=purchased_365&order=DESC"
    ]
    def parse(self, response):
        self.page_count += 1
        name = response.css("div.name.ellipsis a span::text").getall()
        publishers = response.css("div.publisher a.alt::attr(href)").getall()
        publishers_text = list()
        for publisher in publishers:
            publishers_text.append(publisher.split("/")[-2].title())
        authors = response.css("div.author span a.alt::attr(href)").getall()
        authors_text = list()
        for author in authors:
            authors_text.append(author.split("/")[-2].title())
        book = list(zip(name,publishers_text,authors_text))
        self.file.write("Page: " + str(self.page_count))
        self.file.write("\n")
        for book_name,book_publisher,book_author in book:
            self.file.write("***********************************\n")
            self.file.write("Name: {}\n".format(book_name))
            self.file.write("Publisher: {}\n".format(book_publisher))
            self.file.write("Author: {}\n".format(book_author))
            self.file.write("***********************************\n")
        if self.page_count < 6:
            next_url = response.css("a.next::attr(href)").get()
            yield scrapy.Request(url = next_url ,callback = self.parse)
        else:
            self.file.close()