import numpy as np 
from hmmlearn import hmm
ob=np.array([1,0,0,1,1,0,0,1,1,0,1,1,0])
ob.shape=(len(ob),1)
model=hmm.MultinomialHMM(n_components=3)
np.random.seed(1)
model.fit(ob)
print(model.emissionprob_)
print(model.transmat_)
print(model.predict(ob))
print(model.predict_proba(ob)) 