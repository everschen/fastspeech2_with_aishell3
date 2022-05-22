#!/usr/bin/python3
# usage
# ./transform_trans_to_label_train-set.py TRANS.txt
# label_train-set.txt will be generated at the current folder.
# requirement: pip install pypinyin
#              pip install jieba



import sys
import os
import re
from pypinyin import pinyin, lazy_pinyin, Style
import jieba

if __name__ == '__main__':


    if (len(sys.argv)==2):
        with open(sys.argv[1], "r") as f:
            file_content = "label_train-set.txt"
            fw = open(file_content, "w")            
            skip_first_line = True
            for line in f.readlines():
                print(line)
                if skip_first_line:
                    skip_first_line = False
                    continue
                texts = re.split(' |\t', line)
                chinese = texts[2].replace("\n", "")
                
                print(len(chinese))

                
                filename = texts[0].replace(".wav", "")
                chn_list = jieba.cut(chinese)
                chn_ret = "%".join(chn_list)
                result = lazy_pinyin(chn_ret, style=Style.TONE3, neutral_tone_with_five=True)
                #pinyin_list = jieba.cut(result)
                ret = ""
                for i in range(len(result)):
                    ret +=result[i] + " "
                
                fw.write(filename + "|" + ret + "$|" + chn_ret + "$\n")
                print(texts)
            fw.close()
