from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor
import numpy as np
import matplotlib.pyplot as plt 
data=open("C:\\data.txt")
list1=[]
time=0
def k_means(data):
    x=min(3,len(data))
    clf = KMeans(n_clusters=int(x))
    y=clf.fit_predict(data)
    return clf.cluster_centers_,y
list2=[]
data.readline()
first=data.readline()
prev_x=first.strip('\n').split()[2][0:-1]
prev_y=first.strip('\n').split()[4][0:-1]
print(prev_x,prev_y)
for line in data.readlines():
    list3=[]
    line_list=line.strip('\n').split()
    if(line_list[0]=="=>"):
        #print(line_list[2][0:-1],line_list[4][0:-1],abs(float(line_list[2][0:-1])-float(prev_x)),abs(float(line_list[4][0:-1])-float(prev_y)))
        # if(abs(float(line_list[2][0:-1])-float(prev_x))>=5 or abs(float(line_list[4][0:-1])-float(prev_y))>=5):
        #     print(line_list[2][0:-1],line_list[4][0:-1],prev_x,prev_y,"yes")
        # else:          
        list3.append(line_list[2][0:-1])
        list3.append(line_list[4][0:-1])
        list2.append(list3)
        prev_x=line_list[2][0:-1]
        prev_y=line_list[4][0:-1]
    else:
        if(time==0 or line_list[0][:1]==time):
            time=line_list[0][:19]
        else:
            if(len(list2)==0):
                continue
            a,b=k_means(list2)
            list2=list(a)
            for index in range(len(list2)):
                list2[index]=np.insert(list2[index],2,b[index])
            list1.extend(list2[:])
            list2.clear()
            time=line_list[0][:19]

model=LocalOutlierFactor(n_neighbors=10)
clf=model.fit_predict(list1)
list3=[]
for index,point in enumerate(list1):
    if(clf[index]==1):
        list3.append(point)
x=[n[0] for n in list3]
y=[n[1] for n in list3]
plt.scatter(x,y)
plt.title("radar postion")
plt.xlabel("x")
plt.ylabel("y")
plt.show()