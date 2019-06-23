from html.parser import HTMLParser

class CountMovies(HTMLParser):
	movieCount=-1;
	readingArticle=False;
	readingData=False;
	def handle_starttag(self, tag, attrs):
		#================================ARTICLE==========================================
		if tag=="div" and ("class","desc") in attrs:
			if self.movieCount==-1:
				self.readingArticle=True;
		if self.readingArticle and tag=="span":
			self.readingData=True;
	def handle_data(self, data):
		if self.readingData:
			#print("Length: ", data)
			self.movieCount=int(data.split(' ')[2].replace(',',''));
			self.readingData=False;
			self.readingArticle=False;
	def getMovieCount(self):
		return self.movieCount;

