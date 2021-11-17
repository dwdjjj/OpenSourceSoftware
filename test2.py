# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
true_curve = lambda x: 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 
data_range = (-6, 12)
data_num = 100
noise_std = 0.5
      # Generate the true data
x = np.random.uniform(data_range[0], data_range[1], size=data_num) 
y = true_curve(x)
      # Add Gaussian noise
xn = x + np.random.normal(scale=noise_std, size=x.shape) 
yn = y + np.random.normal(scale=noise_std, size=y.shape)
      # Solve the system of equations
A = np.vstack((xn**3, xn**2, xn, np.ones(xn.shape))).T
b=yn
curve = np.matmul(np.linalg.pinv(A), b)
      # Plot the data and result
plt.title(f'Curve: y={curve[0]:.3f}*$x^3$ + {curve[1]:.3f}*$x^2$ + {curve[2]:.3f}*$x$ + {curve[3]:.3f}')
xc = np.linspace(*data_range, 100)
plt.plot(xc, true_curve(xc), 'r-', label='The true curve')
plt.plot(xn, yn, 'b.', label='Noisy data')
plt.plot(xc, curve[0]*xc**3 + curve[1]*xc**2 + curve[2]*xc + curve[3], 'g-', label='Estimate') 
plt.xlim(data_range)
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
f = lambda x: 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 
fd = lambda x: 0.3*x**2 - 1.6*x - 1.5
viz_range = np.array([-6, 12])
learn_rate = 0.1 # Try 0.001, 0.01, 0.5, and 0.6 
max_iter = 100
min_tol = 1e-6
x_init = 12 # Try -2
# Prepare visualization
xs = np.linspace(*viz_range, 100)
plt.plot(xs, f(xs), 'r-', label='f(x)', linewidth=2) 
plt.plot(x_init, f(x_init), 'b.', label='Each step', markersize=12) 
plt.axis((*viz_range, *f(viz_range)))
plt.legend()

x = x_init
for i in range(max_iter):
    # Run the gradient descent
    xp = x
    x = x - learn_rate*fd(x)
    # Update visualization for each iteration
    print(f'Iter: {i}, x = {xp:.3f} to {x:.3f}, f(x) = {f(xp):.3f} to {f(x):.3f} (f\'(x) = {fd(xp):.3f})') 
    lcolor = np.random.rand(3)
    approx = fd(xp)*(xs-xp) + f(xp)
    plt.plot(xs, approx, '-', linewidth=1, color=lcolor, alpha=0.5)
    plt.plot(x, f(x), '.', color=lcolor, markersize=12)
    # Check the terminal condition
    if abs(x - xp) < min_tol: 
        break;
plt.show()