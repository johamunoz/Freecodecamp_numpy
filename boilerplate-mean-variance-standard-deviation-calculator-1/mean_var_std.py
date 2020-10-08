import numpy as np

def calculate(list):
  if len(list) == 9:
    matrix=np.array(list).reshape(3,3)
    mean0=np.mean(matrix,axis=0).tolist()
    mean1=np.mean(matrix,axis=1).tolist()
    meanf=np.mean(matrix)
    var0=np.var(matrix,axis=0).tolist()
    var1=np.var(matrix,axis=1).tolist()
    varf=np.var(matrix)
    std0=np.std(matrix,axis=0).tolist()
    std1=np.std(matrix,axis=1).tolist()
    stdf=np.std(matrix)
    min0=np.min(matrix,axis=0).tolist()
    min1=np.min(matrix,axis=1).tolist()
    minf=np.min(matrix)
    max0=np.max(matrix,axis=0).tolist()
    max1=np.max(matrix,axis=1).tolist()
    maxf=np.max(matrix)
    sum0=np.sum(matrix,axis=0).tolist()
    sum1=np.sum(matrix,axis=1).tolist()
    sumf=np.sum(matrix)

    calculations={ 
      'mean': [mean0, mean1, meanf],
      'variance': [var0, var1, varf],
      'standard deviation': [std0, std1, stdf],
      'max': [max0, max1, maxf],
      'min': [min0, min1, minf],
      'sum': [sum0, sum1, sumf]}

  else:
    raise ValueError("List must contain nine numbers.")
    
  return calculations
