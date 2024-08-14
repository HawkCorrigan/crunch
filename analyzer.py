from numpy.random import default_rng
import numpy as np
from scipy.optimize import least_squares

def fun(x,t):
    return x[0]-np.power(x[1],(t-14)*x[2])

def loss(x,t,y):
    return fun(x,t)-y

x0 = np.array([1.0, 1.0, 1.0], dtype=float)

t_train = np.array([14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], dtype=float)
y_train = np.array([0.0017605633802816902, 0.010582010582010581, 0.0285204991087344, 0.05321100917431193, 0.0872093023255814, 0.1464968152866242, 0.20398009950248755, 0.253125, 0.2803347280334728, 0.3488372093023256, 0.35714285714285715, 0.4444444444444444], dtype=float)
res_lsq = least_squares(loss, x0, args=(t_train, y_train))

res_soft_l1 = least_squares(loss, x0, loss='soft_l1', f_scale=0.1, args=(t_train, y_train))
res_log = least_squares(loss, x0, loss='cauchy', f_scale=0.1, args=(t_train, y_train))

t_test = np.linspace(14, 29, 3 * 10)
y_lsq = fun(res_lsq.x, t_test)
y_soft_l1 = fun(res_soft_l1.x, t_test)
y_log = fun(res_log.x, t_test)

print(res_lsq)

import matplotlib.pyplot as plt

plt.plot(t_train, y_train, 'o')

plt.plot(t_test, y_lsq, 'k', linewidth=2, label='true')
y_lsq = fun(res_lsq.x, t_test)
y_soft_l1 = fun(res_soft_l1.x, t_test)
y_log = fun(res_log.x, t_test)

import matplotlib.pyplot as plt
plt.plot(t_train, y_train, 'o')
#plt.plot(t_test, y_true, 'k', linewidth=2, label='true')
plt.plot(t_test, y_lsq, label='linear loss')
plt.plot(t_test, y_soft_l1, label='soft_l1 loss')
plt.plot(t_test, y_log, label='cauchy loss')
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()