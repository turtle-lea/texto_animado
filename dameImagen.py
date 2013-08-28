
#! usr/bin/python

class ImageProvider:
	def __init__(self):
		self.dicc = {'foo':"im_1.jpeg", 'bar':"im_2.jpeg"}

	def imageFor(self,word):
		if word in self.dicc.keys():
			return self.dicc[word]
		else:
			return "imim_3_3.jpeg"

	
		
