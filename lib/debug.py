#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    author1 = Author('Adam')
    author2 = Author('Betty')
    author3 = Author('Charles')
    magazine1 = Magazine('Vogue', 'Fashion')
    magazine2 = Magazine('Teen Beat', 'Pop Culture')
    magazine3 = Magazine('Better Homes', 'Architecture')
    article1 = Article(author1, magazine1, 'Move, Bitch')
    article2 = Article(author1, magazine1, 'Stop, Bitch')
    article3 = Article(author1, magazine2, 'Your Wig is Under Arrest')
    article4 = Article(author2, magazine1, 'Clubbing for Seals')


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
