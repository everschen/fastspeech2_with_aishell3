#!/usr/bin/python3

import sys
import os
import re
from phonemizer.backend import EspeakBackend
from phonemizer.punctuation import Punctuation
from phonemizer.separator import Separator


if __name__ == '__main__':
    my_txt = ""
    #print("reading from :", sys.argv[1])
    with open(sys.argv[1], "r") as f:
        text = f.read().splitlines()
        
        # remove all the punctuation from the text, considering only the specified
        # punctuation marks
        text = Punctuation(';:,.!"?()-').remove(text)

        # build the set of all the words in the text
        words = {w.lower() for line in text for w in line.strip().split(' ') if w}
        # initialize the espeak backend for English
        backend = EspeakBackend('cmn')

        # separate phones by a space and ignoring words boundaries
        separator = Separator(phone=' ', word=None)

        # build the lexicon by phonemizing each word one by one. The backend.phonemize
        # function expect a list as input and outputs a list.
        lexicon = {
            word: backend.phonemize([word], separator=separator, strip=True)[0]
            for word in words}
        print(lexicon)
    
    exit(0)
    

    

    
