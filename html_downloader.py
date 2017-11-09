import requests

class HtmlDownloader(object):
	"""docstring for HtmlDownloader"""
	def __init__(self):
		super(HtmlDownloader, self).__init__()

	def download(self,url):
		if url is None or url=="":
			print("没有相应url")
			return None
		res = requests.get(url)
		res.encoding='utf-8'
		res_content=res.content
		if res.status_code!=200:
			print("请求失败")
			return None	
		return res_content

