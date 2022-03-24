import re
import jsonlines

data = []
result = []
with open("dataset/data.jsonl", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        data.append(item['code'])
        # print(item['code'])
i=0
j=0
file=open("datajsonl.txt","w",encoding="utf8")

for i in range(len(data)):
    data_result = re.split('\n', data[i])
    for j in range(len(data_result)):
        result.append(data_result[j].strip('\t'))
    j=0
    data_result = ''.join(result)
    file.write(str(data_result))
    file.write('\n')
    result=[]
