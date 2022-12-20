import scrapy


def remove_whitespace_and_newlines(string):
    # Replace all white space characters with a single space
    string = " ".join(string.split())
    # Replace all newline characters with an empty string
    string = string.replace("\n", "")
    return string


class GriffithSpider(scrapy.Spider):
    name = 'griffith'
    allowed_domains = ['www.griffith.ie']
    start_urls = ['https://www.griffith.ie'
                  ]

    maxdepth = 20
    nbdocs = 0

    def parse(self, response):

        from_url = ''
        from_text = ''
        depth = 0

        if 'from' in response.meta:
            from_url = response.meta['from']
        if 'text' in response.meta:
            from_text = response.meta['text']
        if 'depth' in response.meta:
            depth = response.meta['depth']


        # get all the <a> tags
        if depth < self.maxdepth:
            a_selectors = response.xpath("//a")
            for selector in a_selectors:
                link = selector.xpath("@href").extract_first()
                request = response.follow(link, callback=self.parse_text)
                request.meta['from'] = response.url
                request.meta['depth'] = depth + 1
                yield request

    def parse_text(self, response):
        text = ''.join(response.xpath("//body//text()").extract())
        cleaned_text = remove_whitespace_and_newlines(text)
        # writes the documents received to a file
        f = open(f"../../../documents/D{self.nbdocs}", "w")
        f.write(cleaned_text)
        f.close()

        # increments the number of documents
        self.nbdocs += 1
