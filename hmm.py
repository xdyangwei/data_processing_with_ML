from hmmlearn.hmm import GaussianHMM
import numpy as np
import math
data=open("C:\\transfer_data.txt")
data=data.readlines()
sample=[]
for index in range(len(data)):
    sample1=[]
    if(index!=0):
        sample1.append((float)(data[index].split()[0])-(float)(data[index-1].split()[0]))
        sample1.append((float)(data[index].split()[1])-(float)(data[index-1].split()[1]))
        sample.append(sample1)
# for x in sample:
#     print(x[0],x[1])
n=8
model=GaussianHMM(n_components=n,n_iter=100).fit(sample)
x=model.predict(sample)
for result in range(len(x)):
    print(x[result],sample[result])
