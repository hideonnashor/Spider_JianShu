import sys;
sys.path.append("E:\PythonSpace\Spider_JianShu")
import html_downloader,res_parser,url_manager,html_file
import time

class Spider(object):
	"""docstring for Spider"""
	def __init__(self):
		self.urls=url_manager.UrlManager()
		self.downloder=html_downloader.HtmlDownloader()
		self.parser=res_parser.HtmlParser()
		self.file=html_file.HtmlWrite()

	def begin(self,my_urls):
		while 1:
			self.urls.addNextUrl(my_urls)
			while self.urls.hasNewUrl()!=0:
				try:
					next_url=self.urls.getNextUrl()
					print('\n爬取 %s'%(next_url))
					html_content=self.downloder.download(next_url)#下载页面
					listOutput=self.parser.parser(html_content)#解析并打印
					#self.urls.addNextUrl(my_urls)
					outPut=self.file.openFile('E:\PythonSpace\Spider_JianShu\outPut','r+')
					for line in listOutput:
						outPut.write(repr(line)+"\n"+"\n")#输出到文件
					outPut.write("\n"+"\n"+"\n")
					outPut.close()#关闭文件
				except:
					print("爬取失败")
			time.sleep(10)
			

if __name__=="__main__":
	my_urls=["http://www.jianshu.com/"]
	spider=Spider()
	spider.begin(my_urls)#传入参数应为列表，这里列表长度为1,因为实际上只对一个网站做了适配的解析器
	input()