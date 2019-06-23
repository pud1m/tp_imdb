from .parser import Parser
from .countmovies import CountMovies
import urllib.request
import math
import time

#url="https://www.imdb.com/search/title/?title_type=feature&release_date=2017-01-01,2019-01-01&num_votes=500,&count=250";
#url2="https://www.imdb.com/search/title/?title_type=feature&release_date=2017-01-01,2019-01-01&num_votes=500,&count=250&start=251&ref_=adv_nxt"


def getMovieListFromURL(url):
	fp = urllib.request.urlopen(url)
	html = fp.read().decode("utf8")
	parser = Parser()
	parser.reset()
	parser.feed(html)
	ml=parser.getMovieList()
	fp.close()
	return ml;


def getPageNumber(url):
	fp = urllib.request.urlopen(url)
	html = fp.read().decode("utf8")
	countMovies=CountMovies()
	countMovies.feed(html)
	totalMovies=countMovies.getMovieCount()
	print(totalMovies)
	return math.ceil(totalMovies/250)


def getMovies(url):
	list=[]
	pages=getPageNumber(url);
	start=1;
	actualURL=url;
	for i in range(0,pages):
		print(actualURL)
		list=list+getMovieListFromURL(actualURL)
		print(len(list))
		time.sleep(0.2)
		start+=250
		actualURL=url+"&start="+str(start)+"&ref_=adv_nxt";
	return list;

