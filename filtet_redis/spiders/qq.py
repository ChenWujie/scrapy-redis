import scrapy


class QqSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['qq.com']
    start_urls = ['https://v.qq.com/']

    def parse(self, response):
        a_labels = response.xpath('//div[@class="mod_rank_list mod_rank_list_1column  "]/a')
        for a in a_labels[1:]:
            title = a.xpath("./@title").extract_first()
            url = a.xpath("./@href").extract_first()
            yield scrapy.Request(
                url=url,
                callback=self.parse2,
                meta={'title': title}
            )

    def parse2(self, response):
        title = response.meta['title']
        with open(title + '.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode(response.encoding))
        print('yes')

