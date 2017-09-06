from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

def removeStop(text):
	#text = 'hello bye the the hi'
	text = ' '.join([word for word in text.read().split() if word not in cachedStopWords])
	text_file = open("Output.txt", "w")
	text_file.write("%s" % text)
	text_file.close()

text = open('abs.txt','r')

removeStop(text)