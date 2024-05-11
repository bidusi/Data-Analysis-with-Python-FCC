import numpy as np

def mean(arr,axis):
  return np.mean(arr,axis).tolist()
def var(arr,axis):
  return np.var(arr,axis).tolist()
def std(arr,axis):
  return np.std(arr,axis).tolist()
def max(arr,axis):
  return np.max(arr,axis).tolist()
def min(arr,axis):
  return np.min(arr,axis).tolist()
def sum(arr,axis):
  return np.sum(arr,axis).tolist()


def calculate(lst):
    n=len(lst)
    print(n)
    if n==9:
      arr=np.reshape(np.array(lst),(3,3))
      thisdict = {"mean":[mean(arr, axis=0),mean(arr, axis=1),np.mean(arr)],
      "variance":[var(arr, axis=0),var(arr, axis=1),np.var(arr)],
      "standard deviation": [std(arr, axis=0),std(arr, axis=1),np.std(arr)],
      "max":[max(arr, axis=0),max(arr, axis=1),np.max(arr)],
      "min":[min(arr, axis=0),min(arr, axis=1),np.min(arr)],
      "sum":[sum(arr, axis=0),sum(arr, axis=1),np.sum(arr)]}
      return thisdict
    else:
     raise ValueError("List must contain nine numbers.")
    


