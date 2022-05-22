# fastspeech2 with aishell3 training and dataset stuff

generated aishell3 content.txt and label_train-set.txt from magicdata trans.txt

## Table of Contents

- [Security](#security)
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Contributing](#contributing)
- [License](#license)

## Security

### Any optional sections

## Background
```
There's lot's of issue when build own dataset, so here do some summary for it.
```

## Install

This module depends upon a knowledge of [Markdown]().

```
```

### Any optional sections

## Usage

### transform to label_train-set
 ./transform_trans_to_label_train-set.py TRANS.txt
 label_train-set.txt will be generated at the current folder.
 requirement: pip install pypinyin
              pip install jieba
			  
### transform to content
 ./transform_trans_to_content.py TRANS.txt
 content.txt will be generated at the current folder.
 requirement: pip install pypinyin



## API

### Any optional sections

## More optional sections

## Contributing



### Any optional sections

## License

[MIT © Evers Chen.](../LICENSE)