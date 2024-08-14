import numpy as np
import matplotlib.pyplot as plt
import math

def func(x):
    return 0.6 - math.pow(1.16, -2*(x/2-5))

def mult(x,y):
    return x*y

x = (13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27)

y = ( 0.01232394366197183, 0.026737967914438502, 0.056776556776556776, 0.11262135922330097, 0.17286652078774617, 0.25925925925925924, 0.31785714285714284, 0.3769633507853403, 0.3865546218487395, 0.4520547945205479, 0.45, 0.4090909090909091, 0.46153846153846156, 0.42857142857142855, 1.0)
y_func_specific = list(map(func, x))
l = zip(x,y)
lpfff = zip(x,y_func_specific)
l2 = []
lpfff2 = []
temp = 1
for x_i, y_i in l:
    l2.append(temp*y_i)
    temp*=(1-y_i)

temp = 1
for x_i, y_i in lpfff:
    lpfff2.append(temp*y_i)
    temp*=(1-y_i)

l = list(map(mult,x, l2))
lpfff = list(map(mult,x, lpfff2))


print(y_func_specific)
print("MULTIPLIERED")
print(sum(l))

print("MULTIPLIERED")
print(sum(lpfff))
sum=0
for y_iter in y:
    sum+=y_iter
    if(sum>0.5):
        print(y_iter)

# Plot the original data and the sigmoid function with specific parameters
plt.scatter(x, y, label='Data')
plt.plot(x, y_func_specific, label=f'Sigmoid fit', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Calculate and print the differences between the data and the specific sigmoid function
differences = y - y_sigmoid_specific
differences