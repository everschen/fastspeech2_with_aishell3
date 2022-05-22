#!/usr/bin/python3

import sys
import os
import re


if __name__ == '__main__':
    lexicon = []
    #print("reading from :", sys.argv[1])
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            line = re.split('\t| ', line)
            lexicon.append(line[0])

    print("lexicon len=",len(lexicon))

    with open(sys.argv[2], "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            line = re.split('\t| ', line)
            for i in range(len(line)):
                if line[i].strip() == "":
                    continue
                if line[i] not in lexicon:
                    print("not in lexicon:", line[i])
                else:
                    pass
                    #print("in lexicon:", line[i])
            #break
    exit(0)
    

    

    
