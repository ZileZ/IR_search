from bool_search import bool_and, bool_or
from search import Stack

import sys
import numpy as np

indexpath = 'index/index_total.npy'
index_list = np.load(indexpath, allow_pickle=True)
index_list = index_list.tolist()


def word_exist(word):
    if word == 'and' or word == 'or':
        return True
    elif word not in index_list.keys():
        print(r'"' + word + r'"不存在！')
        return False
    else:
        return True


# 判断词表是否重复
def judge_exist(word_list, word):
    for word_n in word_list:
        if word == word_n:
            return True
    return False


#处理AND OR的优先级
def process_symbol(sentence):
    word_list = Stack()
    symbol_list = Stack()
    for i,word in enumerate(sentence):
        word = str(word).lower()
        if not word_exist(word):
            return []
        now_list = index_list[word][1] #当前单词的文档列表

        if word == 'and' or word == 'or':
            symbol_list.push(word)

        else:
            word_list.push(now_list)
            if(symbol_list.top() == 'and'):
                list_1 = word_list.pop()
                list_2 = word_list.pop()
                list_result = bool_and(list_1,list_2)
                word_list.push(list_result)
                symbol_list.pop()
    while not symbol_list.is_empty():
        list_1 = word_list.pop()
        list_2 = word_list.pop()
        list_result = bool_or(list_1,list_2)
        word_list.push(list_result)
        symbol_list.pop()
    return word_list.pop()




# print(sys.argv)
result = process_symbol(sys.argv[1:])
if result == []:
    print("There is no file!")
else:
    print(result)
