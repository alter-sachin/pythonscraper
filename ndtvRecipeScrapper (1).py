import scrapy

class NdtvRecipeSpider(scrapy.Spider):#scrapy spider object as an argument 
	name = 'v5rp/la-biryaneez-chalet' 
	start_urls = ['http://food.ndtv.com/recipes'] #starting url , this page has a list of recipe types 

	def parse(self,response):      # self , the current instance , needs to be explicitly defined in python 
		for title in response.css('li.main_image'): #extract css li class main_image , iterate over titles
			link = title.css('a::attr("href")').extract_first().rstrip() #extract url for title 1 
			print(link) #check
			yield scrapy.Request(link, callback=self.parse_page)  #yield is like return but will give you a generator , a generator is an iterable with only the first value returned. 
									# callbacks send argument to function called.
	def parse_page(self,response): 
		for title in response.css('li.main_image'):
			link = title.css('a::attr("href")').extract_first().rstrip() 
			yield scrapy.Request(link, callback=self.parse_attr)#send link to article to extract the attribute we wish to parse
		for links in response.css('span.pagination'):
			print(links.css('a::text').extract_first())
			if(links.css('a::text').extract_first() == 'Next »'):
				yield response.follow(links.css('a::attr("href")').extract_first(),self.parse_page)

	def parse_attr(self,response):
		ingredients = response.css('div.keyword_tag')
		for ingredient in ingredients.css('a::text'):
			print(ingredient.extract())
			yield {'ingredient' : ingredient.extract()}
