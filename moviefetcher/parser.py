from html.parser import HTMLParser


class Parser(HTMLParser):
	movieList=[]
	movieCount=-1;
	actualMetascore="";
	readingArticle=False;
	readingTitle=False;
	readingTitleData=False;
	readingIMDB=False;
	readingIMDBData=False;
	readingMetascore=False;
	readingMetascoreData=False;
	readingGenre=False;

	def handle_starttag(self, tag, attrs):
		#================================ARTICLE==========================================
		if tag=="div" and ("id","main") in attrs:
			self.readingArticle=True;
		if tag=="div" and ("id","sidebar") in attrs:
			self.readingArticle=False;
		#================================MOVIE============================================
		if self.readingArticle and tag=="div" and ("class","lister-item mode-advanced") in attrs:
			if self.movieCount==-1 or self.movieList[self.movieCount]["Metascore"]!="":
				self.movieList.append({"Title":"","Genre":"","IMDB":"","Metascore":""})
				self.movieCount+=1;
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
			self.movieList[self.movieCount]['IMDB']=data.strip();
			self.readingIMDBData=False;
			self.readingIMDB=False;
		#================================READ-TITLE========================================
		if self.readingTitleData:
			#print("Title: ",data)
			self.movieList[self.movieCount]['Title']=data.strip();
			self.readingTitleData=False;
			self.readingTitle=False;
		#================================READ-METASCORE====================================
		if self.readingMetascoreData:
			#print("Metascore: ",data)
			self.movieList[self.movieCount]['Metascore']=data.strip();
			self.readingMetascoreData=False;
			self.readingMetascore=False;
		#================================READ-GENRE========================================
		if self.readingGenre:
			#print("Genre: ",data.strip().replace('\n',''))
			self.movieList[self.movieCount]['Genre']=data.strip().replace('\n','')
			self.readingGenre=False;

	def getMovieList(self):
		return self.movieList;
