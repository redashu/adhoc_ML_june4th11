#!/usr/bin/python3

from  bs4  import  BeautifulSoup
from  nltk.corpus  import  stopwords
import  urllib.request
import nltk
#  reading data from  URL 
web=urllib.request.urlopen('https://php.net')
#  print  html taged  data
webdata=web.read()
#  applying  Soup  
souped=BeautifulSoup(webdata,'html5lib')
#  only  text extraction 
text_data=souped.get_text()
#print(text_data)
#  tokenize process on behalf of words without stop words 
tokenized1=[i for i  in   text_data.split() if i.lower() not in stopwords.words('english') ]
print(len(tokenized1))

#  applying  freq counter
word_count=nltk.FreqDist(tokenized1)
word_count.plot(20)





