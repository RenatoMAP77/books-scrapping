import scrapy
from scrapy.crawler import CrawlerProcess
import json

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['https://books.toscrape.com/']

    books_list = []

    def parse(self, response):
        for books in response.css('article.product_pod'):
            #Se a avaliacao do livro for maior que 3 e o valor menor que £50.00, coleta os dados
            if books.css('p.star-rating::attr(class)').get().split()[1] in ['Three', 'Four', 'Five'] \
            and float(books.css('p.price_color::text').get().split('£')[1]) < 50:
             books_data = {
                'title': books.css('h3 a::attr(title)').get(),
                'price': books.css('p.price_color::text').get(),
                'stars': books.css('p.star-rating::attr(class)').get().split()[1],
             }
             self.books_list.append(books_data)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
                with open('books2.json', 'w', encoding='utf-8') as f:
                    json.dump(self.books_list, f, ensure_ascii=False, indent=4)

process = CrawlerProcess()
process.crawl(BooksSpider)
process.start()