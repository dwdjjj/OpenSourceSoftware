# import string
# -*- coding: utf-8 -*-

# f = open('./data/class_score_kr.csv', 'r')
# lines = f.read()
# print(lines)
# f.close()

# f = open('data/class_score_en.csv', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()

# with open('data/class_score_kr.csv', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())
        
# with open('data/class_score_kr.csv', 'r') as fi, open('class_score_mean.csv', 'w') as fo:
#     for line in fi.readlines():
#         values = [int(text) for text in line.split(', ')]
#         mean = sum(values) / len(values)
#         for val in values:
#             fo.write(f'{val}, ')
#             fo.write(f'{mean}\n')
            
if (3 == 3.):
    print('같음')
else:
    print('다름')
    
import math
f_prod = lambda n: math.prod(range(1, n+1))
print(f_prod(10))

prof_set = {'Choi', 327, True}
prof_set == {'Choi', 327, True, True} # True
prof_set == {'Choi', True, 327} # True

prof = "Choi, 327, 1"
r0 = prof.split(',')# ['Choi', ' 327', ' 1']
r1 = prof.split(', ')  # ['Choi', '327', '1']
r2 = prof.split('|')  # ['Choi, 327, 1']
r3 = prof.partition(', ') # ('Choi', ', ', '327, 1’) 
print(f"prof.split(',')     : {r0}")
print(f"prof.split(', ')     : {r1}")
print(f"prof.split('|')     : {r2}")
print(f"prof.partition(', ')     : {r3}")

year_set = {1984, 1982, 2014, 2016} 
for item in year_set:
    print(item)
for num, item in enumerate(year_set):
    print(num, item) # 'num' is not a index.
    
import time
print(time.time())
print(time.localtime())
print(time.ctime())

import fnmatch
profs = ['My name is Choi and my E-mail is sunglok@seoultech.ac.kr.',
        'My name is Kim and my e-mail address is jindae.kim@seoultech.ac.kr.']

# For a single string
print([fnmatch.fnmatch(prof, 'e-mail') for prof in profs]) 
print([fnmatch.fnmatch(prof, '*e-mail*') for prof in profs]) 
print([fnmatch.fnmatchcase(prof, '*e-mail*') for prof in profs]) 
print([fnmatch.fnmatchcase(prof, '*[Ee]-mail*') for prof in profs]) 
# For a list of strings
print(fnmatch.filter(profs, '*e-mail*')) # ['My ... Choi ...', 'My ... Kim ...'] 
print(fnmatch.filter(profs, '*Ch?i*')) # ['My ... Choi ...']

# [False, False] # [True, True] # [False, True] # [True, True]


# import matplotlib.pyplot as plt 
# scale = 10
# xs = [x/scale for x in range(-4*scale, 10*scale)] 
# ys = [0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 for x in xs]
# plt.title('$y = 0.1x^3 - 0.8x^2 - 1.5x + 5.4$') # LaTeX style 
# plt.plot(xs, ys, 'r-')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid() 
# plt.axis('equal') 
# plt.show()
import matplotlib.pyplot as plt
scale = 10
xs = [x/scale for x in range(-4*scale, 10*scale)] 
ys = [0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 for x in xs] 
yt = [-3.5*x + 7 for x in xs]
plt.plot(xs, ys, 'r-', label='y')
plt.plot(xs, yt, 'b--', label='tangent line at x=2') 
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()

import sympy as sp
x, y = sp.symbols('x y')
y = 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4
yd = sp.diff(y, x)
print(yd) # 0.3*x**2 - 1.6*x - 1.5 
print(float(yd.subs({x: 2}))) # -3.5 / Casting from Float object to floa