import numpy as np
import matplotlib.pyplot as plt
import math

def func(x):
    return 0.6 - math.pow(1.16, -2*(x/2-5))

def mult(x,y):
    return x*y

x = (18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37)


y = (0.0006724949562878278, 0.0013458950201884253, 0.009433962264150943, 0.014285714285714285, 0.04209799861973775, 0.06556195965417867, 0.1125674633770239, 0.14856646394439618, 0.17244897959183675, 0.25400739827373614, 0.2793388429752066, 0.3623853211009174, 0.39928057553956836, 0.38323353293413176, 0.3883495145631068, 0.38095238095238093, 0.6410256410256411, 0.42857142857142855, 0.75, 1.0)

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