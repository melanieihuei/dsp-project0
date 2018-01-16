import argparse
from pyspark import *
from pyspark.context import SparkContext
from operator import add
import string
import os
from os import walk
from os.path import join
import numpy as np
import json


# Read all the files
# ---- For Mac users,
# ---- use "sudo find / -name ".DS_Store" -depth -exec rm {} \;"
# ---- to remove all .DS_Store files.
# https://helpx.adobe.com/dreamweaver/kb/remove-ds-store-files-mac.html

def _readfile_(path):
	'''
	Read the all the files under the path.
	Result in a list f of paths of files.
	'''
	f = []
	for root, dirs, files in walk(path):
		for file in files:
			fullpath = join(root, file)
			f.append(fullpath)
	return f

def _string_(path):
	'''
	Read the paths of all files you want to read at once.
	Result in a string filename that combines all path and seperates by ','
	'''
	if len(path) > 1:
		filename = path[0]
		for i in range(len(path)-1):
			filename = filename + "," + path[i+1]
	else: filename = path
	return filename

def _adjust_(x):
	'''
	Read a words.
	Result in a word that strip out the punctutaion before or after the word. 
	'''
	x = str(x)
	if len(x) > 1:
		for punc in punctuation:
			if x.startswith(punc): x = x[1:]
			if x.endswith(punc) : x = x[:-1]
	else: x = ''
	return x

def _process_(file, punc = False, stopword = False):
	'''
	Transform the input file into a RDD with format (key, count).
	'''
	words = file.flatMap(lambda x: x.split(' ')).map(lambda x: x.lower())
	if punc:
# 		words = words.map(lambda x: _adjust_(x)).map(lambda x: _adjust_(x)).filter(lambda x: len(x)>1)
# 		words = words.map(lambda x: _adjust_(x)).filter(lambda x: len(x)>1)
		words = words.map(lambda x: _adjust_(x))
	if stopword: 
		words = words.filter(lambda x: x not in stopwords)

	words = words.filter(lambda x: x != '').map(lambda x: (x, 1)).reduceByKey(add)
# 	words = words.map(lambda x: (x, 1)).reduceByKey(add)
	counts = words.sortBy(lambda x: x[1], ascending = False).filter(lambda x: x[1] > 2)		
	return counts

def _fillna_(x):
	'''
	Read an array.
	Result in an numpy.array that transform all 'None' into float values 0.
	'''
	x = np.array(x)
	for i in range(len(x)):
		if x[i] == None: x[i] = 0.
	x = np.asarray(x, dtype = np.float64)
	return x
	
def _IDF_(x, N):
	'''
	Calculate IDF value with inputting (word, np.array).
	'''
	tf = x[1:]
	num = np.zeros((len(tf),))
	for i in range(len(tf)):
		if x[i+1] != 0: num[i] = 1
	n = num.sum()
	idf = np.log([N/n])
	v = np.array(np.append(idf, tf))
	return v

def _TFIDF_(files, books):
	'''
	 files: the file list of the books
	 books: the count of all words in all books
	Calculate TF-IDF value with inputting (word, np.array)
	Result in the format (word, np.array(tf-idf_values))
	'''
	N = len(files) - 1
	for b in range(N):
		book = _process_(sc.textFile(files[b]), punc = True, stopword = False)
		if b < 1:
			tf = books.leftOuterJoin(book)
		else:
			tf = tf.leftOuterJoin(book).map(lambda x: (x[0], (x[1][0] + (x[1][1],))))
	tf = tf.map(lambda x: (x[0], _fillna_(x[1])))
	idf = tf.map(lambda x: (x[0], _IDF_(x[1], N)))
	tfidf = idf.map(lambda x: (x[0], x[1][0]*x[1][1:]))
	return tfidf


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "Project 0", 
		epilog = "CSCI 8360 Data Science Practicum, Spring 2018",
		add_help = "How to use",
		prog = "spark-submit project0.py -p <files-path> [optional args]")
		
	# Required args
	parser.add_argument("-p", "--path", required = True, 
		help = "Path to all input text files")
		
	# Optional args
	parser.add_argument("-n", "--topfreq", default = 40, type = int, 
		help = "Number of the top frequent words. [Default: 40]")
	parser.add_argument("-t", "--topTFIDF", default = 5, type = int, 
		help = "Number of the top words with largest TF-IDF values. [Default: 5]")
	parser.add_argument("-a", "--sp1", default = True, type = bool,
		help = "Option of processing subproject a. [Default: True]")
	parser.add_argument("-b", "--sp2", default = True, type = bool,
		help = "Option of processing subproject b. [Default: True]")
	parser.add_argument("-c", "--sp3", default = True, type = bool,
		help = "Option of processing subproject c. [Default: True]")
	parser.add_argument("-d", "--sp4", default = True, type = bool,
		help = "Option of processing subproject d. [Default: True]")
		
	args = vars(parser.parse_args())
	
	# Read in the variables
	mypath = args['path']
	n = args['topfreq']
	t = args['topTFIDF']
	sp1 = args['sp1']
	sp2 = args['sp2']
	sp3 = args['sp3']
	sp4 = args['sp4']

	# Read in the data
	f = _readfile_(mypath)
	
	sc = SparkContext()
	f1 = sc.textFile(_string_(f[:-1])) # files
	f2 = sc.textFile(f[-1]) # stopwords
	stopwords = f2.collect()
# 	punctuation = [".", ",", ":", ";", "'", "!", "?", '"', "-", "--", "—", "_", "...", 
# 					")", "(", "]", "[", ]
# 	punctuation = string.punctuation
	punctuation = [".", ",", ":", ";", "'", "!", "?"]
	

	os.makedirs(mypath + "output/")
	# subproject a
	if sp1:
		counts_a = _process_(f1, punc = False, stopword = False)
		top40_a = counts_a.take(n)
		json.dump(dict(top40_a), open(mypath + "output/sp1.json", "w"))

	## subproject b
	if sp2:
		counts_b = _process_(f1, punc = False, stopword = True)
		top40_b = counts_b.take(n)
		json.dump(dict(top40_b), open(mypath + "output/sp2.json", "w"))

	## subproject c
	if sp3:
		counts_c = _process_(f1, punc = True, stopword = True)
		top40_c = counts_c.take(n)
		json.dump(dict(top40_c), open(mypath + "output/sp3.json", "w"))

	## subproject d
	if sp4:
		counts = _process_(f1, punc = True, stopword = False)
		tfidf = _TFIDF_(f, counts)
		top5 = list()
		for b in range(len(f)-1):
			top = tfidf.sortBy(lambda x: x[1][b], ascending = False).map(lambda x: (x[0], x[1][b])).take(t)
			top5.extend(top)
		json.dump(dict(top5), open(mypath + "output/sp4.json", "w"))

