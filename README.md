# melanieihuei-p0

The repository contains all works of project 0 of CSCI 8360 Data Science Practicum for Srping 2018.

## Introduction

This project is to implement a basic word counter in Apache Spark and result in a customized word-count dictionary. According to the books inputted, the word counter will detect the words, record the corresponding counts, elminate the stopwords, filter out the punctuations, and provide the top `N` most frequent words in a dictionary. Otherwise, depends on the TF-IDF of each specific word, the counter will also produce the top `n` words with highest TF-IDF scores. 

## Datasets

For the example datasets used in this case, the producer is using freely available data from [Project Guenberg](https://
www.gutenberg.org/). The list of specific 8 books showed as follows:

  1. *Pride and Prejudice*, by Jane Austen
  2. *Alice's Adventures in Wonderland*, by Lewis Carroll
  3. *Ulysses*, by James Joyce
  4. *Leviathan*, by Thomas Hobbes
  5. *The Iliad*, by Homer
  6. *The War of the Worlds*, by H.G. Wells
  7. *The Republic*, by Plato
  8. *Little Women*, by Louisa May Alcott

You can download them via the website, or the files are already uploaded in this Github.

## Tools
- [Python 3.6](https://www.python.org/downloads/release/python-360/)
- [Anaconda](https://www.anaconda.com/)
- [Apache Spark 2.2.1](http://spark.apache.org/)
- [Pyspark 2.2.1](https://pypi.python.org/pypi/pyspark/2.2.1)

## Word Counter

### 1. Arguments for Command-Lines

Run the code `p0.py` in your terminal. There are few notes before running it:

#### For Mac (OS X System) Users:

Go into the directory where you put your datasets (files) in (which will be the path that you call later). 

`.DS_Store` files are automatically created by Mac OS X Finder in browsed directories, which is not visible when you are using GUI. Check the article [here](https://helpx.adobe.com/dreamweaver/kb/remove-ds-store-files-mac.html) for further information. You'll have to delete it before running the code since it confilcts with the python package `os` we used. 

Run the code in terminal under the target directory:

```
sudo find / -name ".DS_Store" -depth -exec rm {} \;
```

You'll have to type in your machine's password to process `sudo` command.

#### Run the word counter in Terminal:

You are able to start [Pyspark](https://pypi.python.org/pypi/pyspark/2.2.1) by type in the path where you put your `pyspark`, however, running `.py` script in [Pyspark](https://pypi.python.org/pypi/pyspark/2.2.1), you'll need `spark-submit`.

Run the code in terminal by following command-line:

```
/bin/spark-submit csci8360/p0.py -p ~/csci8360/p0/
```
where




### 2. Subprojects Selection
 
 1. Subproject a
    
    This is just testing
    if it doesn't work?
    
 2. Subproject b
 
 3. Subproject c
 
 4. Subproject d
