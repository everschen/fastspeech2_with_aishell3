#!/usr/bin/python3

import sys
import os
import re
import cn2an

import requests
import csv
from pydub import AudioSegment
import shutil
import time




if __name__ == '__main__':


    file_list = os.listdir("SSB1988")

    

    #print(file_list)


    for file in file_list:
        print(file)
        new_name = "SSB1988"+file[17:]
        print("mv SSB1988/%s to SSB1988/%s"%(file, new_name))
        os.system("mv SSB1988/%s SSB1988/%s"%(file, new_name))
    
    print(len(file_list))
    exit(0)
    

    

    
