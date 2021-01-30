# -*- coding: UTF-8 -*-
import jieba
import jieba.posseg
import synonyms
import warnings
import time


def jianshu_judge(BOSS_line_review_num):  # 一个模型，用以对句子进行逐词的判断并给每个词语出现的前后关系打分，得到句子的总分
    LIST = []
    for line in BOSS_line_review_num:
        quanzhi = 0.0
        for i in range(0, len(line)):
            if i == 0 and i != len(line) - 1:
                if line[i] == '2':
                    if line[i + 1] == '1':
                        quanzhi -= 1
                    elif line[i + 1] == '0' or line[i + 1] == '2' or line[i + 1] == '3':
                        quanzhi += 1
                elif line[i] == '0':
                    quanzhi -= 0.5
            elif i == len(line) - 1 and i != 0:
                if line[i] == '2':
                    if line[i - 1] == '3':
                        quanzhi += 2
                    elif line[i - 1] == '1' or line[i - 1] == '0':
                        quanzhi -= 1
                    elif line[i - 1] == '2':
                        quanzhi += 1
                elif line[i] == '1':
                    if line[i - 1] == '3':
                        quanzhi -= 2
                    elif line[i - 1] == '0':
                        quanzhi += 1
                    elif line[i - 1] == '1' or line[i - 1] == '2':
                        quanzhi -= 1
                elif line[i] == '0':
                    quanzhi -= 0.5
            elif i != 0 and i != len(line) - 1:
                if line[i] == '2':
                    if line[i - 1] == '2' or line[i + 1] == '0' or line[i + 1] == '2' or line[i + 1] == '3':
                        quanzhi += 1
                    elif line[i - 1] == '1' or line[i - 1] == '0' or line[i + 1] == '1':
                        quanzhi -= 1
                    elif line[i - 1] == '3':
                        quanzhi += 2
                elif line[i] == '1':
                    if line[i - 1] == '2' or line[i - 1] == '1':
                        quanzhi -= 1
                    elif line[i - 1] == '3':
                        quanzhi -= 2
                    elif line[i - 1] == '0':
                        quanzhi += 1
                elif line[i] == '0':
                    quanzhi -= 0.5
            else:
                if line[i] == '0':
                    quanzhi -= 0.5
                elif line[i] == '2':
                    quanzhi += 1
                elif line[i] == '1':
                    quanzhi -= 1
                elif line[i] == '3':
                    quanzhi += 2
        if quanzhi > 0.0:
            LIST.append('2')
        elif quanzhi == 0.0:
            LIST.append('0')
        elif quanzhi < 0.0:
            LIST.append('1')
    return LIST


def write_file(file_name, LIST, flag):  # 写文件子函数
    with open(file_name, 'w') as f:
        for line in LIST:
            if flag == 1:
                f.write(str(line).replace('[', '').replace(']', '') + '\n')
            else:
                f.write(str(line) + '\n')
        f.close()


def add_contents(Line_review_num, num):  # 读入数组子函数
    Line_review_num.append(num)


def create_synonyms(LINE, dictionary_types, MAX, parameter):  # 判断相似度，找出最相似的部分
    future_add_dataset, synonyms_value_dataset = [], []
    for key in dictionary_types:
        if synonyms.compare(LINE, key, seg=True) > MAX:
            MAX = synonyms.compare(LINE, key, seg=True)
            temp = LINE
    if MAX > parameter:
        future_add_dataset.append(temp)
        synonyms_value_dataset.append(MAX)
    return future_add_dataset, synonyms_value_dataset


def create_dictionary(FILE_NAME):  # 创建字典子函数
    DICTIONARY = {}
    with open(FILE_NAME, 'r') as f:
        for line in f:
            temp = line.replace('\n', '')
            DICTIONARY[temp] = 1
        f.close()
    return DICTIONARY


if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    start = time.clock()
    boss_pos_synonyms_value, boss_neg_synonyms_value, quanzhi_list, boss_line_review_num, boss_line_dic_ele, \
    boss_line_review = [], [], [], [], [], []
    stoplist, positive_list, negative_list, degree_list, no_list = {}, {}, {}, {}, {}  # 初始化字典和数组
    stoplist = create_dictionary('./root_dic/stopword.txt')
    positive_list = create_dictionary('./update_dic/positive_deduplicate.txt')
    negative_list = create_dictionary('./update_dic/negative_deduplicate.txt')
    degree_list = create_dictionary('./update_dic/degree_deduplicate.txt')
    no_list = create_dictionary('./update_dic/no_deduplicate.txt')  # 读取指定文件并生成字典
    temp1 = []
    with open('E:/data/value/pos_8/test_pos.txt', 'r', encoding='utf-8') as f:  # 对句子进行整体切词分析
        for line in f:
            seg = jieba.posseg.cut(line.encode('GBK', 'ignore').decode('GBK'))
            temp1.append(seg)
    f.close()
    for line in temp1:
        pos_add, pos_syn, pos_dic_element, neg_add, neg_syn, neg_dic_element, d_add, d_syn, de_dic_element, n_add, n_syn, \
        no_dic_element, line_review, line_dic_ele, line_review_num = [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        positive_synonyms_value, negative_synonyms_value = 0.0, 0.0
        key_dic = {}
        for key in line:  # 逐行判断词语属性
            if key not in stoplist and key != '\n' and key != '\r\n':
                if key.flag == 'n' or key.flag == 'a' or key.flag == 'v' or key.flag == 'l' or key.flag == 'i' or key.flag == 'z' or key.flag == 'nr':
                    key_dic[key.word] = key.flag
                elif key.flag == 'd' or key.flag == 'm':
                    key_dic[key.word] = key.flag
        for key in key_dic:
            if key_dic[key] == 'n' or key_dic[key] == 'a' or key_dic[key] == 'v' or key_dic[key] == 'l' or key_dic[
                key] == 'i' or key_dic[key] == 'z' or key_dic[key] == 'nr':
                pos_add, pos_syn = create_synonyms(key, positive_list, 0.0, 0.9)
                if pos_add:
                    positive_synonyms_value += float(pos_syn[0])
                    add_contents(line_review_num, '2')
                    if pos_add[0] not in positive_list:
                        positive_list[pos_add[0]] = 1  # 满足条件的词语加入到相应词典中
                else:
                    neg_add, neg_syn = create_synonyms(key, negative_list, 0.0, 0.9)
                    if neg_add:
                        negative_synonyms_value += float(neg_syn[0])
                        add_contents(line_review_num, '1')
                        if neg_add[0] not in negative_list:
                            negative_list[neg_add[0]] = 1
            elif key_dic[key] == 'd' or key_dic[key] == 'm':
                d_add, d_syn = create_synonyms(key, degree_list, 0.0, 0.9)
                if d_add:
                    add_contents(line_review_num, '3')
                    if d_add[0] not in degree_list:
                        degree_list[d_add[0]] = 1
                else:
                    n_add, n_syn = create_synonyms(key, no_list, 0.0, 0.9)
                    if n_add:
                        add_contents(line_review_num, '0')
                        if n_add[0] not in no_list:
                            no_list[n_add[0]] = 1
        boss_pos_synonyms_value.append(positive_synonyms_value)
        boss_neg_synonyms_value.append(negative_synonyms_value)
        boss_line_review_num.append(line_review_num)
    write_file('E:/data/11dic_pos_code_quanzhi.txt', jianshu_judge(boss_line_review_num), 0)  # 写文件
    write_file('E:/data/11dic_pos_code_pos_synonyms_value.txt', boss_pos_synonyms_value, 1)
    write_file('E:/data/11dic_pos_code_neg_synonyms_value.txt', boss_neg_synonyms_value, 1)
    end = time.clock()
    print(end - start)
