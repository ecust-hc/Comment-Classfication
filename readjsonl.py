import re
import jsonlines

data = []
result = []
#读取jsonl文件中代码
# with open("dataset/data.jsonl", "r+", encoding="utf8") as f:
#     for item in jsonlines.Reader(f):
#         data.append(item['code'])
#         # print(item['code'])
# i=0
# j=0
# file=open("datajsonl.txt","w",encoding="utf8")
#
# for i in range(len(data)):
#     data_result = re.split('\n', data[i])
#     for j in range(len(data_result)):
#         result.append(data_result[j].strip('\t'))
#     j=0
#     data_result = ''.join(result)
#     file.write(str(data_result))
#     file.write('\n')
#     result=[]



description=[]
with open("dataset/data.jsonl", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        # data.append(item['sdoc'])
        print(item['doc'] + ':' )
        # if item['sdoc']['returns'] != '':
        #     print('@return后为该注释存在返回值这个类别')
        # if item['sdoc']['params'] != '':
        #     print('@param后为该注释存在参数说明这个类别')
        # if item['sdoc']['exceptions'] != {}:
        #     print('@exceptions后为该注释存在异常说明这个类别')
        if item['sdoc']['description'] == '':
            item['sdoc']['description']='null'
            print( '该注释不需要进一步分类')
        description.append(item['sdoc']['description'])
        # print(item['sdoc']['description'])
        # print(type(item['sdoc']))
# print(description)

i=0
j=0
file=open("description.txt","w",encoding="utf8")

for i in range(len(description)):
    data_result = re.split('\n', description[i])
    for j in range(len(data_result)):
            result.append(data_result[j].strip('\t'))
    j=0
    data_result = ''.join(result)
    file.write(str(data_result))
    file.write('\n')
    result=[]
