import scrapy

class GetPrice(scrapy.Spider):
	name="prices"
	urls=[
			'https://www.ambientedirect.com/en/categories/furniture'
		]
	
			# response.xpath('//div//div[@class="productSimpleTeaser__brand"]/text()').extract()

	def parse(self, response):
		for line in response.xpath('//div'):
			yield {
				# Find how to get category
				'Company': line.xpath('//div//div//div//div[@class="productSimpleTeaser__name"]/text()').extract_first(),
				'Brand': line.xpath('//div//div//div//div[@class="productSimpleTeaser__brand"]/text()').extract_first()
				# 'Price':
				# 'Discount':
			}
		# page = response.url.split("/")[-2]
		filename = 'price.txt'
		with open (filname, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)