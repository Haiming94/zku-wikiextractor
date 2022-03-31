# -*- coding: utf-8 -*-
"""
"""
from opencc import OpenCC
import logging
import datetime

zhwiki2File = '/home/wuhaiming/data/wiki/zh/extracted/AA/zhwiki.txt' #中文维基百科数据最终版
zhwikichsFile = '/home/wuhaiming/data/wiki/zh/extracted/AA/zhwiki-chs.txt' #繁体字转成简体字后的中文百科数据

def t2s():
    cc = OpenCC('t2s')  # convert from Traditional Chinese to Simplified Chinese
    with open(zhwiki2File, encoding='utf-8') as fr:
        for line in fr:
            #to_convert = '香菸（英語：Cigarette），爲菸草製品的一種。滑鼠是一種很常見及常用的電腦輸入裝置。'
            converted = cc.convert(line)
            print(converted) 
            with open(zhwikichsFile, 'a', encoding='utf-8') as fw:
                fw.write(converted)

if __name__ == '__main__':
    program = "zku_cleanZhwiki.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))
    # 开始运行时间
    starttime = datetime.datetime.now()
    print("程序开始运行时间：" + str(starttime))
    t2s()
    print('程序运行结束...')
    # 结束运行时间
    endtime = datetime.datetime.now()
    print("程序结束运行时间：" + str(endtime))
    # 运行时间
    runAllTime = endtime - starttime
    print("程序运行时长：" + str(runAllTime))
