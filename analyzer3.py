import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Given data
x = np.array([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], dtype=float)
y = np.array([0.06125166444740346, 0.16879432624113475, 0.2627986348122867, 0.4097222222222222, 0.4549019607843137, 0.38848920863309355, 0.4588235294117647, 0.5434782608695652, 0.3333333333333333, 0.5714285714285714, 0.6666666666666666, 0.5, 1.0], dtype=float)

# Define the function
def func(X, A, B):
    return 0.6 - 1.13**(-A * (X - B))

# Fit the function to the data
popt, pcov = curve_fit(func, x, y, p0=[1, 1])

# Extract the fitting parameters
A, B = popt

# Generate x values for plotting the fitted curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = func(x_fit, A, B)

# Plot the data and the fitted curve
plt.scatter(x, y, label='Data')
plt.plot(x_fit, y_fit, label=f'Fit: A={A:.4f}, B={B:.4f}', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Print the fitting parameters
A, B