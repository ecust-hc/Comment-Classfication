
import pandas as pd

#读标签列
# Label = pd.read_excel(io='dataset/data_set.xlsx',usecols="C")
# print(Label)
# i=0
# file=open("label.txt","w")
# for i in range(Label.shape[0]):
#     file.write(str(Label.iloc[i].values))
#     file.write('\n')


#读代码列
# code = pd.read_excel(io='dataset/data_set.xlsx',usecols="A")
# print(code)
# i=0
# file=open("code.txt","w")
# for i in range(code.shape[0]):
#     file.write(str(code.iloc[i].values))
#     file.write('\n')


#读注释列
nl = pd.read_excel(io='dataset/data_set.xlsx',usecols="B")
print(nl)
i=0
file=open("nl.txt","w")
for i in range(nl.shape[0]):
    file.write(str(nl.iloc[i].values))
    file.write('\n')
