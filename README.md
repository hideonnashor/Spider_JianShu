# Spider_JianShu
html_downloader.py #网页下载器
res_parser.py #网页解析器
url_manager.py #url管理器，想多了，只做了一个url的适配解析器，所以根本不需要url管理器
			   #的太多功能，只需要添加url即可，除非爬取多个DOM节点相同的url
spider_main.py #调度器，实现每50秒爬取一次，事实上对于这个网站来说间隔太短		