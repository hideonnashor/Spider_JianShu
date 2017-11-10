class HtmlWrite(object):
	"""docstring for HtmlWrite"""
	def __init__(self):
		super(HtmlWrite, self).__init__()

	def openFile(self,file_root,method):
		self.file_html=open(file_root,method,encoding='utf-8')
		return self.file_html