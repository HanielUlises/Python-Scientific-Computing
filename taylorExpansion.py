import numpy as np 
import matplotlib.pyplot as pt 


# Function based on the Taylor series expansion on the euler number
def expTaylor (x, x0, nMax):
    # x : argument
    # x0: argument at which the derivatives will be calculated
    # nMax: number n at which the series terminates
    t = 0;
    for n in range(nMax + 1):
        t = t + np.exp(x0) * (x-x0)**n / np.math.factiorial(n)
    return t

x_list = np.linspace(-5,5,101)
plt.scatter(x_list, np.exp(x_list))