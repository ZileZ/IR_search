import os
import numpy as np
from preprocess import seg_sentence

filepath = 'output'
indexpath = 'index'
news_list = {}
file_list = {}

#写索引
def write_index(fpath, context):
    a = np.array(context)
    np.save(os.path.join(fpath),a)

#建立文档索引
def construct_lists(filepath):
    files = os.listdir(filepath)
    # print(files)
    num = 0
    for i in files:
        #对每一个文档给一个id，从1开始
        file_list[i] = num
        num += 1
        #建立文档索引，对每个词储存出现次数和出现文档
        with open(os.path.join(filepath,i),'r',encoding ='utf-8') as f:
            context = f.read()
        ld, cleaned_dict = seg_sentence(context)
        for key, value in cleaned_dict.items():
            if key in news_list:
                news_list[key][0] = news_list[key][0] + 1  # df++
                news_list[key][1].append(i)
            else:
                news_list[key] = [1, [i]]  # [df, [file]]

    # print(file_list)
    write_index(os.path.join(indexpath,'index_total.npy'), news_list)
    write_index(os.path.join(indexpath,'file_index.npy'), file_list)
construct_lists(filepath)
# print(news_list)
