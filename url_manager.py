class UrlManager(object):
	"""docstring for UrlManager"""
	def __init__(self):
		self.next_urls = set();#未爬取的url
		self.completed_urls = set();#已爬取的url

	def addNextUrl(self,urls):#添加下一个url
		if urls is None or len(urls)==0:
			print("缺失url串")
			return None
		for url in urls:
			self.next_urls.add(url)

	def getNextUrl(self):#取出下一个的url
		next_url = self.next_urls.pop()#剔除最后一个字符串并且返回
		self.completed_urls.add(next_url)
		return next_url

	def hasNewUrl(self):#返回管理器中未爬取的url的数量
		return len(self.next_urls)
		
		