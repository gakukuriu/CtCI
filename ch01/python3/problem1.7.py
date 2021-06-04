import numpy as np

def rotation90(d):
  return np.fliplr(d.T)

N = 10
arr = np.random.randint(0, 256** 4, size=(N, N))
print(arr)
print(rotation90(arr))