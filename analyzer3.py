import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Given data
x = ()



x = np.array([24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47], dtype=float)
y = np.array([0.0013454423141607804, 0.0010104412260020209, 0.0023600809170600135, 0.005407232173031429, 0.016989466530750934, 0.035948842032492226, 0.04732879168160631, 0.07339104252916824, 0.1190089358245329, 0.13692946058091288, 0.1971153846153846, 0.2488356620093147, 0.2728077945084145, 0.26431181485992694, 0.326158940397351, 0.3759213759213759, 0.3543307086614173, 0.4329268292682927, 0.44086021505376344, 0.38461538461538464, 0.46875, 0.5294117647058824,  0.25, 0.3333333333333333], dtype=float)

# Define the function
#def func(X, A, B, C,D):
#    return C+D**(-A * (X - B))

# Fit the function to the data
#popt, pcov = curve_fit(func, x, y, p0=[1, 1, 1, -1])

# Extract the fitting parameters
#A, B , C, D= popt

# Generate x values for plotting the fitted curve
#x_fit = np.linspace(min(x), max(x), 100)
#y_fit = func(x_fit, A, B,C, D)

# Plot the data and the fitted curve
plt.scatter(x, y, label='Data')
#plt.plot(x_fit, y_fit, label=f'Fit: A={A:.4f}, B={B:.4f}, C={B:.4f}', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Print the fitting parameters
#A, B, C 