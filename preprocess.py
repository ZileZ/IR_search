# 载入停用词表
#
# 主要思想是分词过后，遍历一下停用词表，去掉停用词。
import jieba

#判断是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def clean_list(seg_list):
    cleaned_dict = {}
    n = 0
    stopwords = stopwordslist('stopWords/1893（utf8）.txt')  # 这里加载停用词的路径
    for i in seg_list:
        i = i.strip().lower()
        if i != '' and not is_number(i) and i not in stopwords:
            n = n + 1
            if i in cleaned_dict:
                cleaned_dict[i] = cleaned_dict[i] + 1
            else:
                cleaned_dict[i] = 1
    return n, cleaned_dict


# 对句子进行分词
def seg_sentence(sentence):
    # print(sentence)
    seg_list = jieba.lcut(sentence, cut_all=False)
    ld, cleaned_dict = clean_list(seg_list)
    return ld, cleaned_dict

#
# inputs = open('input/environment.txt', 'r', encoding='utf-8')
#
# # outputs = open('output/a2.txt', 'w',encoding='utf-8')
# n = 0
# for line in inputs:
#     line_seg = seg_sentence(line)  # 这里的返回值是字符串
#     outputs = open('output/a'+str(n)+'.txt', 'w',encoding='utf-8')
#     outputs.write(line_seg)
#     outputs.close()
#     n += 1
# inputs.close()