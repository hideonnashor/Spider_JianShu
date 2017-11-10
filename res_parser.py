from bs4 import BeautifulSoup

class HtmlParser(object):
	"""docstring for HtmlParser"""
	def __init__(self):
		super(HtmlParser, self).__init__()

	def parser(self,res_content):
		soup = BeautifulSoup(res_content,"html5lib")
		#查找标题标签
		titles = soup.select('a.title')
		#查找图片标签
		pictures = soup.select('a.wrap-img img')
		#查找简要内容
		contents = soup.select('div.content p')

		listDatas=[]#创建列表用于储存
		#筛选信息
		for title,picture,content_text in zip(titles,pictures,contents):
			data={
				'title':title.get_text(),
				'picture':picture.get("src"),
				'content_text':content_text.get_text().replace("\n",""),
			}
			print(data)
			listDatas.append(data)
		
		return listDatas