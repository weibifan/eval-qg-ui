

from itertools import islice
import re
import sys
import json
import os
import spacy
# 需要很长时间，且经常失败
# C:\Users\Wei\.conda\envs\env-web-torch\Lib\site-packages\en_core_web_sm
# 由于JS捕获输出，这个文件不要随便加print
# print('loading model start ....')
spacy_nlp = spacy.load('en_core_web_sm')
# print('loading model end')
# 等待命令行读取，阻塞式，且以^Z为结束，ctrl+z
# print('stdin=', sys.stdin.readlines()[0])
file_name = json.loads(sys.stdin.readlines()[0])
# print(file_name)
'''
file_name="A computer is a digital electronic machine that can be programmed to carry out sequences of arithmetic or logical operations (computation) automatically. 
Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. 
A computer system is a complete computer that includes the hardware, operating system (main software), and peripheral equipment needed and used for full operation. 
This term may also refer to a group of computers that are linked and function together, such as a computer network or computer cluster.   
The above text is from the website of Wikipedia."
'''
# 下面3句很迷惑，分词，然后又连接起来。
doc = spacy_nlp(file_name)
tokens = [token.text for token in doc]
input = " ".join(tokens)

# 将字符串分成字母。
split_txt = re.split('\s*',input)

i=0
count = 0
res=''
res_sen = []
flag = 0
temp_i=[0]
while(i<len(split_txt)):
    if(count>199):
        if((i+100) < len(split_txt)):
            j_range = i+100
        else:
            j_range = len(split_txt)-1
        for j in range(i,j_range):
            r = re.search(r'.*\.',split_txt[j])
            if(r):
                res = res + split_txt[j]
                res_sen.append(res)
                res=''
                count = 0
                temp_i[0]=j
                flag = 1
                break
            else:
                res = res + split_txt[j] + ' '
                count += 1
    else:
        res = res + split_txt[i] + ' '
        count += 1
    if(flag==1):
        i=temp_i[0]
        flag=0
    i+=1

if (res):
    res_sen.append(res)
res_file = '\n'.join(res_sen)

# data = json.dumps(res_file,ensure_ascii=False)
print(res_file)
sys.stdout.flush()
# res_file_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/qg_para/inp_para.txt'
# with(open(res_file_name,'w')) as f:
#    f.write(res_file.lower())
