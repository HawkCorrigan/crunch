import math
import random
import numpy as np

def fun(x):
  return 0.5/(1+math.e**(9-x))

l = np.zeros(100)
f = []

for i in range(100):
    f.append(fun(i+1))
for i in range(1000000):
  j = 0
  if (i%40000==0):
      print(i)
  while(random.random()>f[j] and j<99):
    j+=1
    

  l[j]+=1

s = 0
for idx, i in enumerate(l):
  s+=i
  if s>500000:
    print(idx, s)
    break

