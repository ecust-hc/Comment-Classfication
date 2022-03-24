# Comment-category
Base on the paper of Why My Code Summarization Model Does Not Work: Code Comment Improvement with Category Prediction,I classfier my own data

论文地址：https://dl.acm.org/doi/10.1145/3434280

# Requirements

本人运行论文中的源码是在Anaconda环境下创建虚拟环境,使用pytorch，python==3.8。缺少的第三方包按照requirement是.txt上的版本进行下载。

# Run

cccpm.py clf --classifier=rf classifier可以选择rf(Random Forest),navie(Naïve Bayes),dt(Decision Tree),lgbm(LightGBM).运行的结果就是评估不同模型在cross_validate交叉验证下的模型效果。

cccpm.py eval --classifier=rf classifier可以选择rf(Random Forest),navie(Naïve Bayes),dt(Decision Tree),lgbm(LightGBM).运行的结果就是 将数据集训练完成的模型来预测自己数据集代码的类型。

# Dataset

论文作者使用https://github.com/xing-hu/EMSE-DeepCom中的数据集来训练自己的模型，并通过人工标记20000条数据来训练分类模型。
