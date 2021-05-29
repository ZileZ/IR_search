import numpy as np

indexpath = 'index/index_total.npy'
fileindex_path = 'index/file_index.npy'

index_list = np.load(indexpath, allow_pickle=True)
index_list = index_list.tolist()
fileindex_list = np.load(fileindex_path, allow_pickle=True)
fileindex_list = fileindex_list.tolist()

#得到先前建立的文档id
def get_num(file_str):
    return fileindex_list[file_str]

#AND操作
def bool_and(index_list1, index_list2):
    # print(index_list1,index_list1)
    answer = []
    i = 0
    j = 0
    #合并倒排记录表（AND）
    while i < len(index_list1) and j < len(index_list2):
        # print(index_list1[i],index_list2[j])
        index_i = get_num(index_list1[i])
        index_j = get_num(index_list2[j])
        # print(index_i, index_j)
        if index_i == index_j:
            answer.append(index_list1[i])
            i += 1
            j += 1
        elif index_i < index_j:
            i += 1
        else:
            j += 1
    return answer

def bool_or(index_list1, index_list2):
    answer = []
    i = 0
    j = 0
    # 合并倒排记录表（OR）
    while i < len(index_list1) and j < len(index_list2):
        # print(index_list1[i], index_list2[j])
        index_i = get_num(index_list1[i])
        index_j = get_num(index_list2[j])
        # print(index_i, index_j)
        if index_i == index_j:
            answer.append(index_list1[i])
            i += 1
            j += 1
        elif index_i < index_j:
            answer.append(index_list1[i])
            i += 1
        else:
            answer.append(index_list2[j])
            j += 1
    while i < len(index_list1):
        answer.append(index_list1[i])
        i += 1
    while j < len(index_list2):
        answer.append(index_list2[j])
        j += 1
    return answer
#
# str_list1 = '劣质'
# str_list2 = '房间'
#
# index1 = index_list[str_list1][1]
# index2 = index_list[str_list2][1]
# a = bool_or(index1, index2)
# print(a)