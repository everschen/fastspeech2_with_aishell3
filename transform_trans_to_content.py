#!/usr/bin/python3
# usage
# ./transform_trans_to_content.py TRANS.txt
# content.txt will be generated at the current folder.
# requirement: pip install pypinyin



import sys
import os
import re
from pypinyin import pinyin, lazy_pinyin, Style

if __name__ == '__main__':
    if (len(sys.argv)==2):
        with open(sys.argv[1], "r") as f:
            file_content = "content.txt"
            fw = open(file_content, "w")            
            skip_first_line = True
            for line in f.readlines():
                print(line)
                if skip_first_line:
                    skip_first_line = False
                    continue
                texts = re.split(' |\t', line)
                chinese = texts[2].replace("\n", "")
                ret = lazy_pinyin(chinese, style=Style.TONE3, neutral_tone_with_five=True)
                print(len(ret),len(chinese))
                result = ""
                for i in range(len(ret)):
                    if i == 0 :
                        result += "\t" + chinese[i] + " " + ret[i]
                    else:
                        result += " " + chinese[i] + " " + ret[i]
                fw.write(texts[0] + result + "\n")
                print(texts)
            fw.close()
