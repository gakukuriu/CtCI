import numpy as np

def toZeroArr(arr):
  rows = np.where(arr==0)[0]
  columns = np.where(arr==0)[1]

  for i in rows:
    arr[i] = np.zeros(arr.shape[1])

  for i in columns:
    for j in range(arr.shape[0]):
      arr[j][i] = 0

  return arr


M = 10
N = 15
arr = np.random.randint(0, 100, (M, N))
print(arr)
print(toZeroArr(arr))
