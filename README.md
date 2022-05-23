# fastspeech2 with aishell3 training and dataset stuff

generated aishell3 content.txt and label_train-set.txt from magicdata trans.txt  
MFA align procedure for your own dataset  


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

### 1. resample if your own audio file is not same with aishell3 channels: 1(mono), Audio sample rate:44.100kHZ
```
./resample.py source_audio_file_path/ target_file_path/
```	

### 2. install MFA env to align your audio files
```
conda create -n aligner -c conda-forge montreal-forced-aligner
```	

### 3. get the full lexicon for later use
```
./gen_lexicon.py
```	


### transform to label_train-set
```
 ./transform_trans_to_label_train-set.py TRANS.txt  
 label_train-set.txt will be generated at the current folder.  
 requirement: pip install pypinyin
              pip install jieba
```			  
### transform to content
```
 ./transform_trans_to_content.py TRANS.txt  
 content.txt will be generated at the current folder.  
 requirement: pip install pypinyin
```

### MFA align
```
 conda create -n aligner -c conda-forge montreal-forced-aligner
 gen_lexicon.py  --> output.lexicon.txt this will include all the lexicon
 you can double check your words list if all in output.lexicon.txt use check_pinyin_in_lexicon_or_not.py
 update config/AISHELL3/preprocess.yaml, lexicon_path: "lexicon/output.lexicon.txt"
 python3 prepare_align.py config/AISHELL3/preprocess.yaml
 mfa validate FastSpeech2/raw_data/AISHELL3/ FastSpeech2/lexicon/output.lexicon.txt
 mfa train FastSpeech2/raw_data/AISHELL3/ FastSpeech2/lexicon/output.lexicon.txt FastSpeech2/acoustic_model/new_acoustic_model.zip FastSpeech2/preprocessed_data/AISHELL3/TextGrid/
```


## License

[MIT © Evers Chen.](LICENSE)
