import numpy as np 
from hmmlearn import hmm
import math
ob=np.array([1,0,0,1,1,0,0,1,1,0,1,1,0])
ob.shape=(len(ob),1)
model=hmm.MultinomialHMM(n_components=3)
np.random.seed(1)
for i in range(10):
    model.fit(ob)
    a,b=model.decode([[1]])
    #np.append(ob,b)
    print(math.exp(a),b)