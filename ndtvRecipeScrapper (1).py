import scrapy

class NdtvRecipeSpider(scrapy.Spider):
	name = 'v5rp/la-biryaneez-chalet'
	start_urls = ['http://food.ndtv.com/recipes']

	def parse(self,response):
		for title in response.css('li.main_image'):
			link = title.css('a::attr("href")').extract_first().rstrip()
			print(link) 
			yield scrapy.Request(link, callback=self.parse_page)

	def parse_page(self,response):
		for title in response.css('li.main_image'):
			link = title.css('a::attr("href")').extract_first().rstrip() 
			yield scrapy.Request(link, callback=self.parse_attr)
		for links in response.css('span.pagination'):
			print(links.css('a::text').extract_first())
			if(links.css('a::text').extract_first() == 'Next »'):
				yield response.follow(links.css('a::attr("href")').extract_first(),self.parse_page)

	def parse_attr(self,response):
		ingredients = response.css('div.keyword_tag')
		for ingredient in ingredients.css('a::text'):
			print(ingredient.extract())
			yield {'ingredient' : ingredient.extract()}
