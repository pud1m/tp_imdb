from html.parser import HTMLParser

class Parser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.movieList=[]
		self.actualTitle="";
		self.actualGenre="";
		self.actualIMDB="";
		self.actualMetascore="";
		self.readingTitle=False;
		self.readingTitleData=False;
		self.readingIMDB=False;
		self.readingIMDBData=False;
		self.readingMetascore=False;
		self.readingMetascoreData=False;
		self.readingGenre=False;
	def handle_starttag(self, tag, attrs):
		#================================READ-TITLE========================================
		if tag=="h3" and ("class","lister-item-header") in attrs:
			self.readingTitle=True;
		if self.readingTitle and tag=="a":
			self.readingTitleData=True;
		#================================READ-IMDB=========================================
		if tag=="div" and ("class","inline-block ratings-imdb-rating") in attrs:
			self.readingIMDB=True;
		if self.readingIMDB and tag=="strong":
			self.readingIMDBData=True;
		#================================READ-METASCORE====================================
		if tag=="div" and ("class","inline-block ratings-metascore") in attrs:
			self.readingMetascore=True;
		if self.readingMetascore and tag=="span":
			self.readingMetascoreData=True;
		#================================READ-GENRE=========================================
		if tag=="span" and ("class","genre") in attrs:
			self.readingGenre=True;
	def handle_data(self, data):
		 #================================READ-IMDB=========================================
		if self.readingIMDBData:
			#print("IMDB Rating: ", data)
			self.actualIMDB=data.strip();
			self.readingIMDBData=False;
			self.readingIMDB=False;
		#================================READ-TITLE========================================
		if self.readingTitleData:
			#print("Title: ",data)
			self.actualTitle=data.strip();
			self.readingTitleData=False;
			self.readingTitle=False;
		#================================READ-METASCORE====================================
		if self.readingMetascoreData:
			#print("Metascore: ",data)
			self.actualMetascore=data.strip();
			self.readingMetascoreData=False;
			self.readingMetascore=False;
			self.movieList.append({"Title":self.actualTitle,"Genre":self.actualGenre,"IMDB":self.actualIMDB,"Metascore":self.actualMetascore})
		#================================READ-GENRE========================================
		if self.readingGenre:
			#print("Genre: ",data.strip().replace('\n',''))
			self.actualGenre=data.strip().replace('\n','')
			self.readingGenre=False;

	def getMovieList(self):
		return self.movieList;
