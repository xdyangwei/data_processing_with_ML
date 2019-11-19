from sklearn.cluster import KMeans
data=open("C:\\data.txt")
list1=[]
time=0
def k_means(data):
    clf = KMeans(n_clusters=3)
    y=clf.fit_predict(data)
    return clf.cluster_centers_,y
list2=[]
for line in data.readlines():
    list3=[]
    line_list=line.strip('\n').split()
    if(line_list[0]=="=>"):
        list3.append(line_list[2][0:-1])
        list3.append(line_list[4][0:-1])
        list2.append(list3)
    else:
        if(time==0 or line_list[0][:18]==time):
            time=line_list[0][:18]
        else:
            a,b=k_means(list2)
            list2=list(a)
            for x in list2:
                list(x).append(b)
            list1.append(list2)
            print(list2)
            list2.clear()
            time=line_list[0][:18]
    

import numpy as np
import matplotlib.pyplot as plt 
x=[n[0] for n in list1]
y=[n[1] for n in list1]
z=[n[2] for n in list1]
plt.scatter(x,y,c=z,marker="x")
plt.title("radar postion")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
