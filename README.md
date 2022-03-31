# zku-wikiextractor

一个解析zhwiki数据的个人工具库

### 数据下载网址：
https://dumps.wikimedia.org/zhwiki/latest/

### 解析注意事项：

- 解析代码：https://github.com/attardi/wikiextractor/tree/v3.0.4

- 版本说明：python3.4,  wikiextractor 3.0.4（最新版报错）

- 修改 WikiExtractor.py：修改引用方式

``` Python
from .extract import Extractor, ignoreTag, define_template, acceptedNamespaces
改为
from extract import Extractor, ignoreTag, define_template, acceptedNamespaces
```

### 最终运行:
```Bash
# download wikiextractor 3.0.4 from https://github.com/attardi/wikiextractor/tree/v3.0.4

unzip wikiextractor-3.0.4.zip

cd wikiextractor-3.0.4

python setup.py install

cd wikiextractor

export LC_ALL="en_US.utf8" # just for Chinese server

PYTHONIOENCODING=ascii python WikiExtractor.py -b 3500M -o [output dir path] [input file path, .bz2 or .xml]
PYTHONIOENCODING=ascii python WikiExtractor.py -b 3500M -o ../../zh/extracted ../../zh/zhwiki-latest-pages-articles.xml

# 清洗
python zku_cleanWiki.py

# 繁体转简体
pip install opencc
python zku_t2s.py

# 分词
pip install jieba
python zku_buildSegDict.py
python zku_segSentence.py
```

### 参考：
- [CSDN](https://blog.csdn.net/weixin_34001430/article/details/94267243)

- [Github](https://github.com/CodeManYep/ZhWikiCorpus)
