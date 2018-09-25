from coolscrapy.items import CeePeopleItem
import scrapy

class CeeSpider(scrapy.Spider):
	name = 'ceepeople'
	allowed_domains = ['cmu.edu/cee/people/']
	start_urls = ["https://www.cmu.edu/cee/people/"]

	# Scrap data with xpath
	"""
	XPath is to query parts of an HTML structure
	XPath: identify nodes and content in an XML document structure(including HTML)
	Create XPath query to find specific tables, reference specific rows, or find 
	cells of a table with certain attributes 
	"""
	# To extract the title and links 
	def parse(self, response):
		for sel in response.xpath('//*[@id="content"]/div[4]'):
			item = CeePeopleItem()
			item['title'] = sel.xpath('/a/text()')[0].extract()
			item['link'] = sel.xpath('/a')[0].extract()
			url = response.urljoin(item['link'])
			# item['desc'] = sel.xpath()[0].extract()
			print(item['title'],item['link'])
			yield scrapy.Request(url, callback = self.parse_directory)

	# def parse_directory(self, response):
	# 	detail = response.xpath()
	# 	item = CeePeopleItem()
	# 	item['title'] = detail.xpath()[0].extract()
	# 	item['link'] = response.url
	# 	print(item['title'], item['link'])
	# 	yield item