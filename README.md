# fastspeech2 with own aishell3 dataset

There's lot's of issues you will meet if you want to train your own audio with aishell3, here provide a summary and solution to it. 


## Table of Contents

- [Background](#background)
- [Usage](#usage)
- [License](#license)




## Background
```
There's lot's of issue when build own dataset, so here do some summary for it.
for fastspeech2 you can refer to https://github.com/ming024/FastSpeech2
```


## Usage

### 1. in case your dataset is in magicdata format, you can transform to label_train-set
```
 ./transform_trans_to_label_train-set.py TRANS.txt  
 label_train-set.txt will be generated at the current folder.  
 requirement: pip install pypinyin
              pip install jieba
```	

### 2. in case your dataset is in magicdata format, you can transform to content
```
 ./transform_trans_to_content.py TRANS.txt  
 content.txt will be generated at the current folder.  
 requirement: pip install pypinyin
```


### 3. resample if your own audio file is not same with aishell3 channels: 1(mono), Audio sample rate:44.100kHZ
```
./resample.py source_audio_file_path/ target_file_path/
```	

### 4. install MFA env to align your audio files
```
conda create -n aligner -c conda-forge montreal-forced-aligner
```	

### 5. in case lexicon/pinyin-lexicon-r.txt can't cover your words, get the full output.lexicon.txt and output.symbols and put output.lexicon.txt to lexicon folder, otherwise just skip this step.
```
./generate_lexicon.py --with-tone --with-r output

you can double check if all your words are in output.lexicon.txt use check_pinyin_in_lexicon_or_not.py, you may find some dataset error if not.
./check_pinyin_in_lexicon_or_not.py output.lexicon.txt pinyin.txt
./check_pinyin_in_lexicon_or_not.py pinyin-lexicon-r.txt pinyin.txt
```	

### 6. in case lexicon/pinyin-lexicon-r.txt can't cover your words, and you need to use generated output.lexicon.txt, update lexicon_path of config/AISHELL3/preprocess.yaml to "lexicon/output.lexicon.txt"
```
update lexicon_path of config/AISHELL3/preprocess.yaml
```	


### 7. do prepare_align.py to prepare raw_data\AISHELL3\
```
python3 prepare_align.py config/AISHELL3/preprocess.yaml 
```	

### 8. do mfa validate for your raw data and lexicon
```
conda activate aligner
mfa validate FastSpeech2/raw_data/AISHELL3/ FastSpeech2/lexicon/output.lexicon.txt
```	

### 9. do mfa train to generate TextGrid and acoustic model
```
mfa train FastSpeech2/raw_data/AISHELL3/ FastSpeech2/lexicon/output.lexicon.txt FastSpeech2/acoustic_model/new_acoustic_model.zip FastSpeech2/preprocessed_data/AISHELL3/TextGrid/
conda deactivate
```	

### 10. do preprocess.py (need GPU)
```
python3 preprocess.py config/AISHELL3/preprocess.yaml
```	

### 11. do train.py (need GPU)
```
python3 train.py -p config/AISHELL3/preprocess.yaml -m config/AISHELL3/model.yaml -t config/AISHELL3/train.yaml
```	

### 12. correction to aishell3
jv4 --> ju4  
din4 --> ding4


## License

[MIT © Evers Chen.](LICENSE)
