#!/usr/bin/python3

import sys
import os
import re


if __name__ == '__main__':
    my_txt = ""
    #print("reading from :", sys.argv[1])
    with open(sys.argv[1], "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            line = re.split('\t| ', line)
            for i in range(len(line)):
                if i % 2 == 0 and i != 0:
                    my_txt += line[i]+ " "
            print(my_txt)
            my_txt = ""

    
    exit(0)
    

    

    
