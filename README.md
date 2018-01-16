# melanieihuei-p0

The repository contains all works of project 0 of CSCI 8360 Data Science Practicum for Srping 2018.

## Introduction

This project is to implement a basic word counter in Apache Spark and result in a customized word-count dictionary. According to the books inputted, the word counter will detect the words, record the corresponding counts, elminate the stopwords, filter out the punctuations, and provide the top `N` most frequent words in a dictionary. Otherwise, depends on the TF-IDF of each specific word, the counter will also produce the top `n` words with highest TF-IDF scores. 

## Datasets

For the example datasets used in this case, the producer is using freely available data from [Project Guenberg](https://
www.gutenberg.org/). The list of specific 8 books showed as follows:

⋅⋅1. *Pride and Prejudice*, by Jane Austen
⋅⋅2. *Alice's Adventures in Wonderland*, by Lewis Carroll
⋅⋅3. *Ulysses*, by James Joyce
⋅⋅4. *Leviathan*, by Thomas Hobbes
⋅⋅5. *The Iliad*, by Homer
⋅⋅6. *The War of the Worlds*, by H.G. Wells
⋅⋅7. *The Republic*, by Plato
⋅⋅8. *Little Women*, by Louisa May Alcott

You can download them via the website, or the files are already uploaded in this Github.

## Tools
- [Python 3.6](https://www.python.org/downloads/release/python-360/)
- [Anaconda](https://www.anaconda.com/)
- [Apache Spark 2.2.1](http://spark.apache.org/)
- [Pyspark 2.2.1](https://pypi.python.org/pypi/pyspark/2.2.1)

## Create Counter


